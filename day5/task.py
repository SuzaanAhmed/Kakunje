import random
"""
TUPLE QUESTIONS

t1 = (10,20,"Python","Code")
t2=("A","B")
1. Access and print the first element of t1.
2. Access and print the last element of t2.
3. Convert t1 into a list, change "Code" to "Program", and convert it back into a tuple.
4. Unpack all elements of t1 into separate variables and print them.
5. Join t1 and t2 and store the result in a new tuple.
6. Access elements from index 1 to 3 of the joined tuple.
t1=(1,2,3)
7. Multiply the tuple t1 by 3 and print the result.
"""
t1 = (10,20,"Python","Code")
t2=("A","B")

xlist=[
    t1.__getitem__(0),
    t2.__getitem__(-1),
    (ylist := list(t1), ylist.__setitem__(3, "Program"), tuple(ylist))[2],
    [f"{a}|{b}|{c}|{d}" for a,b,c,d in [t1]][0],
    t3:= (t1+t2),
    t3[1:4],
    t1*3
]

for i,x in enumerate(xlist):
    print(f"{i+1}). {x}")

print("======================================================")
#############################################################
"""
SET QUESTIONS
mySet={10,20,30,40}
1. Print the given set.
2. Check whether 20 is present in my_set.
3. Find and print the length of my_set.
4. Add 50 to my_set.
5. Remove 30 from my_set.
6. Remove an element using discard() and note the output.
7. Remove a random element from my_set.
8. Loop through my_set and print each element.
9. Clear all elements from my_set.
"""

mySet={10,20,30,40}
xlist=[
    mySet.copy(),
    f"{'Yes, 20 is present in mySet.' if mySet.__contains__(20) else 'No, 20 is not present in mySet.'}",
    mySet.__len__(),
    (mySet.add(50), mySet.copy())[1],
    (mySet.remove(30),mySet.copy())[1],
    (mySet.discard(50), mySet.copy())[1],
    (mySet.remove(random.choice(list(mySet))), mySet.copy())[1],
    [f"{i}" for i in mySet],
    mySet.clear() or mySet.copy(),        
]

for i, x in enumerate(xlist):
    print(f"{i+1}). {x}")

print("======================================================")
#############################################################

"""
set1={1,2,3}
set2={3,4,5,6}
1. Print the elements that are in set1 but not in set2.
2. Print the elements that are in either set1 or set2 but not in both (symmetric difference).
3. Add all items from set2 into set1 and print the updated set1.
4. Print all unique elements from both set1 and set2.
5. Add 7 to set1 and print the set.
"""

set1={1,2,3}
set2={3,4,5,6}

xlist=[
    (set1 - set2),
    (set1 ^ set2),
    (set1.update(set2), set1.copy())[1],
    (set1 | set2),
    set1.add(7) or set1.copy()
]

for i,x in enumerate(xlist):
    print(f"{i+1}). {x}")

print("======================================================")
#############################################################

"""
DICTIONARY QUESTIONS
student{
    "name":"Anu",
    "age":20,
    "course":"Python"
}

1. Print all keys, values, and all items in the dictionary.
2. Access the value of "name".
3. Access the value of "course" using get().
4. Add a new key "marks" with value 85.
5. Update the value of "age" to 21.
6. Remove "course" using pop().
7. Remove the last inserted item using popitem().
8. Loop through the dictionary and print keys and values.
"""

student={
    "name":"Anu",
    "age":20,
    "course":"Python"
}
xlist=[
    (list(student.keys()),list(student.values()),list(student.items())),
    student["name"],
    student.get("course"),
    (student.update({"marks":85}), student.copy())[1],
    (student.update({"age":21}), student.copy())[1],
    (student.pop("course"), student.copy())[1],
    (student.popitem(), student.copy())[1],
    [f"{k}: {v}" for k,v in student.items()]
]

for i,x in enumerate(xlist):
    print(f"{i+1}). {x}")
print("======================================================")
#############################################################

"""
students{
    "student1":{
        "name":"Anu",
        "age":20
        
    },
    "student2":{
        "name":"Ravi",
        "age":21
    }
}
    }
1. Print the complete nested dictionary.
2. Create a copy of the students dictionary.
"""

students={
    "student1":{
        "name":"Anu",
        "age":20
        
    },
    "student2":{
        "name":"Ravi",
        "age":21
    }
}
xlist=[
    f"{students}",
    students.copy()
]

for i,x in enumerate(xlist):
    print(f"{i+1}). {x}")

print("======================================================")
#############################################################

"""
employee={
    "emp_id":101,
    "name":"Kiran",
    "department":"HR",
    "salary":35000
    }
1. Display all keys in the employee dictionary.
2. Display all values in the employee dictionary.
3. Display all key-value pairs (items) from the dictionary.
4. Access and print the value of "name".
5. Update the "salary" to 40000.
"""

employee={
    "emp_id":101,
    "name":"Kiran",
    "department":"HR",
    "salary":35000
    }

xlist=[
    list(employee.keys()),
    list(employee.values()),
    list(employee.items()),
    employee["name"],
    (employee.update({"salary":40000}), employee.copy())[1]
]

for i,x in enumerate(xlist):
    print(f"{i+1}). {x}")