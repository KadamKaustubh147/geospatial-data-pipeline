from db import db

# # -----------------------------
# # Constituencies Schema
# # -----------------------------
# db.create_collection(
#     "constituencies",
#     validator={
#         "$jsonSchema": {
#             "bsonType": "object",
#             "required": ["name", "constituency", "email", "party", "phone_num"],
#             "properties": {
#                 "name": {"bsonType": "string"},
#                 "constituency": {"bsonType": "string"},
#                 "email": {"bsonType": "string"},
#                 "party": {"bsonType": "string"},
#                 "phone_num": {"bsonType": "string"}
#             }
#         }
#     }
# )

# # -----------------------------
# # Localities Schema
# # -----------------------------
# db.create_collection(
#     "localities",
#     validator={
#         "$jsonSchema": {
#             "bsonType": "object",
#             "required": [
#                 "name",
#                 "area_sq_km",
#                 "population",
#                 "male_population",
#                 "female_population",
#                 "coordinates",
#                 "constituency"
#             ],
#             "properties": {
#                 "name": {"bsonType": "string"},
#                 "area_sq_km": {"bsonType": "double"},
#                 "population": {"bsonType": "int"},
#                 "male_population": {"bsonType": "int"},
#                 "female_population": {"bsonType": "int"},
#                 "coordinates": {
#                     "bsonType": "object",
#                     "required": ["latitude", "longitude"],
#                     "properties": {
#                         "latitude": {"bsonType": "double"},
#                         "longitude": {"bsonType": "double"}
#                     }
#                 },
#                 "constituency": {"bsonType": "string"}
#             }
#         }
#     }
# )

# -----------------------------
# Education Institutes Schema
# -----------------------------
# db.create_collection(
#     "education_institutes",
#     validator={
#         "$jsonSchema": {
#             "bsonType": "object",
#             "required": [
#                 "name",
#                 "type",
#                 "address",
#                 "Phone_num",
#                 "mail_id",
#                 "locality_id"
#             ],
#             "properties": {
#                 "name": {"bsonType": "string"},
#                 "type": {
#                     "enum": ["School", "College", "University"]
#                     },    
#                 "address": {"bsonType": "string"},
#                 "Phone_num": {
#                     "bsonType": "array",
#                     "items": {"bsonType": "string"}
#                 },
#                 "mail_id": {
#                     "bsonType": "array",
#                     "items": {"bsonType": "string"}
#                 },
#                 "locality_id": {
#                     "bsonType": "objectId",
#                     "description": "Reference to localities collection"
#                 }
#             }
#         }
#     }
# )

# -----------------------------
# Hospitals Schema
# -----------------------------
db.create_collection(
    "hospitals",
    validator={
        "$jsonSchema": {
            "bsonType": "object",
            "required": [
                "name",
                "address",
                "contact",
                "opd_timings",
                "locality_id"
            ],
            "properties": {
                "name": {"bsonType": "string"},
                "address": {"bsonType": "string"},
                "contact": {
                    "bsonType": "array",
                    "items": {"bsonType": "string"}
                },
                "opd_timings": {"bsonType": "string"},
                "locality_id": {
                    "bsonType": "objectId",
                    "description": "Reference to localities collection"
                }
            }
        }
    }
)


print("✅ Collections created with schema validation")