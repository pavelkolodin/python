
a = ["ru", "en", "ge"]

for i in range(0, 10):
    s = "zuzu" + str(i)
    a.append(s)


print(len(a))
print(a)

longstring = ""

for s in a:
    print("STRING: " + s)
    longstring += s

print(longstring)

