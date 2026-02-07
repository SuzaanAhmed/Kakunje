A=("mango","bannana","grapes")

print(f"{A}")
print((A:=list(A),A.append("kiwi"),A.sort(),tuple(A))[3])


student1={
    "name":"Suzaan",
    "age":22,
}

student1.update({"university":"SCEM"})
print(list(student1.values()))


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

s = "python"
print(s[::-1].upper())

L = [10, 20, 30, 40, 50]
print([L[0], L[-1]])

print({x**2 for x in range(1, 6)})
mat_rot = [[1, 2], [3, 4]]
print([list(row) for row in zip(*mat_rot[::-1])])

st_upd = {"name": "Suzaan", "age": 22}
print((st_upd.update({"age": st_upd["age"] + 1, "status": "graduated"}), st_upd)[1])

user = {"info": {"loc": {"city": "Bengaluru", "pin": 560001}}}
print((user["info"]["loc"].update({"city": "Mangaluru"}), user)[1])

mix_t = (10, "Python", 20, "SCEM", 30)
print(sum([x for x in mix_t if isinstance(x, int)]))

print([[1 if i == j else 0 for j in range(3)] for i in range(3)])

words = ["kiwi", "mango", "banana", "apple"]
print((words.sort(key=len), words)[1])

k = ["id", "name", "USN"]
v = [1, "Suzaan", "4SF22CI002"]
print(dict(zip(k, v)))
d = {"id": 1}
print((d.update({"status": "active", "zone": A}), d)[1])

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([row[1] for row in M])

T = (1, 5, 10)
print(10 in T)

Mat = [[1, 2], [3, 4]]
print([val for row in Mat for val in row])

sA, sB = {1, 2, 3}, {3, 4, 5}
print(sA - sB)

L2 = [1, 2, 3]
print((L2.__setitem__(1, 99), L2)[1])

print("Suzaan".swapcase())

emp = {"name": "Suzaan", "role": "Intern"}
print(list(emp.keys()))

t1, t2 = (1, 2), (1, 3)
print((t1 + t2).count(1))

L3 = [50]
print((L3.insert(0, 0), L3.append(100), L3)[2])

M2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([row[:2] for row in M2[:2]])

myS = {1, 2}
print((myS.update({3, 4}), myS.copy())[1])

d2 = {"a": 1, "b": 2, "c": 3}
print((d2.pop("b"), d2)[1])

print("Python".startswith("Py"))

print([x for x in range(11) if x % 2 == 0])

raw_L = [1, 2, 2, 3, 1, 4]
print((seen := set(), [x for x in raw_L if not (x in seen or seen.add(x))])[1])

msg = "Internship2026_Day06"
print("".join([char for char in msg if char.isdigit()]))

s_a, s_b = {1, 2, 3}, {3, 4, 5}
print(s_a.symmetric_difference(s_b))


M3 = [[10, 20], [30, 40]]
print([M3[i][1-i] for i in range(2)])

d3 = {"temp": "data"}
print((d3.clear(), d3)[1])