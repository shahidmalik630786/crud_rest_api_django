import requests
import json

URL1 = "http://127.0.0.1:8000/studentapi/"





def select_query_retrival(id=None):
    data={}
    if id is not None:
        data = {"id" : id}
    json_data=json.dumps(data)
    r=requests.get(url=URL1, data= json_data)
    data= r.json()
    print(data)

#complete data will be given
select_query_retrival()

#only id 2 data will be given
# select_query_retrival(2)


#insert
def insert_data():
    data={
    "name":"ahmed",
    "roll":101,
    "city":"vapi"
    }

    a1= json.dumps(data)

    r=requests.post(url=URL1,data=a1)

    data = r.json()
    print(data)

# insert_data()


#update
def update_data():
    data={
    "id":5,
    "name":"ahmed malik",
    }

    a1= json.dumps(data)

    r=requests.put(url=URL1,data=a1) #we will use patch 
                                     #to update partially
    data = r.json()
    print(data)

# update_data()

#delete
def delete_data():
    data={
    "id":5
    }
    a1= json.dumps(data)

    r=requests.delete(url=URL1,data=a1) #delete method
    data = r.json()
    print(data)

# delete_data()









