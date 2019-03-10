from bottle import route, run, post, get, request
from pymongo import MongoClient

MONGODB_URI = "mongodb://wework:wework1@ds163825.mlab.com:63825/wework"
client = MongoClient(MONGODB_URI, connectTimeoutMS=30000)
db = client.get_database("wework")
collection = db.names
namesArray = [] # holds all names from DB

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

# format {namesArray} with actual data from DB
new_message = message.format(namesArray=namesArray)

# GET on root. Gets all names from DB
@get('/')
def dashboard():
    return new_message

# POST on form submit. Reset previusly displayed names, enters another name to DB, and get all names from DB
@post('/addName')
def addName():
    newName = request.forms.get('name')
    collection.insert({"name": newName})

    namesArray = []

    for name in collection.find():
        namesArray.append(name['name'])

    new_message = message.format(namesArray=namesArray)
    return new_message

# run on localhost, port 3000
run(host='localhost', port=3000)
