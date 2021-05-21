email=str(input("Please enter your email address: "))
username=email[:email.index("@")]
password=email[email.index("@")+1:]
print("your username is {0} and domain is {1}".format(username,password))
