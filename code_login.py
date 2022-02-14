from getpass import getpass
def login():
    with open("login/userid.txt", "r") as f:
        u = f.read()
        uid = u.split(",")
        lu = len(uid)
    
    with open("login/password.txt", "r") as f:
        p = f.read()
        pd = p.split(",")

    dtl = {}
    for i in range(0,lu):
        dtl.update({uid[i]:pd[i]})

    a = input(" Enter your user name: \n")
    i = 0
    while a not in dtl.keys():
        if i < 4:
            print("You have entred wrong user name, try again")
            a = input(" Enter your user name: \n")
            i+=1
        else:
            print("You have entred to many wrong user name. \n Plese make your fresh user id or try after some time !!!!")
            break

    if a in dtl.keys():
        print("You have entred correct username")
        b = getpass("Now, Enter your password: \n")
        j = 0
        while b != dtl.get(a):
            if j < 4:
                print("You have entred wrong password, try again")
                b = getpass("Enter your password: \n")
                j+=1
            else:
                print("You have entred to many wrong password. \n Plese make your fresh user id or try after some time !!!!")
                break
                

        if b == dtl.get(a):
            print("Congratulations you have succesfully logged in: ")





