import requests
BSAE_URL='https://jsonplaceholder.typicode.com/'
ENDPOINT='todos/'
def get_resource():
     resp=requests.get(BSAE_URL+ENDPOINT)
     #print(resp.content)
     print(resp.status_code)
     print(resp.json())
get_resource()