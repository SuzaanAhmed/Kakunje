'''
Task1: 
Here I have take name, age and height as input and printed it out.
'''
print("TASK1")

name=input("Enter name: ")
age=int(input("Enter age: "))
feet,inch=map(int,input("Enter height(feet,inch): ").split(','))
print(f"My name is {name}, I am {age} years of age and am {feet}ft {inch}inches tall.")

print("\n########################################################################################\n")
########################################################################################
'''
Task2 and Task3:
Here I have taken three numeric integer inputs for a,b,c.
Then I have taken sum inside parenthesis and printed it.
'''
print("TASK2 and TASK3")

a,b,c=5,10,15
sum=(
    a+
    b+
    c
)
print(f"Sum of {a} + {b} + {c} = {sum}")

print("\n########################################################################################\n")
########################################################################################

'''Task4'''
print("TASK4")

sentence=(
    "This is task 4. "
    "Here I have created 'sentence' variable. "
    "I have demonstrated implicit continuation inside parenthesis."
)
print(sentence)

print("\n########################################################################################\n")
########################################################################################
'''
Task5:
Here I have made a list of games and printed it.
'''
print("TASK5")

games=[
    "Sea Of Thieves",
    "Sifu",
    "Ghost Of Tsushima",
    "Dishonored 1&2",
    "Witcher 3",
    "Hitman: WOA",
    "Elden Ring",
    "Sekiro: Shadow Die Twice"
]
print(f"Below is a list of games I played:\n{games}")

print("\n########################################################################################\n")
########################################################################################
'''
Task6:
Below I have taken user input for name and greeted the said user.
'''
print("TASK6")

name=input("Enter name: ")
print(f"Greeting {name}, how are you doing?")

print("\n########################################################################################\n")
########################################################################################

'''
Task7: 
Here I have taken input into 'x' and 'y' variables and printed sum, difference and product.
'''
print("TASK7")

x,y=map(int,input("Enter two numbers(x,y): ").split(','))
print(
    f"{x} + {y} = {x+y}\n"
    f"{x} - {y} = {x-y}\n"
    f"{x} * {y} = {x*y}\n"
    )

print("\n########################################################################################\n")
########################################################################################
'''
Task8:
I have taken two values through 'input' and printed their datatype and sum.
'''
print("TASK8")

val1,val2=input("Enter two values(val1,val2): ").split(',')
print(f"Datatype of {val1} : {type(val1)}\nDatatype of {val2} : {type(val2)}")
val1,val2=int(val1),int(val2)
print(f"Sum of {val1} and {val2} is {val1+val2}")