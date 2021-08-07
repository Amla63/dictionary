dic=[{"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, {"six":"9"},{"seven":"7"}]
i=0
a={}
s=[]
h=[]
while i<len(dic):
    d=dic[i]
    for v in dic[i]:
        s.append(v)
        if d[v] not in h:
            h.append(dic[i][v])
        i=i+1
print(h)









    

                                                                                                                                                                                                                                    



