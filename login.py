from project import menu
import json
def login_app():

    list = []
    user_email = input("\033[1mEmail : \033[0m")

    password = input("\033[1mPassword : \033[0m")

    json_file = open('users_data.json')
    for line in json_file:
        Dict = json.loads(line)
        list.append(Dict)

    for dict in list:
        if user_email == dict['email'] and password == dict['password']:
            print("login successfull,Welcome Sir *_*")
            user_id = dict['user_id']
            menu(user_id)
            break
    else:
        print("invalid data ,, please try again")
        login_app()
