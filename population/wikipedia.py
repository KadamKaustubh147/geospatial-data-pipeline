import requests


class WikipediaClient:
    def __init__(self, user_agent: str):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": user_agent
        })
        self.api_url = "https://en.wikipedia.org/w/api.php"

    def search(self, query: str) -> str | None:
        params = {
            "action": "opensearch",
            "namespace": "0",
            "search": query,
            "limit": "5",
            "format": "json"
        }

        r = self.session.get(self.api_url, params=params)
        r.raise_for_status()
        data = r.json()

        return data[1][0] if data[1] else None

    def get_wikidata_id(self, title: str) -> str | None:
        params = {
            "action": "query",
            "titles": title,
            "prop": "pageprops",
            "ppprop": "wikibase_item",
            "format": "json"
        }

        r = self.session.get(self.api_url, params=params)
        r.raise_for_status()
        data = r.json()

        page = next(iter(data["query"]["pages"].values()))
        return page.get("pageprops", {}).get("wikibase_item")

    def get_area_sq_km(self, wikidata_id: str) -> float | None:
        url = f"https://www.wikidata.org/wiki/Special:EntityData/{wikidata_id}.json"

        r = self.session.get(url)
        r.raise_for_status()
        wd = r.json()

        entity = wd["entities"][wikidata_id]
        claims = entity.get("claims", {})
        area_claim = claims.get("P2046")  # area property

        if not area_claim:
            return None

        amount = area_claim[0]["mainsnak"]["datavalue"]["value"]["amount"]
        return float(amount)

    def get_coordinates(self, wikidata_id: str) -> dict | None:
        url = f"https://www.wikidata.org/wiki/Special:EntityData/{wikidata_id}.json"

        r = self.session.get(url)
        r.raise_for_status()
        wd = r.json()

        entity = wd["entities"][wikidata_id]
        claims = entity.get("claims", {})

        coord_claim = claims.get("P625")
        if not coord_claim:
            return None

        value = coord_claim[0]["mainsnak"]["datavalue"]["value"]

        return {
            "latitude": value["latitude"],
            "longitude": value["longitude"],
            "precision": value.get("precision"),
            "source": "wikidata"
        }