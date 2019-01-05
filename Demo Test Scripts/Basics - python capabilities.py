
#this is how you write a comment

print("Hello World")

y = "hello "
x = "world"

print(y + x)


x = 5
y = 10

print(y + x)


if 10 > 5:
    print("10 is greater than 5")


def summation(a, b):
    print(a+b)
    print("this sum was printed from a function")


summation(x,y)

x = 5
y = 2.5
z = 4j

print()
print()
print("X is type " + str(type(x)) + "and has a value of " + str(x))
print("y is type " + str(type(y)))
print("z is type " + str(type(z)))


#casting
x = int(2)
y = int(2.5)
z = float(1)
p = str(10)


print()
print()
print(x)
print(y)
print(z)
print(p)



print("what is your name?\n\n")

#x = input()
x = "Slim Shady"
print("Hello " + x)


for y in x:
    print(y)



x = 5

if x > 8:
    print("x is greater in 8")
else:
    print("x is not greater than 8")



y = ["apple", "orange", "grapes"]

for x in y:
    print(x)
else:
    print("no more fruits")





i = 0
sum = 0
num = 10

while i < num:
    sum+=i
    print(sum)
    i = i + 1


def printHi(name="John"):
    print("Hi " + name)


printHi("Eric")
printHi()

def returnSum(a, b):
    """This is a description of the function"""
    return(a+b)




class MyClass:
    name = "Raghav"

    def __init__(self, name = "Eric A Garthoffner", age = 36):
        self.name = name
        self.age = age

    def sum(self, a, b):
        print(a + b)

x = MyClass("John", 40)
print(x.name)
print(x.age)
x.sum(x.age,5)



y = MyClass()
print("y's name is " + y.name)
print(y.age)
y.sum(y.age,5)


#Collections

#Lists [] (ordered | indexed | changeable | duplicates
my_list = ["Tokyo", "New York", "Los Angeles", "San Diego"]
print(my_list)

for val in my_list:
    print(val)

my_list[3] = "Long Beach"
my_list.append("Boston")
my_list.remove("Tokyo")
my_list.append("foo")
my_list.append("bar")
my_list.pop()

print(my_list)

my_list.reverse()

print(my_list)

my_list.clear()


print(my_list)

my_list = ["foo", [1, 2, 3], ['a', 'b', 'c']]

print(my_list)



#Tuple () (ordered | indexed | unchangeable | duplicates
my_tuple = ("Apples", "oranges", "banana")
print(my_tuple)
print(my_tuple[-1])

for val in my_tuple:
    print(val)

print("Apples" in my_tuple)
print("Cherry" in my_tuple)




#Set {} (unordered | unindexed | no duplicates
my_set = {"Chalk", "Duster", "Board"}
print(my_set)

for x in my_set:
    print(x)

print("Chalk" in my_set)

my_set.add("pen")
my_set.update('eraser', 'pencil', "stuff")
print(my_set)

for x in my_set:
    print(x)


# UNION / INTERSECTION / DIFF / SYMMETRIC DIFF

A = {"A", 'B', 1, 2,3}
B = {"B", 'C', 3, 4,5}

print(A.union(B))
print(A | B)

print(A.intersection(B))
print(A&B)

print(A.difference(B))
print(A - B)

print(B.difference(A))
print(B - A)

print(A.symmetric_difference(B))
print(B.symmetric_difference(A))
print(A ^ B)







#Dictionary {K:V} (unordered | indexed | changeable | no duplicates

my_dict = {

    "class" : "animal",
    "name"  : "giraffe",
    "age"   : 10
}

print(my_dict)
print(my_dict["name"])
print(my_dict.get("name"))
print(my_dict.values())

for x in my_dict:
    print(my_dict[x])

my_dict["color"] = "grey"
print(my_dict)



