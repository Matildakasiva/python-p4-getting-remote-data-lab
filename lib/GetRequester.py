import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    #sends a get request to the url passed on initialization, returns the body of the response
    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    # sends a request, then returns a dict made up of data converted from the response of that request
    def load_json(self):
        response = requests.get(self.url)
        return json.loads(response.content)