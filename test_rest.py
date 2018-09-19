import json
import requests

resp = requests.get('https://jsonplaceholder.typicode.com/todos/1', stream=True)
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /todos/1 {}'.format(resp.status_code))
json_data =  resp.json()

# print status_code
print('status_code:' + str(resp.status_code))

# print response
print (json_data)
print('userId:' + str(json_data['userId']))
print('id:' + str(json_data['id']))
print('title:' + str(json_data['title']))
print('completed:' + str(json_data['completed']))
