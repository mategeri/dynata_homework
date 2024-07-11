import requests
from constants import BASE_URL
from data import user_data

def get_request():
    url = BASE_URL
    response = requests.get(url)

    if response.status_code == 200:
        users = response.json()
        if users:
            first_user_id = users[0]['id']
            return first_user_id
    return None

def post_request():
    response = requests.post(BASE_URL, json=user_data)

    if response.status_code == 201:
        new_user = response.json()
        print("\nNew user successfully created:")
        print("Id: " + str(new_user['id']))
        print("Name: " + new_user['name'])
        print("Username: " + new_user['username'])
        print("Email: " + new_user['email'])
        return new_user['id'] if new_user else None
    else:
        print("\nError occurred during POST request: " + str(response.status_code))
        return None

def put_request():
    url = f"{BASE_URL}/1"
    updated_data = {
        "id": 1,
        "name": user_data['name'] + "_updated",
        "username": user_data['username'] + "_updated",
        "email": user_data['email'].replace('@', '_updated@')
    }
    headers = {
        'Content-type': 'application/json; charset=UTF-8'
    }
    response = requests.put(url, json=updated_data, headers=headers)
    if response.status_code == 200:
        updated_user = response.json()
        print("\nUser updated successfully:")
        print("Id: " + str(updated_user['id']))
        print("Name: " + updated_user['name'])
        print("Username: " + updated_user['username'])
        print("Email: " + updated_user['email'])
    else:
        print("\nError occurred during PUT request: " + str(response.status_code))
        print(response.text)

def delete_request(user_id):
    url = f"{BASE_URL}/{user_id}"

    response = requests.delete(url)

    if response.status_code == 200:
        print(f"\nUser with ID {user_id} successfully deleted!")
    else:
        print(f"\nError occurred during DELETE request for ID {user_id}: {response.status_code}")
        print(response.text)
