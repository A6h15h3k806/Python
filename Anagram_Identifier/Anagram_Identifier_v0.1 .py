word1 = input('''Type the first word or phase here!
''')

word2 = input('''Type the second word or phase here!
''')

word1 = word1.lower()
word2 = word2.lower()

a1 = word1.count("a") * 2
b1 = word1.count("b") * 3
c1 = word1.count("c") * 5
d1 = word1.count("d") * 7
e1 = word1.count("e") * 11
f1 = word1.count("f") * 13
g1 = word1.count("g") * 17
h1 = word1.count("h") * 19
i1 = word1.count("i") * 23
j1 = word1.count("j") * 29
k1 = word1.count("k") * 31
l1 = word1.count("l") * 37
m1 = word1.count("m") * 41
n1 = word1.count("n") * 43
o1 = word1.count("o") * 47
p1 = word1.count("p") * 53
q1 = word1.count("q") * 59
r1 = word1.count("r") * 61
s1 = word1.count("s") * 67
t1 = word1.count("t") * 71
u1 = word1.count("u") * 73
v1 = word1.count("v") * 79
w1 = word1.count("w") * 83
x1 = word1.count("x") * 89
y1 = word1.count("y") * 97
z1 = word1.count("z") * 101


a2 = word2.count("a") * 2
b2 = word2.count("b") * 3
c2 = word2.count("c") * 5
d2 = word2.count("d") * 7
e2 = word2.count("e") * 11
f2 = word2.count("f") * 13
g2 = word2.count("g") * 17
h2 = word2.count("h") * 19
i2 = word2.count("i") * 23
j2 = word2.count("j") * 29
k2 = word2.count("k") * 31
l2 = word2.count("l") * 37
m2 = word2.count("m") * 41
n2 = word2.count("n") * 43
o2 = word2.count("o") * 47
p2 = word2.count("p") * 53
q2 = word2.count("q") * 59
r2 = word2.count("r") * 61
s2 = word2.count("s") * 67
t2 = word2.count("t") * 71
u2 = word2.count("u") * 73
v2 = word2.count("v") * 79
w2 = word2.count("w") * 83
x2 = word2.count("x") * 89
y2 = word2.count("y") * 97
z2 = word2.count("z") * 101


list1 = [a1, b1, c1, d1, e1, f1, g1, h1, i1, j1, k1, l1, m1,
         n1, o1, p1, q1, r1, s1, t1, u1, v1, w1, x1, y1, z1,]

list2 = [a2, b2, c2, d2, e2, f2, g2, h2, i2, j2, k2, l2, m2,
         n2, o2, p2, q2, r2, s2, t2, u2, v2, w2, x2, y2, z2,]

try:
    for number in list1: list1.remove(0)

except ValueError: print("Zeros from list1 removed !")


try:
    for number in list2: list2.remove(0)

except ValueError: print("Zeros from list2 removed !")

list1.sort()
list2.sort()

if list1 == list2: print("Indeed the Words/Phases are Anagrams of each other !")
else: print("These are not the Anagrams of each other!")

Terminator = input("Press 'n' to terminate this module")

if Terminator == "n": print("Thank you and Good bye!!")


