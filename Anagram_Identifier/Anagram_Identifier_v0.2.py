word1 = input('''Type the first word or phase here!
''')

word2 = input('''Type the second word or phase here!
''')

word1 = word1.lower()
word2 = word2.lower()

a1 = word1.count("a") * 104479
b1 = word1.count("b") * 104491
c1 = word1.count("c") * 104513
d1 = word1.count("d") * 104527
e1 = word1.count("e") * 104537
f1 = word1.count("f") * 104543
g1 = word1.count("g") * 104549
h1 = word1.count("h") * 104551
i1 = word1.count("i") * 104561
j1 = word1.count("j") * 104579
k1 = word1.count("k") * 104593
l1 = word1.count("l") * 104597
m1 = word1.count("m") * 104623
n1 = word1.count("n") * 104639
o1 = word1.count("o") * 104651
p1 = word1.count("p") * 104659
q1 = word1.count("q") * 104677
r1 = word1.count("r") * 104681
s1 = word1.count("s") * 104683
t1 = word1.count("t") * 104693
u1 = word1.count("u") * 104701
v1 = word1.count("v") * 104707
w1 = word1.count("w") * 104711
x1 = word1.count("x") * 104717
y1 = word1.count("y") * 104723
z1 = word1.count("z") * 104729



a2 = word2.count("a") * 104479
b2 = word2.count("b") * 104491
c2 = word2.count("c") * 104513
d2 = word2.count("d") * 104527
e2 = word2.count("e") * 104537
f2 = word2.count("f") * 104543
g2 = word2.count("g") * 104549
h2 = word2.count("h") * 104551
i2 = word2.count("i") * 104561
j2 = word2.count("j") * 104579
k2 = word2.count("k") * 104593
l2 = word2.count("l") * 104597
m2 = word2.count("m") * 104623
n2 = word2.count("n") * 104639
o2 = word2.count("o") * 104651
p2 = word2.count("p") * 104659
q2 = word2.count("q") * 104677
r2 = word2.count("r") * 104681
s2 = word2.count("s") * 104683
t2 = word2.count("t") * 104693
u2 = word2.count("u") * 104701
v2 = word2.count("v") * 104707
w2 = word2.count("w") * 104711
x2 = word2.count("x") * 104717
y2 = word2.count("y") * 104723
z2 = word2.count("z") * 104729


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


