import pymongo
import time
from bson.objectid import ObjectId
"""
client=pymongo.MongoClient()
client = pymongo.MongoClient('mongodb://localhost:27017/')

db = client['quanlynha']
collection = db['devices']

#print(collection.find_one())

#x=collection.insert_one({'did': ObjectId('587d82b58f28f74cef9c518f')})
#y=collection.update_one({'_id': ObjectId('587d82b58f28f74cef9c518f')},{'$set':{'status': 0}})
#print(x.inserted_id,x.acknowledged)
#print(y.upserted_id,y.raw_result)

def updateStatus(id,status):
    rs = collection.update_one({'_id': ObjectId(id)}, {'$set': {'status': status}}).raw_result
    if rs['nModified']==1:
        print("Change status completed")
    else:
        print("Fail Cmnr")

updateStatus('587d82b58f28f74cef9c518f',0)

"""

class mongo:
    def __init__(self, address=None):

        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.db=self.client['quanlynha']
        self.device_c= self.db['devices']
        self.history_c = self.db['historys']

    def Create_Device(self,dname,address):

        check_address=self.device_c.find_one({'address': address})
        if check_address!=None:
            print("Address exist")
            return 300
        return_id=self.device_c.insert_one({ 'dname': dname, 'address': address, 'status': 0, 'power': 0}).inserted_id
        print(return_id)
        return return_id
    def Get_All_Device(self):
        result=self.device_c.find()
        print(result)
        return  result

    def updateStatus(self,id,status):
        rs = self.device_c.update_one({'_id': ObjectId(id)}, {'$set': {'status': status}}).raw_result
        if rs['nModified']==1:
            print("Change status completed")
            self.createHistory(id,status)
            return 200
        else:
            print("Fail Cmnr")
            return 201

    def createHistory(self,id,status):
        time_change=int(time.time())
        x = self.history_c.insert_one({'id': ObjectId(id), 'status': status, 'time': time_change})

    def Get_History(self,time_start,time_end,limit,skip):
        result= self.history_c.find({ 'time': {'$lte': time_start}, 'time': {'$gte': time_end}}).skip(skip).limit(limit).sort('time',-1)

        return result

    def Cursor_To_Array(self,cusor):
        array=()
        for it in cusor:
            print(it)
        print(cusor)

        return  array


db=mongo()
db.updateStatus('587f0bac067222055c4d6de4',0)
db.Create_Device("Đèn 1","abcd1")
x=db.Get_All_Device()
for doc in x:
    print(doc)

print(ObjectId())
z=db.Get_History(0,1484730697,2,0)
for doc in z:
    print(doc)
print(z)

