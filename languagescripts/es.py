f = open("it.txt","r")
naam = open("new.txt","w")
a = ""
b = f.readline()
while(b):
    g = b.split(" ")[1]
    p = g.strip("\n")
    naam.write(p)
    naam.write(",")
    naam.write("\n")
    a += '"'+p+'"'+','
    b = f.readline()
f.close()
print a
