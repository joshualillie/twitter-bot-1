print("let's play")

x = 10

print("x is {}".format(x))

for y in range(x):
    print("count is {}".format(y))

print("-------------------------")
for y in range(10, (x+10), 2):
    print("count is {}".format(y))

print("-------------------------")
names = ["Matthew", "Mark", "Luke", "John"]
for name in names:
    print("The Gospel of {}".format(name))
