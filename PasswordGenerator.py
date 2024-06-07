import random
def PasswordGenerator(pwl):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    password = "" 
    for j in range(pwl):
        index = random.randint(0, len(alphabets)-1)
        password = password + alphabets[index]  
    password = replace_with_number(password)
    password = replace_with_uppercase_letter(password)   
    return password
def replace_with_number(pword):
    for i in range(random.randint(1,2)):
        index = random.randint(0, len(pword)//2)
        pword = pword[0:index] + str(random.randint(0,9)) + pword[index+1:]
    return pword
def replace_with_uppercase_letter(pword):
    for i in range(random.randint(1,2)):
        index = random.randint(0, len(pword)//2)
        pword = pword[0:index] + pword[index].upper() + pword[index+1:]
    return pword
no_of_Passwords = int(input("How many passwords do you want to generate? "))   
print("Generating " +str(no_of_Passwords)+" passwords")
Lengths_of_Passwords = []
print("Minimum length of password should be 3")
for i in range(no_of_Passwords):
    length = int(input("Enter the length of Password #" + str(i+1) + " "))
    if length<3:
        length = 3
    Lengths_of_Passwords.append(length)
for j in range(no_of_Passwords):
    print("Password #"+str(j+1)+" = "+ PasswordGenerator(Lengths_of_Passwords[j]))