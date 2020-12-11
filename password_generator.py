import random
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456!@#$%^&*()"
users = ['user1', 'user2', 'user3']

users_count = 0
for i in users:
    users_count = users_count + 1


pass_len = int(input("Password length = "))
pass_count = users_count

user_passwords={}
for user in users: # For each user
    password=""
    for i in range(0, pass_len): # Lets generate the password
        password = password + random.choice(chars) # Add a random character
    user_passwords[user] = password # assign the password to the user

for user in users:
    print(user," Password : ",user_passwords[user])