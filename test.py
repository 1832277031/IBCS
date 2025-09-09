print("Test")
print("Test")
print("It \' s a beautiful day")
print("Computer Science is \"fun\" ")
print("Computer \nScience \nis \nfun")
print("""在使用 Git 进行版本控制时，
    遇到提示 \"Everything up-to-date\"，通常意味着你尝试推送(push)到远程仓库时，本地仓库与远程仓库已经同步,没有新的更改需要推送。然而,有时你可能确实进行了更改但仍收到此提示。
    本文将详细介绍如何解决这一问题,确保你的更改能够顺利推送到远程仓库。""")

math=[80,80,80]
sci=[70,90,100]
eng=[90,70,80]
for i in range(3):
    total=math[i]*0.4+sci[i]*0.35+eng[i]*0.25
    if total>=80:
        passed=True
        print("Student \' s total score is",float(total), passed)
        print("Student \'s total score is %.1f %s" % ((total), passed))
        print(f'{"Student \' s total score is"} {total} {passed} ')
        print("Student \' s total score is {} {}".format(total,passed))
    else:
        passed=False
        print("Student \' s total score is" + str(total) + str(passed))
        print("%s total score is %s %s" % ("Student \' s",(total), passed))
        print(f'{"Student \' s total score is"} {total} {passed} ')
        print("Student \' s total score is {} {}".format(total,passed))




print("Please enter your full name, house / flat number and street number or name: ")
fname = input("first name: ")
lname = input("last name: ")
fullname = fname+" "+lname
house = input("house / flat number: ")
street = input("street number and name: ")
length = len(fullname.strip())
print("From", fullname,"\n Address", house, street,"\n and the length of your name is:", length)
print("Enter a noun and a letter")
str1=input("your noun: ")
letter=input("your letter: ")
str2=str1.replace(letter , "@")
print(str2)
