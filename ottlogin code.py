username=input("enter username")
password=input("enter password")
age=int(input("enter your age"))
plan=input("enter a basic/perimium/vvip")

if username =="anoopmadanu"and password =="anoop143":
  print("login sucessful")
else:
    print("login failed")
    exit()
    
if plan not in["basic","perimium","vvip"]:
    print("invalid plan.choose basic,perimumorvvip")
    
if age<13:
    category ="kids"
elif age<18:
    category ="teen" 
else:
    category ="adult"
    
HD="yes" if plan =="perimium"or plan == "vvip" else "no"

match plan:
    case"basic":
        screen=1
        price=99
    case"perimium":
        screen=4
        price=399
    case"vvip":
        screen=6
        price=599
        
print(f"welcome{username}") 
print(f"plan:{plan.upper()}| {price}/month")
print(f"screen:{screen}|HD.{HD}")
print(f" content category:{category}")

