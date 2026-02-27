from decouple import config
from wikipedia import WikipediaClient
from search import GeoIQSearcher
from coordinates import CoordinatesResolver


def main(query: str):
    wiki = WikipediaClient(
        user_agent="SmartCityPopulationBot/1.0 (kaustubh@example.com)"
    )

    proxy = config("PROXY_SERVER", default=None)

    geoiq = GeoIQSearcher(proxy=proxy)
    coord_resolver = CoordinatesResolver(wiki_client=wiki, proxy=proxy)

    result = {
        "query": query,
        "wikipedia": None,
        "wikidata": {},
        "coordinates": None,
        "geoiq": None,
    }

    # ---------- Wikipedia (OPTIONAL) ----------
    title = wiki.search(query)
    if title:
        result["wikipedia"] = {"title": title}

        wikidata_id = wiki.get_wikidata_id(title)
        if wikidata_id:
            result["wikidata"]["id"] = wikidata_id
            result["wikidata"]["area_sq_km"] = wiki.get_area_sq_km(wikidata_id)
    else:
        wikidata_id = None  # important

    # ---------- Coordinates (NOT dependent on Wikipedia) ----------
    coords = coord_resolver.resolve(query, wikidata_id)
    result["coordinates"] = coords

    # ---------- GeoIQ (ALWAYS TRY) ----------
    geoiq_data = geoiq.find_place(query)
    result["geoiq"] = geoiq_data

    # ---------- Final output ----------
    print("\n=== FINAL DATA ===")
    for k, v in result.items():
        print(f"\n{k.upper()}:")
        print(v)


if __name__ == "__main__":
    main("Vijay Nagar Kanpur")