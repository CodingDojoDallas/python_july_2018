def randInt(min=0,max=100):
    import random
    # rndm=int(random.random()*max)
    # while rndm < min:
    #     rndm=int(random.random()*max)
    rndm=int(random.random()*(max-min)+min)
    return rndm
print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50,max=500))
print(dir(random))