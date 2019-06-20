def concatenate():
    servername=(input("Enter the server name-"))
    dname=(input("Enter the dbname-"))
    username=(input("Enter the username-"))
    password=(input("Enter the pasword-"))
    result=("servname="+servername+";dbname="+dname+";uname="+username+";password="+password+";")
    return result

res=concatenate()    
print(res)
