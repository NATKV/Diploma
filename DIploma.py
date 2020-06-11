import requests
import json

token = "958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008"

def get_user_id(short_name):

    params = {"access_token" : token, "v" : 5.107}
    params["user_ids"] = short_name
    params["extended"] = "1"
    URL = "https://api.vk.com/method/users.get"
    response = requests.get(URL,params)
    return response.json()["response"][0]["id"]


def list_of_friends(id):
    params = {"access_token" : token, "v" : 5.107}
    params["user_id"] = id
    URL = "https://api.vk.com/method/friends.get"
    response = requests.get(URL,params)

    friends_list = []
    for each_friend in response.json()["response"]["items"]:
        try:
            friends_list.append(each_friend)
            print("Well done!")
            return friends_list

        except:
            print("ERROR")
            return friends_list

def get_groups(id):
    try:
        params = {"access_token": token, "v": 5.107}
        params["user_id"] = id
        # params["extended"] = "1"
        URL = "https://api.vk.com/method/groups.get"
        response = requests.get(URL, params)
        groups_list = response.json()["response"]["items"]
        return groups_list

    except KeyError:
        return []

def info_groups(id):
    try:
        params = {"access_token": token, "v": 5.107}
        params["group_id"] = id
        params["fields"] = "members_count"
        URL = "https://api.vk.com/method/groups.getById"
        response = requests.get(URL, params)
        return {"name" : response.json()["response"][0]["name"], "gid" : id, "members_count" : response.json()["response"][0]["members_count"]}

    except KeyError:
        return {}


short_name = "eshmargunov"
id = get_user_id(short_name)

new_group = get_groups(id)
# print(new_group)

list_friends = list_of_friends(id)
# print(list_friends)

list_of_groups = []
for each_item in list_friends:
    list_of_groups.append(get_groups(each_item))
    # print(list_of_groups)

answer = new_group

for each_friend_list_of_group in list_of_groups:
    answer = set(answer) - set(each_friend_list_of_group)


result = []
for group_id in answer:
    result.append(info_groups(group_id))

with open('groups.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False)

with open("groups.json", encoding='utf-8') as f:
    print(f.read())











