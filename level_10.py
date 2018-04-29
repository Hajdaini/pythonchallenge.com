def seq(a):
    a = str(a)
    k,last,result = 1,a[0],''
    for i in range(1,len(a)):
        if last==a[i]:k+=1
        else:
            result = result+str(k)+last
            k=1
        last = a[i]
    result = result+str(k)+last
    return result

value = 1
for x in range (30):
    value = seq(value)

print(len(value))