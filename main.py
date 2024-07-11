from data import user_data
from http_requests import get_request

def main():
    data = user_data
    post_id = data['post_id']
    updated_request_body = data['updated_request_body']

    get_request(post_id, updated_request_body)

if _name_ == "_main_":
    main()

#sdsdssdsdd