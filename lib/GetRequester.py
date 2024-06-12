import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        users_list = []
        users = json.loads(self.get_response_body())
        for user in users:
            users_list.append(user)
        return users_list

get_requester = GetRequester("https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json")

output = get_requester.load_json()

for i in output:
    print(f"{i['name']} is a {i['occupation']}")
