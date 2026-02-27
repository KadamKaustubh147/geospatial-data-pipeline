import re
from typing import Optional
from collections import Counter
import time
import random
from ddgs import DDGS


class CoordinatesResolver:
    def __init__(self, wiki_client, proxy: str | None = None):
        self.wiki = wiki_client
        self.ddgs = DDGS(proxy=proxy)

    # ---------- Wikipedia / Wikidata ----------
    def from_wikipedia(self, wikidata_id: str | None) -> Optional[dict]:
        if not wikidata_id:
            return None

        coords = self.wiki.get_coordinates(wikidata_id)
        if not coords:
            return None

        return {
            "latitude": coords["latitude"],
            "longitude": coords["longitude"],
            "source": "wikidata",
        }

    # ---------- IndiaMappia (stabilized) ----------
    def from_indiamapia(self, query: str, retries: int = 5) -> Optional[dict]:
        hits = []

        for _ in range(retries):
            results = self.ddgs.text(
                f"{query} latitude longitude indiamapia.com",
                max_results=5
            )

            for r in results:
                text = f"{r.get('title','')} {r.get('body','')}"

                # Pattern 1: Latitude: 26.4652 Longitude: 80.3498
                m = re.search(
                    r"Latitude\s*[:=]\s*(\d+(?:\.\d+)?).*?"
                    r"Longitude\s*[:=]\s*(\d+(?:\.\d+)?)",
                    text,
                    re.I
                )
                if m:
                    lat = round(float(m.group(1)), 4)
                    lon = round(float(m.group(2)), 4)
                    hits.append((lat, lon))
                    break

                # Pattern 2: 26.4652 N and 80.3498 E
                m = re.search(
                    r"(\d+(?:\.\d+)?)\s*[Nn].*?(\d+(?:\.\d+)?)\s*[Ee]",
                    text
                )
                if m:
                    lat = round(float(m.group(1)), 4)
                    lon = round(float(m.group(2)), 4)
                    hits.append((lat, lon))
                    break

            # jitter (important)
            time.sleep(1.5 + random.uniform(0.5, 1.0))

        if not hits:
            return None

        (lat, lon), freq = Counter(hits).most_common(1)[0]

        return {
            "latitude": lat,
            "longitude": lon,
            "source": "indiamapia",
            "retries": retries
        }

    # ---------- Public API ----------
    def resolve(self, place_name: str, wikidata_id: str | None) -> Optional[dict]:
        result = self.from_wikipedia(wikidata_id)
        if result:
            return result

        return self.from_indiamapia(place_name)


# ---------- Manual test ----------
if __name__ == "__main__":
    from wikipedia import WikipediaClient
    from decouple import config

    query = "Vijay Nagar Kanpur"

    wiki = WikipediaClient(
        user_agent="SmartCityPopulationBot/1.0 (kaustubh@example.com)"
    )

    resolver = CoordinatesResolver(
        wiki_client=wiki,
        proxy=config("PROXY_SERVER", default=None)
    )

    coords = resolver.resolve(place_name=query, wikidata_id=None)

    if coords:
        print("Coordinates found:")
        print(coords)
    else:
        print("Coordinates not found")