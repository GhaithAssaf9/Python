# import random
# def randInt(min = 0,max = 100):
#     if max<0:
#         print('need a number greater than 0')
#     elif min > max:
#         print('need a max greater than the min')
#     else: 
#         if max != 100 and min != 0:
#             return round(random.random()*(max-min)+min)
#         if min != 0:
#             return round(random.random()*(100-min)+min)
#         if max != 100:
#             return round(random.random()*max)
#     return round(random.random()*100)
# print(f"random number between 0 and 100 randInt() = {randInt()}")
# print(f"random number between 0 and 10 randInt(max = 10) = {randInt(max = 10)}")
# print(f"random number between 98 and 100, randInt(min = 98) = {randInt(min = 98)}")
# print(f"random number between 22 and 25 randInt(min = 22, max = 25) = {randInt(min = 22, max = 25)}")
# print(f"takes into account the edge case of min>max, randInt(min = 7, max = 2) {randInt(min = 7, max = 2)}")
# print(f"takes into account the edge case of 0<max, randInt(max = -5) {randInt(max = -5)}")



# x = [ [5,2,3], [10,8,9] ]
# x[1][0]=15
# print(f"x was [ [5,2,3], [10,8,9] ]  and now {x}")
# x2 = [[7,8,99,10], [0,2,-6,10,10]]
# for val in x2:
#     for i in range(len(val)):
#         if 10 == val[i]:
#             savedIndex = i
#             val[savedIndex] = 15
# print(f"x2 was [ [7,8,99,10],[0,2,-6,10,10] ] and now {x2}")



# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# students[0]['last_name'] = 'Bryant'
# print("student 1's information was {'first_name':  'Michael', 'last_name' : 'Jordan'}")
# print("student 1's new information is {student[0]}")


# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }



# sports_directory['soccer'][0] = 'Andres'
# print("sports_directory key code 'soccer' used to say ['Messi', 'Ronaldo', 'Rooney'] ")
# print('now has changed to')
# for i in range(len(sports_directory['soccer'])):
#     print(f"{sports_directory['soccer'][i]} and ")
# sports_directory2 = {
#     'american_football' : ['Peyton', 'Eli'],
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# for i in range(len(sports_directory2['soccer'])):
#     if 'Messi' in sports_directory2['soccer']:
#         sports_directory2['soccer'][i] = 'Andres'
# print("my new sports_directory2 changed from 'soccer' : ['Messi', 'Ronaldo', 'Rooney']  to")
# for i in range(len(sports_directory2['soccer'])):
#     print(f"{sports_directory2['soccer'][i]} and ")


# z = [{'x': 10, 'y': 20}] 
# z[0]['y'] = 30
# print("z used to look like [{'x': 10, 'y': 20}] now {z}")


# students2 = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'},
#     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#     {'first_name' : 'KB', 'last_name' : 'Tonel'}]


# def iterateDictionarycopy(anyList):
#     stringReturn = ''
#     for val in anyList:
#         stringReturn += f"first_name - {val['first_name']}, last_name - {val['last_name']}\n"
#     return stringReturn
# print(iterateDictionarycopy(students2))



# def iterateDictionary2(key_name, some_list):
#     stringReturn = ''
#     for val in some_list:
#         stringReturn += f"{val[key_name]} \n"
#     return stringReturn
# print(iterateDictionary2('last_name',students2))



# dojo = {
#    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }


# def printDictonaryInfo(my_dictonary):
#     # outputStr = ''
#     for key in my_dictonary:
#         print(f"{len(my_dictonary[key])} {key.upper()}")
#         for val in my_dictonary[key]:
#             print(val)
#         print("")
# printDictonaryInfo(dojo)