# print("Test")
# print("Test")
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

