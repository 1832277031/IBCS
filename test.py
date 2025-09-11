# print("Test")
# print("It \' s a beautiful day")
# print("Computer Science is \"fun\" ")
# print("Computer \nScience \nis \nfun")
# print("""在使用 Git 进行版本控制时，
#     遇到提示 \"Everything up-to-date\"，通常意味着你尝试推送(push)到远程仓库时，本地仓库与远程仓库已经同步,没有新的更改需要推送。然而,有时你可能确实进行了更改但仍收到此提示。
#     本文将详细介绍如何解决这一问题,确保你的更改能够顺利推送到远程仓库。""")

# math=[80,80,80]
# sci=[70,90,100]
# eng=[90,70,80]
# for i in range(3):
#     total=math[i]*0.4+sci[i]*0.35+eng[i]*0.25
#     if total>=80:
#         passed=True
#         print("Student \' s total score is",float(total), passed)
#         print("Student \'s total score is %.1f %s" % ((total), passed))
#         print(f'{"Student \' s total score is"} {total} {passed} ')
#         print("Student \' s total score is {} {}".format(total,passed))
#     else:
#         passed=False
#         print("Student \' s total score is" + str(total) + str(passed))
#         print("%s total score is %s %s" % ("Student \' s",(total), passed))
#         print(f'{"Student \' s total score is"} {total} {passed} ')
#         print("Student \' s total score is {} {}".format(total,passed))

# print("Please enter your full name, house / flat number and street number or name:")
# fname=input("first name: ")
# lname=input("last name: ")
# fullname=fname+" "+lname
# length=len(fullname.strip())
# house=input("house / flat number: ")
# street=input("street number and name: ")
# print("From: ", fullname, "\n Address: ",house, street)
# print("The length of your name is ",length)
# print("Please enter a noun and a letter: ")
# string1=input("Noun: ")
# letter=input("Letter: ")
# string2 = string1.replace(letter, "@")
# print(string2)

# testString="This is a test string"
# textFind=input("Enter a word to find: ")
# print(testString.find(textFind))

# testString="This is a test string This is a test string This is a test string This is a test string" 
# textFind=input("Enter a word to find: ")
# print("First instance is ", testString.find(textFind))
# print("Last instance is ", testString.rfind(textFind))

# testString="This is a test string"
# sub=slice(0,4)
# print(testString[sub])
# print(testString[slice(0,4)])

# text="This is a test string"
# subtext=text.split()
# print(subtext)
# print(len(subtext))
# print(subtext[0])

# username=input("Enter your username: ")
# spaceremove=username.strip()
# if username=="admin":
#     truename=username.replace("admin","player")
#     finalname=truename+"_Gamer"
#     print("The final name is: ",finalname)
# textfind="_"
# for i in range(len(username)):
#     if username[i]==textfind:
#         print("The first underscore is at index:", username.find(textfind))
#         print("The last underscore is at index:", username.rfind(textfind))
#         subtext=username.split("_")
#         print("The clan name is: ",subtext)
#         print("The length of the clan name is: ",len(subtext))
#         break
#     else:
#         print("No clan")
# finalname=username+"_Gamer"
# firstletter=finalname.index(finalname[0])
# lastletter=finalname.index(finalname[len(finalname)-1])
# print(firstletter)
# print(lastletter)

array1=[0,1,2,3,4,0]
array2=[]
total=0
count=0
if array1[0]==array1[5]:
    print("True")
number=int(input("Enter a number: "))
array2=[0 for i in range(number)]
for i in range(number):
    array2[i]=int(input("Enter a number for array2: "))
for i in range(number):
    if int(array2[i])%2==0:
        total=sum(array2)
        count=count+1
if total!=0:
    print("The sum of even number is: ",total," and the average is: ",total/count)
print("The number of odd number is: ",number-count)

array3=["steven","anna","danial","fred","jason"]
array3.reverse()
print(array3)

