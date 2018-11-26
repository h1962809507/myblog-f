import json
import requests


def storage(file):
    url = "https://sm.ms/api/upload"

    response = requests.post(url, data={"ssl": True, }, files={"smfile": file})

    response_dict = json.loads(response.text)

    code = response_dict.get("code")

    if code != "success":
        raise Exception(code)

    img_url = response_dict.get("data").get("url")
    delete_url = response_dict.get("data").get("delete")

    return img_url


if __name__ == '__main__':
    file = None
    with open("./1.jpg", 'rb') as f:
        file = f.read()
    url = storage(file)
    print(url)
