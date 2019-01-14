f = open("ca.txt","r")
naam = open("new.txt","w")
a = ""
b = f.readline()
while(b):
    try:
        p = b.split("(")[0]
        p = p.strip(" ")
        naam.write(p)
        naam.write(",")
        naam.write("\n")
        a += '"'+p+'"'+','
    except:
        pass
    b = f.readline()
f.close()
print a
