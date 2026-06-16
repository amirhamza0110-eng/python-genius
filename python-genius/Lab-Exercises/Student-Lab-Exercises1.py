#1. Capture inputs from user (Name, Age, Developer Status)

name = input("what is your name ? ")
age = int(input("what is your age? "))
developer = input("are you a developer?(yes/no) ").strip().lower()

#2. Evaluate conditional logic to determine the clearance tier
if age < 18:
    tier = "Tier 3: Guest"
elif developer == 'yes':
    tier = "Tier 1: Admin Infrastructure Access"
else:
    tier = "Tier 2: Standard Executive Access"
    
#3. Print out the final profile card using an f-string
print(f"Name is {name}, age is {age}, access level: {tier}")