from random import randrange
from random import choice
import pickle
# First name handling
f_name = input("Enter your first Name: ")
while not f_name:
    f_name = input("Enter your first Name: ")

# Last name handling
l_name = input("Enter your last Name: ")
while not l_name:
    l_name = input("Enter your last Name: ")

# Handling the first username
f_name =f_name.title()
l_name = l_name.title()
print(f"Great! You are {f_name} {l_name}")

initial1 = ''
for i in f_name: 
    if i.isupper():
       initial1 += i
initial2 = ''
for i in l_name:
    if i.isupper():
        initial2 +=i

nospace_f_name = f_name.replace(' ','')
user_name1 = initial1+initial2+str(len(nospace_f_name + l_name))
print(user_name1)
# handling the second username
user_name2=nospace_f_name.capitalize() +""+l_name.lower()
print(user_name2)

#handling the third username 
random_number = randrange(100,1000)
fn= f_name.split()
fn1 = fn[0]

for i in fn:
    if len(i)<len(fn1):
        fn1=i


ln=l_name.split()
# print(ln)
# print(fn)
ln1=ln[0]
for y in ln:
    if len(ln1)>len(i):
        len1=y

smalest_name = ''
if len(fn1)<len(ln1):
    smalest_name=fn1
else:
    smalest_name=ln1

reversal=smalest_name[::-1]
username3=reversal+str(random_number)
user_name3=username3.title()
print(user_name3)
usernames= [f_name, l_name, user_name1, user_name2, user_name3]

#handling username choice
fav_username=[]
for i in usernames:
    if len(i)<8:
        fav_username.append(i)

# write list to binary file
def write_list(a_list):
    with open('database.txt', 'ab') as fp:
        pickle.dump(myfav_username, fp)
        print('Done writing list into database')

# Read list to memory
def read_list():
    with open('database.txt', 'rb') as fp:
        n_list = pickle.load(fp)
        return n_list

# list of names
myfav_username =choice(fav_username)
write_list(myfav_username)
r_names = read_list()
print('List is', r_names)


