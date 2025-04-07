import requests
import json

# Firebase database URL
firebase_url = "https://echo-of-humanity-cf3c2-default-rtdb.firebaseio.com/users.json"

# Data to send
data = {
    "GHQ10_A_10": "About the same as usual",
    "GHQ11_A_11": "More time than usual",
    "GHQ1_A_1": "Much less than usual",
    "GHQ2_A_2": "Much more than usual",
    "GHQ6_A_6": "Better than most",
    "GHQ7_A_7": "About the same as usual",
    "GHQ8_A_8": "Less satisfied than usual",
    "date_registered": "2025-03-05 09:33:58",
    "email": "mariadragneel008@gmail.com",
    "password": "sylus",
    "username": "mariam"
}

# Send POST request
response = requests.post(firebase_url, json=data)

# Check response
if response.status_code == 200:
    print("Data successfully sent to Firebase!")
else:
    print(f"Failed to send data. Status code: {response.status_code}")
    print(response.text)



