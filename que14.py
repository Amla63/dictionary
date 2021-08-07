dic={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}


b=[]
for i in dic:
    a=dic[i]
    b.append(a)
i=0
while i<len(b):
    j=0
    while j<len(b)-1:
        if b[j]>b[j+1]:
            b[j],b[j+1]=b[j+1],b[j]
        j+=1
    i+=1
newdic = {}
for k in b:
    for j in dic:
        if k==dic[j]:
            newdic[j]=k
print(newdic)