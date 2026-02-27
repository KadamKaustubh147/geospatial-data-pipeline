from db import db

constituencies = db["constituencies"]
localities = db["localities"]

# -----------------------------
# Insert Constituency
# -----------------------------
constituency_data = {
    "name": "Manoj kumar",
    "constituency": "Gurgaon Central",
    "email": "mla.gurgaon@example.com",
    "party": "ABC Party",
    "phone_num": "9876543210"
}

constituency_result = constituencies.insert_one(constituency_data)
print("Inserted Constituency ID:", constituency_result.inserted_id)

# -----------------------------
# Insert Locality
# -----------------------------
locality_data = {
    "name": "Sector 21",
    "area_sq_km": 4.5,
    "population": 25000,
    "male_population": 13000,
    "female_population": 12000,
    "coordinates": {
        "latitude": 28.4595,
        "longitude": 77.0266
    },
    "constituency": "Gurgaon Central"
}

locality_result = localities.insert_one(locality_data)
print("Inserted Locality ID:", locality_result.inserted_id)