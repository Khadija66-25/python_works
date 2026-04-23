frame_works = [
    {"name": "django", "language": "python", "rating": 5},
    {"name": "odoo", "language": "python", "rating": 4},
    {"name": "fastapi", "language": "python", "rating": 5},
    {"name": "spring", "language": "java", "rating": 5},
    {"name": "angular", "language": "javascript", "rating": 5},
    {"name": "nest", "language": "javascript", "rating": 5},
    {"name": "express", "language": "javascript", "rating": 5}
]

#print the all frame works name 
            #normal method

#for fw in frame_works:

    #print(fw.get("name"))

    #comprehensive method
all_frame_works = {fw.get("name") for fw in frame_works}
print(all_frame_works)
