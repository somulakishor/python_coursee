def greek(name,region):
    message=get_message(region)
    return message + " " + name
def get_message(region):
    if(region == "USA"):
        return "Hello"
    elif(region == "India"):
        return "Namaste"
print(greek("kishor","India"))

A="kishor"
new=" "
for i in A:
    new=i+new
print(new)

count=0
for i in A:
    count+=1
print(count)

print(len([i for i in A if i.isalpha()]))

input="a 30 b 20 c  40 d 50"
A=input.split()
print(A)
B=[]
C=[]
for i in A:
    if i.isdigit()== True:
        B.append(i)
    if i.isalpha()== True:
        C.append(i)
C.extend(B)
output=" ,".join(C)
print((output))

A="kishor Reddy"
print(A.split(" "))
print(tuple(A.split()))
print(set(A.split()))

A="kishor123,kishor,kiran234,kiran"
B=[]
for i in A.split(','):
    if i.isalpha()==False:
        B.append(i)
print(B)


A="google.com"
def count(A):
    dict={}
    for i in A:
        keys=dict.keys()
        print(keys)
        if i in keys:
            dict[i]+=1
        else:
            dict[i]=1
    return dict
print(count(A))

A="kishor"
B={}
for i in A:
    B[i]=0
print(B)

print(dict.fromkeys(A,0))

A="kishor25 And my age is age30"
B=[]
for i in A.split():
    print(i)
    if not i.isalpha():
        B.append(i)
print(B)

A='I am 25 years and 10 months old'

B=[]
for i in A.split():
    if not i.isalpha():
        B.append(i)
        C=" ".join(B)
print(C)

B=",".join([i for i in A if i.isdigit()])
print(B)

A=['a','b','c']
B=",".join(A)
print(B)

A=("kishor","reddy")
print(" ".join(A))
print(list(A))
A=('1','2','3')
print("".join(map(str,A)))
print(list(map(int,A)))

t=(4,4,4)

n=all(i==t[0] for i in t)
print(n)


A= (11, 22, 33, 44, 55, 66)
#output = 44,55
B=list(A)
B[2]=333
A=tuple(B)
print(A)
B=A[-3:-1]
print(B)
print(A[:-3])
print(A[-3:])
print(A[3:-1])
B=A[2]
C=A[4]
print(B, C)

A="kishor"
B=" "
C=len(A)//2
for i in range(len(A)):
    if i<C:
        B+=A[i].upper()
    else:
        B+=A[i]
print(B)

print(set([i for i in A if A.count(i)>1]))

num=12
for i in range(1,11):
    print(num,"X",i,"=",num*i)
    
    
A=['aa','bb','aa','bb','cc']
B=set(A)
C={name:A.count(name)for name in B}
print(C)

A="google.com"
B=set(A)
print({name:A.count(name)for name in B})

dict={}
for i in A:
    keys=dict.keys()
    if i in keys:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)


