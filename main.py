from requests import get_request, post_request, put_request, delete_request

if __name__ == "__main__":

    user_id = get_request()
    if user_id:
        print(f"Első felhasználó azonosítója: {user_id}")


    post_request()


    put_request()


    delete_request(1)