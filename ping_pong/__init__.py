import requests
import time
import json
from you_api import API
import random

url = f"https:some_url_here{API}"


def ping():
    try:
        while True:
            response = requests.get(url)
            time.sleep(3)
            print(response.json(), time.ctime())
            with open('update_ping.json', 'w', encoding='utf-8') as file_json:
                json.dump(response.json(), file_json, indent=4, ensure_ascii=False)
    except ValueError:
        time_out = random.choice([1, 10, 15, 30])
        time.sleep(time_out)
        print('Error', time_out, time.ctime())
        return ping()
    except KeyboardInterrupt:
        print('Error INTERRUPTED')


ping()
