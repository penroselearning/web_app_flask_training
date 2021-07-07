from flask import Flask, render_template, request
import json, random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

# route variables

@app.route("/person_details/<prodID>")
def person_details(prodID):

    if prodID == "PRD111":
        return "<img src='https://www.theone.com/images/thumbs/0015439_tora-dining-table-180x93-clear_870.jpeg'>"
    elif prodID == "PRD123":
        return "<img src='https://cdn.ambientedirect.com/chameleon/mediapool/thumbs/0/47/Gubi_Beetle-Chair-mit-Stoff-und-Gestell-schwarz_1515x1515-ID572442-a40195c7e75264b6a6309e1e0ffa09f7.jpg'>"

# use variables in HTML

@app.route("/student/<name>")
def student(name):

    return render_template("greeting_for_student.html", name = name)

# building master template

@app.route("/about_us")
def about_us():

    return render_template("about_us.html")

@app.route("/subscriber")
def subscriber():

    return render_template("subscriber.html")

@app.route("/square", methods=["POST","GET"])
def square():
    if request.method == "GET":
        return render_template("squares.html")
    
    elif request.method == "POST":
        number = int(request.form['number'])

        square = number ** 2
        return render_template("squares.html", square=square)


@app.route("/pin_authentication", methods=["GET","POST"])
def pin_authentication():

    users = {
        1234 : ["John Doe", 2001],
        1002 : ["Eric Jerald", 2005],
        1011 : ["Rick Grimes", 2001],
        1221 : ["Carl Grimes", 2008]
    }

    if request.method == "GET":
        return render_template("pin_user_info.html")

    elif request.method == "POST":
        pin = int(request.form['pin'])

        if pin in users.keys():
            user = users[pin]

            return render_template("pin_user_info.html", user=user)
        else:
            return render_template("pin_user_info.html", error="user not found")

@app.route("/shopping_cart", methods=["POST", "GET"])
def shopping_cart():

    shopping_cart = {
        1234 : ["Apples", "Mangoes", "Bananas", "Stawberries", "Avacado"],
        5322 : ["Bananas", "Stawberries", "Avacado"],
        1002 : ["Apples", "Mangoes", "Avacado"]
    }

    if request.method == "GET":
        return render_template("pin_access_shopping_cart.html")

    elif request.method == "POST":
        pin = int(request.form['pin'])

        shopping_list = shopping_cart[pin]

        return render_template("shopping_cart.html", shopping_list=shopping_list)

@app.route("/user_shopping_cart", methods=["POST", "GET"])
def user_shopping_cart():

    if request.method == "GET":
        return render_template("shopping_cart.html")

    elif request.method == "POST": 
        
        item = request.form['item']
        add_remove = request.form['add_remove']

        if add_remove == "add":
            shopping_cart.append(item)
        elif add_remove == "remove":
            shopping_cart.remove(item)

        return render_template("shopping_cart.html", shopping_list=shopping_list)
        

@app.route("/lib_management", methods=["POST", "GET"])
def lib_management():

    with open("static/data/library.json", "r") as file:
        library = json.load(file)

    if request.method == "GET":
        return render_template("library_management_system.html", library=library)

    elif request.method == "POST":
        name_of_book = request.form['name_of_book']
        name_of_author = request.form['name_of_author']

        randomID = str(random.randint(1, 5000))

        library[randomID] = [name_of_book, name_of_author]

        with open("static/data/library.json", "w") as file:
            json.dump(library, file, indent=2)
        
        return render_template("library_management_system.html", library=library)

if __name__ == '__main__':
    app.run(debug=True)
