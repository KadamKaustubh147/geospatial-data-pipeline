import requests

query = "Sricity"


S = requests.Session()
S.headers.update({
    "User-Agent": "SmartCityPopulationBot/1.0 (kaustubh@example.com)"
})

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "opensearch",
    "namespace": "0",
    "search": query,
    "limit": "5",
    "format": "json"
}

R = S.get(URL, params=PARAMS)

R.raise_for_status()  # fail fast if HTTP error
DATA = R.json()

# this is the page title of the first search result
print(DATA[1][0])




# scraping the page

PARAMS = {
    "action": "query",
    "titles": DATA[1][0],   # e.g. "Hampi"
    "prop": "pageprops",
    "ppprop": "wikibase_item",
    "format": "json"
}

r = S.get(URL, params=PARAMS)
r.raise_for_status()
data = r.json()

page = next(iter(data["query"]["pages"].values()))
wikidata_id = page["pageprops"]["wikibase_item"]

print(wikidata_id)  # e.g. Q5877

WIKIDATA_URL = "https://www.wikidata.org/wiki/Special:EntityData/{}.json".format(wikidata_id)

r = S.get(WIKIDATA_URL)
r.raise_for_status()
wd = r.json()

entity = wd["entities"][wikidata_id]
claims = entity["claims"]

area_claim = claims.get("P2046")

# in sq km2

if area_claim:
    area_value = area_claim[0]["mainsnak"]["datavalue"]["value"]["amount"]
    unit = area_claim[0]["mainsnak"]["datavalue"]["value"]["unit"]
    print("Area:", area_value, unit)
else:
    print("Area not available")
    # if area not available we get from geoiq thru search scraper
    



