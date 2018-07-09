# Create beCheerful().  Within it, print string "good morning!" 98 times.

print("*"*80)
def beCheerful(name='', repeat=98):
	print(f"good morning {name}\n"*repeat)

beCheerful()
beCheerful(name="john")
beCheerful(name="michael", repeat=5)
beCheerful(repeat=5, name="kb")
beCheerful(name="aa")

# Create a function radInt() where:
    # randInt() returns a random integer between 0 to 100
    # randInt(max=50) returns a random integer between 0 to 50
    # randInt(min=50) returns a random integer between 50 to 100
    # randInt(min=50, max=500) returns a random integer between 50 and 500

def randInt(min=0, max=100):
    import random
    print(min + int(random.random()*max))

randInt()
randInt(max=50)
randInt(min=50)
randInt(min=50, max=500)
