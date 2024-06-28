import json 
import random 
from faker import Faker 

fake = Faker() 

# function for generating single record
def generate_record(record_id):
    return {
        "id": record_id,
        "name": fake.name(),
        "compensation": random.randint(3, 12) * 10000,
        "exempt": random.choice([True, False]),
        "DOB": int(round(random.uniform(3, 4), 6) * 10**11)
    }

# generate 50 records
data = [generate_record(i) for i in range(1, 51)]

# save to a JSON file
with open('emp_data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("Data generated and saved to emp_data.json")
