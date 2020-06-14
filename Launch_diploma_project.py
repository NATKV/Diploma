import Diploma
import json
import time


def main():
    short_name = "eshmargunov"
    id = Diploma.get_user_id(short_name)

    new_group = Diploma.get_groups(id)
    # print(new_group)

    list_friends = Diploma.list_of_friends(id)
    # print(list_friends)

    list_of_groups = []
    for each_item in list_friends:
        Diploma.time.sleep(0.5)
        list_of_groups.append(Diploma.get_groups(each_item))
        # print(list_of_groups)

    answer = new_group

    for each_friend_list_of_group in list_of_groups:
        answer = set(answer) - set(each_friend_list_of_group)

    result = []
    for group_id in answer:
        Diploma.time.sleep(0.5)
        result.append(Diploma.info_groups(group_id))

    with open('../.idea/groups.json', 'w', encoding='utf-8') as f:
        Diploma.json.dump(result, f, ensure_ascii=False)

    with open("../.idea/groups.json", encoding='utf-8') as f:
        print(f.read())


if __name__ == "__main__":
    main()