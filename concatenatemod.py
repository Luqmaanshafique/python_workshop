def concatenatemod():
    servername=(input("Enter the server name-"))
    dname=(input("Enter the dbname-"))
    username=(input("Enter the username-"))
    password=(input("Enter the pasword-"))
    #result="servname="+servername+";dbname="+dname+";uname="+username+";password="+password+";"
    result="servername=%s;dbname=%s;uname=%s;password=%s;" %(servername,dname,username,password)
    return result

res=concatenatemod()    
print(res)

