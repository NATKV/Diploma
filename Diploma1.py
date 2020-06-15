import requests
import json
import time

token = "958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008"

def get_params(add_params: dict = None):
    params = {"access_token": token, "v": 5.107}
    if add_params:
        for key in add_params:
            params[key] = add_params[key]
    return params


def get_request(method: str, params):
    url = f'https://api.vk.com/method/{method}'
    response = requests.get(url, params)
    result = response.json()
    return result


def get_user_id(short_name):
    special_params = {}
    special_params["user_ids"] = short_name
    special_params["extended"] = "1"
    parameters = get_params(special_params)
    new_method = "users.get"
    response = get_request(new_method, parameters)
    print(response)
    return response["response"][0]["id"]


def list_of_friends(id):
    special_params = {}
    special_params["user_id"] = id
    parameters = get_params(special_params)
    new_method = "friends.get"
    response = get_request(new_method, parameters)
    json = response["response"]
    if "items" in json:
        friends_list = []
        for each_friend in json["items"]:
            friends_list.append(each_friend)
        return friends_list
    else:
        print("Error:", json)
    return []


def get_groups(id):
    special_params = {}
    special_params["user_id"] = id
    parameters = get_params(special_params)
    new_method = "groups.get"
    response = get_request(new_method, parameters)
    if "response" in response:
        json = response["response"]
        if "items" in json:
            groups_list = json["items"]
            return groups_list
        else:
            print("Error:", json)

    else:
        print("Error:", response)
    return []


def info_groups(id):
    try:
        special_params = {}
        special_params["group_id"] = id
        special_params["fields"] = "members_count"
        parameters = get_params(special_params)
        new_method = "groups.getById"
        response = get_request(new_method, parameters)
        return {"name": response["response"][0]["name"], "gid": id,
                "members_count": response["response"][0]["members_count"]}

    except KeyError:
        return {}
