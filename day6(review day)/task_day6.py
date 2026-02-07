A=("mango","bannana","grapes")

print(f"{A}")
print((A:=list(A),A.append("kiwi"),A.sort(),tuple(A))[3])


student={
    "name":"Suzaan",
    "age":22,
}

student.update({"university":"SCEM"})
print(list(student.values()))
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