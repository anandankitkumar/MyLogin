import code_login as lg

with open("login/userid.txt", "r") as fnew:
        unew = fnew.read()
        uidnew = unew.split(",")
        
def loginnew():
    print('''For login enter 1
    For creating new user id and password enter 2''')
    def z_check():
        global z
        try:
            z = int(input("Enter Your Choice: \n"))
        except Exception:
            print("Please Enter Correct Choice:")
            z_check()
        finally:
            pass
    z_check()

    if z == 1:
        lg.login()
    elif z ==2:
        
        def ck_newuser():
            global newuser
            newuser = input("Enter your username")
            
            while newuser  in uidnew:
                print("username already availble, try diffrent combinations: \n")
                newuser = input("Enter your username")
                ck_newuser()
            
            while " "  in newuser:
                print("Please enter username, without space: \n")
                newuser = input("Enter your username")
                ck_newuser()
        ck_newuser()
        
        newpass = input("Enter your password")
        with open("login/userid.txt", "a") as fnew:
            fnew.write(','+newuser)
        with open("login/password.txt", "a") as fnew:
            fnew.write(','+newpass)
        print("Congratulations your new userid and password is created !!! \n Login Now....")
        lg.login()
    else:
        print("You have entered wrong choice, Try again:")
        loginnew()

loginnew()