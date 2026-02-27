from db import db
from bson import ObjectId
constituencies = db["constituencies"]
localities = db["localities"]
education_collection = db["education_institutes"]

# # -----------------------------
# # Insert Constituency
# # -----------------------------
# constituency_data = {
#     "name": "Sri K. Adimulam",
#     "constituency": "Satyavedu",
#     "email": "",
#     "party": "Telugu Desam Party",
#     "phone_num": "9393730377"
# }

# constituency_result = constituencies.insert_one(constituency_data)
# print("Inserted Constituency ID:", constituency_result.inserted_id)

# # -----------------------------
# # Insert Locality
# # -----------------------------
# locality_data = {
#     "name": "Sricity",
#     "area_sq_km": 89.8,
#     "population": 25602,
#     "male_population": 12693,
#     "female_population": 12909,
#     "coordinates": {
#         "latitude": 13.557673,
#         "longitude": 80.029489
#     },
#     "constituency": "Satyavedu"
# }

# locality_result = localities.insert_one(locality_data)
# print("Inserted Locality ID:", locality_result.inserted_id)


# education_data = [

#     {
#         "name": "Chinmaya Vidyalaya (CBSE)",
#         "type": "School",
#         "address": "Sri City Chinmaya Vidyalaya, Pioneer Avenue, SriCity, NHS, Near TADA, Andhra Pradesh – 524401",
#         "Phone_num": ["+91-8919760536"],
#         "mail_id": ["sccvprincipal@gmail.com"],
#         "locality_id": ObjectId("69a1f7f5b9babf2ae6bd2664")
#     },

#     {
#         "name": "Accord School",
#         "type": "School",
#         "address": "Sri City, Andhra Pradesh",
#         "Phone_num": ["+91-9100944448"],
#         "mail_id": [
#             "sricityinfo@theaccordschool.com",
#             "sricityadmissions@theaccordschool.com"
#         ],
#         "locality_id": ObjectId("69a1f7f5b9babf2ae6bd2664")
#     },

#     {
#         "name": "Padmavathi Vidhyalaya (CBSE)",
#         "type": "School",
#         "address": "Pulivendra Village, Tada Mandal, Tada, SPSR Nellore Dist. Andhra Pradesh",
#         "Phone_num": [
#             "+91-9346610414",
#             "+91-9908154742",
#             "+91-9959579374"
#         ],
#         "mail_id": [],
#         "locality_id": ObjectId("69a1f7f5b9babf2ae6bd2664")
#     },

#     {
#         "name": "RMK Patasala",
#         "type": "School",
#         "address": "RSM Nagar, Kavaraipettai, Gummidipoondi Taluk, Tiruvallur District, Tamil Nadu",
#         "Phone_num": ["044-67911234", "044-67911200"],
#         "mail_id": [],
#         "locality_id": ObjectId("69a1f7f5b9babf2ae6bd2664")
#     },

#     {
#         "name": "RMK International School (Residential) (CBSE)",
#         "type": "School",
#         "address": "RMK Residential Senior Secondary School, N.H. 5, RSM Nagar, Kavaraipettai, Gummidipoondi, Tamil Nadu – 601206, India",
#         "Phone_num": ["044-67901234"],
#         "mail_id": [],
#         "locality_id": ObjectId("69a1f7f5b9babf2ae6bd2664")
#     },

#     {
#         "name": "Holy Cross High School (CBSE)",
#         "type": "School",
#         "address": "NH16, Sullurupeta, Andhra Pradesh 524121",
#         "Phone_num": [],
#         "mail_id": [],
#         "locality_id": ObjectId("69a1f7f5b9babf2ae6bd2664")
#     },

#     {
#         "name": "Tiny Tots English Medium School (CBSE)",
#         "type": "School",
#         "address": "Government Hospital Road, Sullurpet, Nellore – 524121",
#         "Phone_num": ["+91-8623242424"],
#         "mail_id": [],
#         "locality_id": ObjectId("69a1f7f5b9babf2ae6bd2664")
#     },

#     {
#         "name": "Champion School (CBSE)",
#         "type": "School",
#         "address": "Railway Station Road, Sullurupeta, Andhra Pradesh 524121",
#         "Phone_num": [],
#         "mail_id": [],
#         "locality_id": ObjectId("69a1f7f5b9babf2ae6bd2664")
#     },

#     {
#         "name": "Sri Venkateswara English Medium High School (CBSE)",
#         "type": "School",
#         "address": "Tada, Andhra Pradesh 524401",
#         "Phone_num": ["+91-8302511111"],
#         "mail_id": ["support@studyapt.com"],
#         "locality_id": ObjectId("69a1f7f5b9babf2ae6bd2664")
#     },

#     {
#         "name": "Dr.C V Raman Public High School (BSEAP)",
#         "type": "School",
#         "address": "Tada, Andhra Pradesh",
#         "Phone_num": [],
#         "mail_id": [],
#         "locality_id": ObjectId("69a1f7f5b9babf2ae6bd2664")
#     },

