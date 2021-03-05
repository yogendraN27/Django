import requests
import json
BSAE_URL='http://127.0.0.1:8000/'
ENDPOINT='apiempall/'
# def get_resource():
#     resp=requests.get(BSAE_URL+ENDPOINT)
#     print(resp.content)
#     print(resp.status_code)
#     print(resp.json())
# get_resource()
def get_all():
    resp=requests.get(BSAE_URL+ENDPOINT)
    print(resp.json())
get_all()

def create_resource():
    new_emp={
        'eno':'109',
        'ename':'test',
        'esal':111,
        'eadd':'chhattisgarh',
    }
    resp=requests.post(BSAE_URL+ENDPOINT,data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())
    
create_resource()


    