from bottle import route, run, post, get, request
from pymongo import MongoClient

MONGODB_URI = "mongodb://wework:wework1@ds163825.mlab.com:63825/wework"
client = MongoClient(MONGODB_URI, connectTimeoutMS=30000)
db = client.get_database("wework")
collection = db.names
namesArray = []

for name in collection.find():
    namesArray.append(name['name'])

message = """<html>
<body>
    <div>
        <p>Names: {namesArray}</p> 
        </br>
        </br>
        </br>
    </div>

    <form method="POST" action="/addName"> Name:
        <input type="text" name="name" >
        <input type="submit" value="Submit">
    </form>
</body>
</html>"""

new_message = message.format(namesArray=namesArray)

@get('/')
def dashboard():
    return new_message

@post('/addName')
def addName():
    newName = request.forms.get('name')
    collection.insert({"name": newName})

    namesArray = []
    
    for name in collection.find():
        namesArray.append(name['name'])

    new_message = message.format(namesArray=namesArray)
    return new_message


run(host='localhost', port=3000)
