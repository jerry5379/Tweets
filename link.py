import pyshorteners

link= input("enter th link")
shortener = pyshorteners.Shortener()
x= shortener.tinyurl.short(link)
print(x)
y=x
z= shortener.tinyurl.expand(y)
print(z)

