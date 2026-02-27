from db import db

# -----------------------------
# Constituencies Schema
# -----------------------------
db.create_collection(
    "constituencies",
    validator={
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["name", "constituency", "email", "party", "phone_num"],
            "properties": {
                "name": {"bsonType": "string"},
                "constituency": {"bsonType": "string"},
                "email": {"bsonType": "string"},
                "party": {"bsonType": "string"},
                "phone_num": {"bsonType": "string"}
            }
        }
    }
)

# -----------------------------
# Localities Schema
# -----------------------------
db.create_collection(
    "localities",
    validator={
        "$jsonSchema": {
            "bsonType": "object",
            "required": [
                "name",
                "area_sq_km",
                "population",
                "male_population",
                "female_population",
                "coordinates",
                "constituency"
            ],
            "properties": {
                "name": {"bsonType": "string"},
                "area_sq_km": {"bsonType": "double"},
                "population": {"bsonType": "int"},
                "male_population": {"bsonType": "int"},
                "female_population": {"bsonType": "int"},
                "coordinates": {
                    "bsonType": "object",
                    "required": ["latitude", "longitude"],
                    "properties": {
                        "latitude": {"bsonType": "double"},
                        "longitude": {"bsonType": "double"}
                    }
                },
                "constituency": {"bsonType": "string"}
            }
        }
    }
)

print("✅ Collections created with schema validation")