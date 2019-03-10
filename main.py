from bottle import route, run, post, get, request

names = ['Roman', 'Ofir']
 
message = """<html>
<body>
    <div>
        <p>Names: {names}</p> 
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

new_message = message.format(names=names)

@get('/')
def dashboard():
    return new_message

@post('/addName')
def addName():
    newName = request.forms.get('name')
    names.append(newName)
    new_message = message.format(names=names)
    return new_message


run(host='localhost', port=3000)
