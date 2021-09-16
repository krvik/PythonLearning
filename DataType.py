# This is a sample Python script.
fname = "vikash"

print(fname)
print(fname)
print(fname)
#this is single line comment.
a = 2
b = 3.6j
c = a + b
print(type(c))
"""This is doc string"""
print(len(fname))
print(fname[3])
print(fname.upper())

mylist = ["mango", "patna", 123, True, 12.1]
print(mylist)
print(mylist[3])
print(type(mylist[4]))

#using append one can add value at end only.
mylist.append("12st")
print(mylist)

#using insert one can add value in middle also.
mylist.insert(2, "apple")
print(mylist)

#dictionary data type
marks = {'maths':90,
         'science': 67,
         'ssc': 89,
         'hindi': 98}
print(marks)
#Accessing the value of dictionary
print(marks['science'])

#modifying value of key in dictionary
marks['science'] = 88
print(marks)
#adding key:value in dictionary
marks['english'] = 59
print(marks)


#Tuples data type: ordered and unchangable, and can have duplicate value
HomeTown = ("Delhi","patna", "Gaya", "patna", 123)
print(HomeTown)
print(HomeTown[4])
print(HomeTown.count('patna'))

#Set: unordered and no-duplicate entry. Does not have indexing
mySet = {'tiger', 'monkey', 24, 43, 24, 4.5, True}
print(mySet)

#Range Data type
R1 = list(range(10))
print(R1)

#TypeConversion
dob = 1996
name = 'vikash'
username = name + str(dob)
print(username)

