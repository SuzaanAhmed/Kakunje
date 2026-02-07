A=("mango","bannana","grapes")

print(f"{A}")
print((A:=list(A),A.append("kiwi"),A.sort(),tuple(A))[3])


student1={
    "name":"Suzaan",
    "age":22,
}

student1.update({"university":"SCEM"})
print(list(student1.values()))
###########################################

mySet1={1,2,3,4,5}
mySet2={3,4,5,6,7}
print(mySet1.intersection(mySet2))

MatA=[
    [1,2],
    [3,4]
    ]
print((MatA.insert(1,[5,6]),MatA)[1])


print("Hello world.\nHow are you?\nMy name is Suzaan.\nWhat is your name?")

MatB=[
    [1, 2],
    [5, 6], 
    [3, 4]
    ]

stringA="hello world"
print(stringA[4:0:-1])

listA=[1,2,3,4]
print({x for x in listA})
print(listA[1::2])

employee={
    "name":"Suzaan",
    "age":22
}

print(employee)

listB=[1,2,3,4,5]
print((listB.insert(2,0),listB)[1])
print((listB.remove(1),listB)[1])
print((listB.sort(reverse=True),listB)[1])
tupleA=(1,2,3,4,5)
print(tupleA)
#delete 2 from tupleA
print((temp:=list(tupleA),temp.remove(2),tupleA:=tuple(temp))[2])
print(tupleA.__add__(("call","of","duty")))

student2={
    "name":"Suzaan",
    "age":22,
    "course":"Python",
    "marks":85,
    "university":"SCEM"
}
print((student2.update({"marks":93}), (student2.copy()))[1])