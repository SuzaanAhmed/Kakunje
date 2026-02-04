"""
xlist=["apple", "banana", "cherry"]
1. ["apple", "banana", "cherry", "orange"]
2. ["apple", "mango", "banana", "cherry", "orange"]
3. ["apple", "mango", "banana", "cherry", "orange", "kiwi", "grape"]
"""
mainList=["apple", "banana", "cherry"]
print(f"The main list is: {mainList}")
xlist=[(mainList.append("orange"),mainList.copy()), 
       (mainList.insert(1,"mango"),mainList.copy()), 
       (mainList.extend(["kiwi","grape"]),mainList.copy())]

for i,x in enumerate(xlist):
    print(f"{i+1}. {x[1]}")

print("=================================================================================")
#########################################################################################
"""
[10,20,30,40,50]
1. [10,20,300,40,50]
2. [10,200,3000,400,50]
"""
mainList=[10,20,30,40,50]
print(f"The main list is: {mainList}")
xlist=[(mainList.__setitem__(2,300),mainList.copy())[1],
       (mainList.__setitem__(2,3000),mainList.__setitem__(1,200),mainList.__setitem__(3,400),mainList.copy())[3]]

for i,x in enumerate(xlist):
    print(f"{i+1}. {x}")

print("=================================================================================")
#########################################################################################
"""
[1,2,3]
1. [1,100,2,3]
2. [1,100,2,999]
"""
mainList=[1,2,3]
print(f"The main list is: {mainList}")
xlist=[(mainList.insert(1,100),mainList.copy()), 
       (mainList.extend([999]),mainList.copy())]

for i,x in enumerate(xlist):
    print(f"{i+1}. {x[1]}")

print("=================================================================================")
#########################################################################################
"""
[10,20,30,40,50]
1. [10,20,30,40,50,60]
2. [5,10,20,30,40,50,60]
3. [5,10,20,30,40,50,60,70,80,90]
""" 
mainList=[10,20,30,40,50]
print(f"The main list is: {mainList}")
xlist=[(mainList.append(60),mainList.copy()), 
       (mainList.insert(0,5),mainList.copy()),
       (mainList.extend([70,80,90]),mainList.copy())]

for i,x in enumerate(xlist):
    print(f"{i+1}. {x[1]}")

print("=================================================================================")
#########################################################################################
"""

[42,3.14,"Hello",True]
1. [2.718,3.14,"Hello",True]
2. [2.718,3.14,"Hello",True,1000]
3. [2.718,False,3.14,"Hello",True,1000]
4. [5,3.14,"Hello",True,1000]
"""
mainList=[42,3.14,"Hello",True]
print(f"The main list is: {mainList}")
xlist=[(mainList.__setitem__(0,2.718),mainList.copy()), 
       (mainList.append(1000),mainList.copy()), 
       (mainList.insert(1,False),mainList.copy()),
       (mainList.__setitem__(0,5),mainList.pop(1),mainList.copy())[1:]]

for i,x in enumerate(xlist):
    print(f"{i+1}. {x[1]}")

print("=================================================================================")
#########################################################################################
"""
["Cat", "Dog", "Lion", "Tiger", "Rabbit", "Monkey"]
1) ["lion"]
2) ["Monkey", "Rabbit"]
3) ["Tiger", "Lion", "Dog"]
4) ["Cat", "Tiger"]
5) ["Tiger", "Cat"]
6) ["Monkey", "Lion"]
7) ["Rabbit", "Lion", "Cat"]
8) ["Monkey", "Rabbit", "Tiger", "Lion", "Dog", "Cat"]
"""
mainList=["Cat", "Dog", "Lion", "Tiger", "Rabbit", "Monkey"]
print(f"The main list is: {mainList}")
copy_mainList=mainList.copy()
xlist=[(mainList.clear(),mainList.append(copy_mainList[2].lower()),mainList.copy())[1:], 
       (mainList.clear(),mainList.extend(copy_mainList[:-3:-1]),mainList.copy())[1:],  
       (mainList.clear(),mainList.extend(copy_mainList[-3:0:-1]),mainList.copy())[1:], 
       (mainList.clear(),mainList.extend(copy_mainList[:-2:3]),mainList.copy())[1:], 
       (mainList.reverse(),mainList.copy()), 
       (mainList.clear(),mainList.extend(copy_mainList[::-3]),mainList.copy())[1:],  
       (mainList.__setitem__(0,copy_mainList[-2]),mainList.extend([copy_mainList[0]]),mainList.copy())[1:], 
       (copy_mainList.reverse(),copy_mainList.copy())
       ] 

for i,x in enumerate(xlist):
    print(f"{i+1}. {x[1]}")

print("=================================================================================")
#########################################################################################
"""
l1=[50, "apple", True, "car", 40.5]
1. Find the length of l1.
2. Replace 'True' with 'False'.
3. [50, "Kiwi", "Boat", 20, "car", 40.5]
4. [5000, "Kiwi", "Boat", 20, "car", 40.5]
5. ["Kiwi", "Boat", 20, "car", 40.5] (remove)
6. ["Kiwi", 20, "car", 40.5] (pop)
7. ["Kiwi", 20, "car"] (del)
8. ["Kiwi", 20, "car", 100]
9. ["Banana", "Kiwi", 20, "car", 100]
10. ["Banana", "Kiwi", 20, 30.5, "car", 100]
11. [] (Empty list)
"""
l1 = [50, "apple", True, "car", 40.5]
print(f"The main list is: {l1}")
xlist = [
    (None,len(l1)),
    (l1.__setitem__(2, False), l1.copy()),
    (l1.__setitem__(slice(1, 3), ["Kiwi", "Boat", 20]), l1.copy()),
    (l1.__setitem__(0, 5000), l1.copy()),
    (l1.remove(5000), l1.copy()),
    (l1.pop(1), l1.copy()),
    (l1.__delitem__(-1), l1.copy()),
    (l1.append(100), l1.copy()),
    (l1.insert(0, "Banana"), l1.copy()),
    (l1.insert(3, 30.5), l1.copy()),
    (l1.clear(), l1.copy())
]

for i, x in enumerate(xlist):
    print(f"{i+1}. {x[1]}")    
print("=================================================================================")
#########################################################################################
"""
l2 = [50, -1, 2, 100, -6, -3, 67, 79, -55]
1. Reverse
2. Ascending
3. Descending
"""

l1=[50, -1, 2, 100, -6, -3, 67, 79, -55]
print(f"The main list is: {l1}")
xlist=[
    (l1.reverse(),l1.copy()),
    (l1.sort(),l1.copy()),
    (l1.sort(reverse=True),l1.copy())]

for i,x in enumerate(xlist):
    print(f"{i+1}. {x[1]}")
    
print("=================================================================================")
#########################################################################################