from gc import get_objects

from endpoints.create_object import CreateObject
from endpoints.get_object import GetObject
from endpoints.udpate_object import UpdateObject
from endpoints.delete_object import DeleteObject

payload = {
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
}

def test_create_object():
   new_object_endpoint = CreateObject()
   new_object_endpoint.new_object(payload)
   new_object_endpoint.check_response_is_200()
   new_object_endpoint.check_name(payload['name'])

def test_get_object(obj_id): # в параметр ф-ии подставляется response["id"] (obj_id = response["id"])
   get_object_endpoint = GetObject()
   get_object_endpoint.get_by_id(obj_id)
   get_object_endpoint.check_response_is_200()
   get_object_endpoint.check_response_id(obj_id)

def test_update_object(obj_id):
   update_object_endpoint = UpdateObject()
   update_object_endpoint.update_by_id(obj_id,payload)
   update_object_endpoint.check_response_is_200()
   update_object_endpoint.check_response_name(payload['name'])

def test_delete_object(obj_id):
   delete_object_endpoint = DeleteObject()
   delete_object_endpoint.delete_by_id(obj_id)
   delete_object_endpoint.check_response_is_200()
   get_object_endpoint = GetObject()
   get_object_endpoint.get_by_id(obj_id)
   get_object_endpoint.check_response_is_404()