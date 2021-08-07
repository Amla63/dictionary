num={"one":1,"two":2,"three":3,"five":5,"four":4}
n=max(num.values())
m=max(num,key=num.get)
print("max key,value",   m,n)

n=max(num.values())
m=max(num,key=num.get)
print("minimum key,value",   m,n)