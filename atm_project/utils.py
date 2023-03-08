import json
import os

USER_DATA_DIR = "user_data"


def create_user_dir():
    if not os.path.exists(USER_DATA_DIR):
        os.makedirs(USER_DATA_DIR)
    else:
        print("This folder already exists.")


def check_file_exists(file_name):
    return os.path.exists(f"{USER_DATA_DIR}/{file_name}")


def get_user_data(file_name):
    if check_file_exists(file_name):
        with open(f"{USER_DATA_DIR}/{file_name}", "r") as file:
            return json.loads(file.read())

    return {}


def create_user_file(file_name: str, data: dict):
    create_user_dir()

    with open(f"{USER_DATA_DIR}/{file_name}", "w") as file:
        file.write(json.dumps(data))
        return True

    return False
