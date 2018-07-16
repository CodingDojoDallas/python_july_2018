# class Zoo:
#     def __init__(self, zoo_name):
#         self.animals = []
#         self.name = zoo_name
#     def addDog(self, name):
#         self.animals.append( Dog(name) )
#     def addDragon(self, name):
#         self.animals.append( Dragon(name) )
#     def printAllHealth(self):
#         print("-"*30, self.name, "-"*30)
#         for animal in self.animals:
#             animal.displayHealth()
# zoo1 = Zoo("John's Zoo")
# zoo1.addDog("Tracy")
# zoo1.addDog("Doggy")
# zoo1.addDragon("Draggy")
# zoo1.addDragon("Dragoon")
# zoo1.printAllHealth()


# class Card:
#     def __init__(self, value, type):
#         self.value = value
#         self.type = type
#     def show(self):
#         print("Value: ", self.value, "Type: ", self.type)
# class Deck:
#     def __init__(self, name):
#         self.deck = []
#         self.name = name
#         for i in ["clubs", "diamonds", "hearts", "spades"]:
#             for j in range(1,15):
#                 self.deck.append( Card(j, i ) )
#     def show(self):
#         print("\n", "*"*30, self.name, "*"*30)
#         for cheese in self.deck:
#             cheese.show()
# d1 = Deck("First Deck")
# d1.show()
# d2 = Deck("Second Deck")
# d2.show()

# def varargs(arg1, *args):
#     print("Got "+arg1+" and "+ ", ".join(args))
# varargs("one") # output: "Got one and "
# varargs("one", "two") # output: "Got one and two"
# varargs("one", "two", "three") # output: "Got one and two, three"

# # In this example, the first argument is assigned to the first method parameter as usual. 
# # However, the next parameter is prefixed with an asterisk (the splat operator we just introduced), 
# # which bundles the remaining arguments into a new tuple, which is then assigned to that parameter.

# # If we tested the type of args inside our function using type(args) we would get:

# def varargs(arg1, *args):
#     print("args is of " + str(type(args)))
# varargs("one", "two", "three") # output: args is of <class 'tuple'>

# # Note the .join() method in the first code snippet is called on a string that glues the values in the tuple together. 
# # For example, the tuple of arguments ('two', 'three') was joined as 'two, three' when we called ", ".join(args).



from flask import Flask, render_template, redirect, request

app = Flask(__nam__)

@app.route('/')
def green():
    return "I am in green"
    
@app.route('/blue', method='post',/<color>)
# post requests are alot of times for form data
# <color> is for the user to input a color, we just don't know what they'll type, so we use <>
def display_color(color): #color here is from the html/user input
    return render_template('index.html', colorname=color) #assinging <color> from user to colorname
    
    # return redirect('/')  #this redirects to whereever you need it to, in this case, back to localhost homepage ('/')

@app.route('new/<variable>')

@app.route('/life')
def purple():
    return render_template('index.html')

{% for i in range(e)%} #these 3 lines' syntax is to type in python code in HTML
<p>{{Cheese}}</p>
{% endfor %}

<form action="/process" method="post"> #these 4 lines=syntax for forms in HTML code (form)
    contact Name<input type="text" name="name">
    <input type="submit" value=submit">
</form>


@app.route('/process', methods=["post"])
def form_data():
    name = request.form['contactname']
    # contactname is the key and its value is what the user input in the form above
    return render_template('welcome.html', n = name, num = number) #need to create a welcome.html file that will
                                                                   #output n and num

