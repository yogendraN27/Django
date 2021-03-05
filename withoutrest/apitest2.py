import requests
import json
BSAE_URL='http://127.0.0.1:8000/'
ENDPOINT='apiemp/'
def get_resource(id=None):
    data={}
    if id is not None:
        data={
            'id':id
        }
    resp=requests.get(BSAE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
get_resource(3)

#get data by Id
# def get_resource(id):
#     resp=requests.get(BSAE_URL+ENDPOINT+id+'/')
#     #print(resp.content)
#     print(resp.status_code)
#     print(resp.json())
# id=input('Enter ID:' )
# get_resource(id)

def update_resource(id):
    new_emp={
        'esal':5550,
    }
    resp=requests.put(BSAE_URL+ENDPOINT+str(id)+'/',data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())
update_resource(8)

def delete_resource(id):
    resp=requests.delete(BSAE_URL+ENDPOINT+id+'/')
    #print(resp.content)
    print(resp.status_code)
    print(resp.json())
id=input('Enter ID:' )
delete_resource(id)

