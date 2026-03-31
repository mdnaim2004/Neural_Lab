import random

pas = input("Enter your Password : ")

keys = [
    
    "A","B","C","D","E","F","G","H","I","J","K","L","M",
    "N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
   

]

pwg = ""

while pwg != pas:
    pwg = "" 
    
    for i in range(len(pas)):
        pwg += random.choice(keys)

    print(pwg)

print(f"Your Password is : {pwg}")