import requests,json,os
os.makedirs("data",exist_ok=True)
r=requests.get("https://jsonplaceholder.typicode.com/users")
users=r.json()
with open("data/users.json","w") as f: json.dump(users,f,indent=4)
print(f"Records Collected: {len(users)}")
