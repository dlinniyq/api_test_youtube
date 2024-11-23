import requests
from endpoints.base_endpoint import Endpoint

class DeleteObject(Endpoint):

    def delete_by_id(self,id):
        self.response = requests.delete(f"https://api.restful-api.dev/objects/{id}")
        self.response_json = self.response.json()