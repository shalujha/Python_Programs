# stands for Java Script Object notation
# light weight data Interchange Format
# data is shared in the form of json between clients and servers
# process of convert object into a file is called serialization
# pyhton objects are in ram and json file are in secondary storage
import json,pprint
book={
    "name":"Learning Python",
    "page":320,
    "authors":[
        {
            "name":"A1",
            "age":30
        },
        {
            "name":"A2",
            "age": 40
        }
    ]
}
print(type(book))
print(book["authors"][0])
print(type(book["authors"][0]))
with open("myJsonFile.json",'w') as f: # it is creating a file whose name is myjsonFile in writable mode 
    json.dump(book,f) # it has content of book object and file handler f.takes ist parameter the object u want to serialize and the file where u want to serialize
s=json.dumps(book) # basically returns a string(conversion of object into string i.e serialization)
# dump and dumps method are for serialization
object=json.loads(s) # converting a string into object(deserialization)
print(object)
print(type(object))
with open("myjsonFile.json",'r') as f:
    data=json.load(f)
    pprint.pprint(data) # if json file is very large use pprint to ease the interpret of data


