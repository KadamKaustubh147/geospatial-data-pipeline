import time
import random
import re
from collections import Counter
from ddgs import DDGS


class GeoIQSearcher:
    def __init__(self, proxy: str | None = None):
        self.ddgs = DDGS(proxy=proxy)

    def _parse_geoiq_text(self, text: str) -> dict:
        """
        Extract structured data from GeoIQ body text.
        Assumes GeoIQ's standard sentence templates.
        """
        data = {}

        patterns = {
            "locality": r"locality\s+(.+?)\s+falls",
            "district": r"falls in\s+(.+?)\s+district",
            "state": r"situated in\s+(.+?)\s+state",
            "population": r"population\s+(\d+)",
            "male_female": r"male and female populations are\s+(\d+)\s+and\s+(\d+)",
            "area": r"area is about\s+([\d.]+)\s+square\s+kilometer",
        }

        if m := re.search(patterns["locality"], text, re.I):
            data["locality"] = m.group(1)

        if m := re.search(patterns["district"], text, re.I):
            data["district"] = m.group(1)

        if m := re.search(patterns["state"], text, re.I):
            data["state"] = m.group(1)

        if m := re.search(patterns["population"], text):
            data["population"] = int(m.group(1))

        if m := re.search(patterns["male_female"], text, re.I):
            data["male_population"] = int(m.group(1))
            data["female_population"] = int(m.group(2))

        if m := re.search(patterns["area"], text, re.I):
            data["area_sq_km"] = float(m.group(1))

        return data

    def find_place(self, query: str, retries: int = 5) -> dict | None:
        final_query = f"{query} geoiq"
        all_hits = []

        for _ in range(retries):
            try:
                results = self.ddgs.text(
                    final_query,
                    max_results=10,
                    backend="duckduckgo"
                )
            except Exception:
                time.sleep(4)
                continue

            for r in results:
                href = r.get("href", "")
                if "geoiq.io/places" in href:
                    all_hits.append((
                        href,
                        r.get("title", ""),
                        r.get("body", "")
                    ))
                    break

            time.sleep(2 + random.uniform(0.5, 1.5))

        if not all_hits:
            return None

        (href, title, body), freq = Counter(all_hits).most_common(1)[0]

        parsed_data = self._parse_geoiq_text(body)

        return {
            "source": "geoiq",
            "title": title,
            "url": href,
            "frequency": freq,
            "raw_text": body,
            "parsed": parsed_data
        }