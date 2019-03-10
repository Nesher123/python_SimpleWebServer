from bottle import route, run
import webbrowser

names = ['Roman', 'Ofir']
 
f = open('index.html','w')
 
message = """<html>
<body>
    <div>
        <p>Names: {names}</p> 
        </br>
        </br>
        </br>
    </div>

    <form method="POST" action="http://localhost:3000/addName"> Name:
        <input type="text" name="name" value="">
        <input type="submit" value="Submit">
    </form>
</body>
</html>"""

new_message = message.format(names=names)

# f.write(new_message)
f.close()

@route('/')
def dashboard():
    return new_message

@route('/addName')
def add():
    names.append('a')

run(host='localhost', port=3000)

# #Change path to reflect file location
# filename = 'index.html'
# webbrowser.open_new_tab(filename)