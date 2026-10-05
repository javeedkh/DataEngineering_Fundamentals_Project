import requests
import json
import os

os.makedirs("data", exist_ok=True)

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url)

    if response.status_code == 200:

        users = response.json()

        with open("data/users.json", "w") as f:
            json.dump(users, f, indent=4)

        print("\n" + "="*50)
        print("API INGESTION REPORT")
        print("="*50)

        print(f"Total Records Collected: {len(users)}")

        print("\nSample Data:")

        for user in users[:5]:
            print(
                f"ID: {user['id']} | "
                f"Name: {user['name']} | "
                f"Email: {user['email']} | "
                f"City: {user['address']['city']}"
            )

    else:
        print(f"API request failed with status code {response.status_code}")

except Exception as e:
    print("Error:", e)