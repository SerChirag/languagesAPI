f = open("hi.txt","r")
naam = open("new.txt","w")
a = ""
b = f.readline()
while(b):
    
    g = b.split("\t")[2]
    p = g.split("(")[0]
    p = p.strip(" ")
    naam.write(p)
    naam.write(",")
    naam.write("\n")
    a += '"'+p+'"'+','
    b = f.readline()
f.close()
print a
