# from ddgs import DDGS

# # query = "Vijay nagar kanpur"
# query = "Seawoods"

# final_query = f"{query} geoiq"
# # final_query = f"{query} geoiq area in square km"

# results = DDGS().text(final_query, max_results=5)
# print(results[0])


from ddgs import DDGS
from collections import Counter
import time
import random
from decouple import config

proxy = config("PROXY_SERVER")

ddgs = DDGS(proxy=proxy)
# ddgs = DDGS()

query = "noida"
final_query = f"{query} geoiq"

all_hits = []

for i in range(5):
    try:
        results = ddgs.text(
            final_query,
            max_results=10
        )
    except Exception as e:
        print(e)
        print(f"Search {i+1} failed, cooling down")
        time.sleep(4)
        continue

    for r in results:
        href = r.get("href", "")
        title = r.get("title", "")
        body = r.get("body", "")

        if "geoiq.io/places" in href:
            all_hits.append((href, title, body))
            break

    # delay + jitter (important even with proxy)
    time.sleep(2 + random.uniform(0.5, 1.5))

if not all_hits:
    print("No GeoIQ place found after retries")
else:
    counter = Counter(all_hits)
    (href, title, body), freq = counter.most_common(1)[0]

    print({
        "title": title,
        "href": href,
        "body": body,
        "frequency": freq
    })