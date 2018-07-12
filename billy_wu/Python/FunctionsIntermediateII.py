# ###Part 1####

# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# How would you change the value 10 in x to 15?  Once you're done x should then be [ [5,2,3], [15,8,9] ].  

# x[1][0]=15
# print(x)

# How would you change the last_name of the first student from 'Jordan' to "Bryant"?

# students[0]['last_name']="Bryant"
# print(students)

# For the sports_directory, how would you change 'Messi' to 'Andres'?

# sports_directory['soccer'][0]='Andres'
# print(sports_directory)

# For z, how would you change the value 20 to 30?

# z[0]['y']=30
# print(z)



# ###Problem 2####
# Create a function that given a list of dictionaries, it loops through each dictionary in the list and prints each key and the associated value

# def iterateDictionary(dictionary):
#     for i in range(0,len(dictionary)):
#         print('first_name', dictionary[i]['first_name'] + ', ' + 'last_name', dictionary[i]['last_name'])
#     # for k,v in range(0,len(dictionary)):
#     #     print(dictionary[[k])

# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
# iterateDictionary(students)




####PrOblem 3####   
# Create a function that given a list of dictionaries and a key name, it outputs the value stored in that key for each dictionary.

# def iterateDictionary2(first_name, students):
#     for i in range(0,len(students)):
#         print(students[i][first_name])

# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
# iterateDictionary2('first_name', students)



####Problem 4#####
# Create a function that prints the name of each location and also how many locations the Dojo currently has.  Have the function also print the name of each instructor and how many instructors the Dojo currently has

# def dojostats(dojo):
#     print(len(dojo['location']), "LOCATIONS")
#     for i in range(0,len(dojo['location'])):
#         print(dojo['location'][i])
#     print(len(dojo['instructors']), "INSTRUCTORS")
#     for i in range(0,len(dojo['instructors'])):
#         print(dojo['instructors'][i])
# dojo = {
#    'location': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }
# dojostats(dojo)

