import requests
from constants import BASE_URL
from data import user_data

def get_request():
    response = requests.get(BASE_URL)

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
        print("\nÚj felhasználó sikeresen létrehozva:")
        print("Id: " + str(new_user['id']))
        print("Name: " + new_user['name'])
        print("Username: " + new_user['username'])
        print("Email: " + new_user['email'])
        return new_user['id'] if new_user else None
    else:
        print("\nHiba történt a POST kérés során: " + str(response.status_code))
        return None

def put_request(user_id):
    url = f"{BASE_URL}/{user_id}"

    updated_data = {
        "id": user_id,
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
        print("\nFelhasználó frissítve:")
        print("Id: " + str(updated_user['id']))
        print("Name: " + updated_user['name'])
        print("Username: " + updated_user['username'])
        print("Email: " + updated_user['email'])
    else:
        print("\nHiba történt a PUT kérés során: " + str(response.status_code))
        print(response.text)

def delete_request(user_id):
    url = f"{BASE_URL}/{user_id}"

    response = requests.delete(url)

    if response.status_code == 200:
        print(f"\nA(z) {user_id} azonosítójú felhasználó sikeresen törölve!")
    else:
        print(f"\nHiba történt a DELETE kérés során az {user_id} azonosítóval: {response.status_code}")
        print(response.text)
