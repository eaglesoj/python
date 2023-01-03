import json
import requests

resp = requests.get('https://jsonplaceholder.typicode.com/todos/')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /todos/ {}'.format(resp.status_code))
json_data =  resp.json()

# print status_code
print('status_code:' + str(resp.status_code))

# print response
print (json_data)

# only print record if id is 4
for items in json_data:
    if (items['id'] == 4):
        print ('items:' + str(items))
        print('userId:' + str(items['userId']))
        print('id:' + str(items['id']))
        print('title:' + str(items['title']))
        print('completed:' + str(items['completed']))
        break