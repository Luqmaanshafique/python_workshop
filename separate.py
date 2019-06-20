def string():
    a=input('Enter the string')
    i=0
    b=a.split(';')
    c=b[0]
    d=b[1]
    e=b[2]
    f=b[3]
    s1=c.split('=')
    s2=d.split('=')
    s3=e.split('=')
    s4=f.split('=')
    result=(s1,s2,s3,s4)
    return result
res=string()
print(res)
