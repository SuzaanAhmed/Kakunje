"""
String Slicing:
"ABCDEFGHIJKL"
1) CEGI
2) KJIHGFED
3) KJIHGFEDCB
4) KIGE
5) AEI
"""
s="ABCDEFGHIJKL"
sliced=[
    s[2:-2:2],
    s[-2:2:-1],
    s[-2:0:-1],
    s[-2:3:-2],
    s[::4]
]
for i,slice in enumerate(sliced):
    print(f"{i+1}){slice}")
    
print("==========================================================================")
#######################################################
"""
"Python String Slicing Example"
1) gnirtS nohtyP
2) Slicing Example
3) emEni iS oy
4) Potgigae
5) elpmaxE
6) gtoP
"""
s="Python String Slicing Example"

sliced=[
    s[12::-1],
    s[14::],
    s[-1:5:-3]+" "+s[4:0:-3],
    s[0::4],
    s[-1:-8:-1],
    s[12::-4]
]

for i,slice in enumerate(sliced):
    print(f"{i+1}){slice}")

print("==========================================================================")
#######################################################
"""
String Slicing:
"Python is easy to learn"
1) easy
2) rae
3) es ola
4) si nohtyP
5) tnsa__a(_(space))
6) nhy
7) easy to learn
8) ot ysae
"""
s="Python is easy to learn"
sliced=[
    s[10:14],
    s[-2:-5:-1],
    s[10:-1:2],
    s[8::-1],
    s[2::3],
    s[5::-2],
    s[10::],
    s[16:9:-1]
]

for i,slice in enumerate(sliced):
    print(f"{i+1}){slice}")

print("==========================================================================")
#######################################################
"""
String Slicing:
"One of the world's spectacular bridge is Tower Bridge"
1) Tower Bridge
2) world's spectacular
3) egdirb
4) Ooho'aare_re(_(space))
5) rasleo
""" 
s="One of the world's spectacular bridge is Tower Bridge"
sliced=[
    s[-12::],
    s[11:30],
    s[-17:30:-1],
    s[::4],
    s[29::-5]
]

for i,slice in enumerate(sliced):
    print(f"{i+1}){slice}")

print("==========================================================================")
#######################################################
"""
String Slicing Task 3:
s = "DATASTRUCTURESANALYSIS"
1. Print the first and last character using index values.
2. Print the character at index 7.
3. Print the character at index -5.
4. Print characters from index 4 to 13.
5. Print the string without the first 4 characters.
6. Print every second character starting from index 0.
7. Print characters at even index positions only.
8. Print the entire string in reverse order.
9. Print characters from index 15 to index 5 in reverse.
10. Print the middle 6 characters using indexing.
"""
s = "DATASTRUCTURESANALYSIS"
sliced=[
    s[0]+s[-1],
    s[7],
    s[-5],
    s[4:13],
    s[4::],
    s[0::2],
    s[::2],
    s[-1::-1],
    s[15:5:-1],
    s[int((len(s)/2))-3:int((len(s)/2))+3]
]
for i,slice in enumerate(sliced):
    print(f"{i+1}){slice}")

print("==========================================================================")
#######################################################
"""
String Slicing Task 4:
Given: s = "LogicalThinking"
Write Python code to get the following outputs using string slicing only:
a) Thinking
b) gniknihTlacigoL
c) LglTiki
d) lacigo
e) giTk

Write Python code to:
Print the character at index -4
Print characters from index 2 to index 7
Print characters from index -8 to -1
Print the string except the first 3 characters
"""
s = "LogicalThinking"
sliced=[
    s[7::],
    s[::-1],
    s[:3:2]+s[6]+s[7:-2:2]+s[-3],
    s[6:0:-1],
    s[-1:-4:-2]+s[7:-3:4],
    s[-4],
    s[2:7],
    s[-8:-1],
    s[4::]
]
for i,slice in enumerate(sliced):
    print(f"{i+1}){slice}")

print("==========================================================================")
#######################################################