def makeRESTCall(url):
    import json
    import requests

    if url != '':
        resp = requests.get(url)
    else:
        return "no url passed"
    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET /todos/ {}'.format(resp.status_code))
    json_data =  resp.json()
    return json_data

output = makeRESTCall('https://jsonplaceholder.typicode.com/todos/')
print('output: ' + str(output))
