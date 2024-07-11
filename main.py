from http_requests import get_request, post_request, put_request, delete_request

def main():
    print("Starting the process...\n")

    print("Getting the first user ID...")
    first_user_id = get_request()
    if first_user_id:
        print(f"First user ID: {first_user_id}\n")
    else:
        print("No users found.\n")

    print("Creating a new user...")
    new_user_id = post_request()
    if new_user_id:
        print(f"New user created with ID: {new_user_id}\n")
    else:
        print("Failed to create a new user.\n")
        return  # Exit if the new user creation failed

    print("Updating the new user...")
    put_request()

    print("Deleting the new user...")
    delete_request(new_user_id)

    print("\nProcess completed.")

if __name__ == "__main__":
    main()