#     {
#         "name": "St.Marys Matriculation School (TN state Board)",
#         "type": "School",
#         "address": "Eluru By pass Road 2, Railway Over Bridge, NH16, Arambakkam, Tamil Nadu 601207",
#         "Phone_num": ["044-27948255", "044-27900771"],
#         "mail_id": [],
#         "locality_id": ObjectId("69a1f7f5b9babf2ae6bd2664")
#     }

# ]

# education_collection.insert_many(education_data)

# print("✅ All education institutes inserted successfully")

# college_data = [

#     {
#         "name": "Indian Institute of Information Technology (IIIT), Sri City",
#         "type": "College",
#         "address": "Indian Institute of Information Technology, Sri City, 630 Gnan Marg, Sri City, Satyavedu Mandal, Chittoor District – 517646, Andhra Pradesh, India",
#         "Phone_num": [
#             "+91-7306473364",
#             "+91-7032851919",
#             "+91-9177319115",
#             "+91-9550380002"
#         ],
#         "mail_id": [
#             "admissions@iiits.in",
#             "dasa@iiits.in",
#             "pgadmissions@iiits.in",
#             "placement.office@iiits.in",
#             "contact@iiits.in"
#         ],
#         "locality_id": ObjectId("69a1f7f5b9babf2ae6bd2664")
#     },

#     {
#         "name": "IIT Tirupati",
#         "type": "College",
#         "address": "Tirupati, Andhra Pradesh, India",
#         "Phone_num": ["0877-250-3530"],
#         "mail_id": ["iittirupati@iittp.ac.in"],
#         "locality_id": ObjectId("69a1f7f5b9babf2ae6bd2664")
#     },

#     {
#         "name": "Gokula Krishna College of Engineering, Sullurpeta",
#         "type": "College",
#         "address": "Behind RTC Depot, Sullurpet, Nellore Dist., Andhra Pradesh-524121",
#         "Phone_num": [
#             "086232-41777",
#             "+91-8179974369",
#             "+91-9848813706",
#             "+91-9848813707"
#         ],
#         "mail_id": ["gkcesp@rediffmail.com"],
#         "locality_id": ObjectId("69a1f7f5b9babf2ae6bd2664")
#     },

#     {
#         "name": "Indian Institute of Science Education and Research Tirupathi",
#         "type": "College",
#         "address": "C/o Sree Rama Engineering College (Transit Campus), Rami Reddy Nagar, Karakambadi Road, Mangalam (P.O.) Tirupati -517507, Andhra Pradesh, India",
#         "Phone_num": ["0877-2500400"],
#         "mail_id": [],
#         "locality_id": ObjectId("69a1f7f5b9babf2ae6bd2664")
#     },

#     {
#         "name": "Government Junior College- Telugu Medium",
#         "type": "College",
#         "address": "Sullurupeta, Andhra Pradesh 524121",
#         "Phone_num": [],
#         "mail_id": [],
#         "locality_id": ObjectId("69a1f7f5b9babf2ae6bd2664")
#     }

# ]

# education_collection.insert_many(college_data)

# print("✅ College data inserted successfully")

# -----------------------------
# Insert Hospitals
# -----------------------------
hospitals_collection = db["hospitals"]

hospital_data = [
    {
        "name": "Sri Ramachandra Hospital",
        "address": "Ground Floor, 305 North, 2nd St, Sri City, Andhra Pradesh- 517646",
        "contact": ["+91-9080605607", "08576-293329"],
        "opd_timings": "All Day",
        "locality_id": ObjectId("69a1f7f5b9babf2ae6bd2664")
    },
    {
        "name": "Medicover Clinic",
        "address": "1st Floor, The Arcade, Central Expressway, Sri City",
        "contact": ["+91-90100327129"],
        "opd_timings": "9 am to 6 pm everyday",
        "locality_id": ObjectId("69a1f7f5b9babf2ae6bd2664")
    },
    {
        "name": "Satish Dhawan Memorial Hospital",
        "address": "Pulicat Nagar, Sullurupeta, Andhra Pradesh 524121",
        "contact": ["(086232)-30200"],
        "opd_timings": "",
        "locality_id": ObjectId("69a1f7f5b9babf2ae6bd2664")
    },
    {
        "name": "Sri Pottipati Obul Reddy Government Hospital",
        "address": "Eluru By pass Road 2, Railway Over Bridge, on National Highway 5, Andhra Pradesh 524401",
        "contact": ["096751 86779"],
        "opd_timings": "",
        "locality_id": ObjectId("69a1f7f5b9babf2ae6bd2664")
    },
    {
        "name": "Mother Joseph Hospital",
        "address": "NH Service Road, Arambakkam, Andhra Pradesh 524401",
        "contact": ["(044)-27900755"],
        "opd_timings": "",
        "locality_id": ObjectId("69a1f7f5b9babf2ae6bd2664")
    },
    {
        "name": "Lavanya Hospital",
        "address": "Lavanya Hospital, Opp Court, Sathyavedu Mandal, Chittoor District 517 588",
        "contact": ["+91-9493815548"],
        "opd_timings": "",
        "locality_id": ObjectId("69a1f7f5b9babf2ae6bd2664")
    }
]

hospitals_collection.insert_many(hospital_data)

print("✅ Hospital data inserted successfully")