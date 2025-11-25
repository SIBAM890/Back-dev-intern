import requests
import json

BASE = "http://127.0.0.1:5000"

def run():
    # 1. Register an Admin
    print("Registering Admin...")
    reg = requests.post(f"{BASE}/auth/register", json={
        "username": "admin", "email": "admin@test.com", "password": "pass", "is_admin": True
    })
    print(reg.json())

    # 2. Login to get Token
    print("\nLogging in...")
    login = requests.post(f"{BASE}/auth/login", json={"email": "admin@test.com", "password": "pass"})
    token = login.json().get('access_token')
    headers = {"Authorization": f"Bearer {token}"}
    print("Got Token!")

    # 3. Create a Job
    print("\nCreating Job...")
    job = requests.post(f"{BASE}/jobs/", headers=headers, json={
        "title": "Flask Developer", "description": "Write code", "location": "Remote", "salary": "100k"
    })
    print(job.json())

    # 4. Check if it appears in the browser list
    print("\nNow check http://127.0.0.1:5000/jobs/ in your browser!")

if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        print(f"Error: {e} (Did you pip install requests?)")