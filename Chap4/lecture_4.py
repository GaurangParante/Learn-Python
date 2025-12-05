# dict = {
#     "key":"value",
#     "name":"Gaurang",
#     "subjects":["Python","js","node"],
#     "topic":("dict","set"),
#     "age":35,
#     "is_adult":True,
#     "marks":98.2,

# }


# dict['name'] = "Bhavesh" #overwrite
# print(dict["name"])
# print(dict['age'])
# print(dict['is_adult'])
# dict["surname"] = "Parante"

# print(dict)
# print(type(dict))/

# student = {
#     "name":"Gaurang",
#     "marks":{
#         "maths":98,
#         "english":35,
#         "science":86
#     }
# }

# print(student)
# print(student['marks'])
# print(student["marks"]["maths"])
# print(student.keys())
# print(len(student))
# print(list(student.keys()))
# print(len(list(student.keys())))
# print(student.values())
# print(list(student.values()))

# print(student.items())
# pairs = list(student.items())
# print(pairs[0])

# print(student['name2']) # Will give error while no data found
# print(student.get('name2')) # Will not None when no data found

# add_dict = {"city":"Ahmedabad"}
# student.update(add_dict)
# print(student)

# collection = {1,2,3,4,"hello","world",2,8}

# print(collection)
# print(type(collection))
# print(len(collection)) # total number of unique items

# empty_set = {} # This is empty dictionary
# empty_set = set() # empty set; syntex
# print(type(empty_set))

# collection= set()
# collection.add(1)
# collection.add("Hello")
# collection.add((1,2,3))
# collection.add(2)
# collection.add([1,2,3]) # its gives error unhashable

# print(collection)
# collection.remove(1)
# print(len(collection))
# collection.clear()
# print(collection)

collection = {"hello","world","gaurang","bhavesh","python"}
print(collection.pop())
print(collection.pop())

