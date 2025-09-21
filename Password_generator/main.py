import random

print("Welcome to Password Generator")
print("="*len("welcome to password generator"))

chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789"

user_input=int(input("Enter the number of passwords you want: "))
length=int(input("Enter the length of the password: "))

print("Here are your Passwords:")

for pwd in range(1,user_input+1):
    password=""
    for c in range(length):
        password += random.choice(chars)
        
    print(f"Password {pwd} -> ",password)