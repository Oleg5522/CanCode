#i=1
#while i<10
#print(i)
#i+=1

#start = 1
#end = 10
s=0
string=input('Input')

for n in string:
    if  string.isdecimal():
        n=int(n)
        n+=1
    print(n)

word=input('Input word')
vowels = ('a','e')

