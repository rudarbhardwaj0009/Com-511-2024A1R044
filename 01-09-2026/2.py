# Write a python program to fill the given letter template with name and date
letter = '''
You are selected!
<Date>
'''

n=input("Enter name :")
d=input("Enter date :")

l=letter.replace("<Name>", n)
l=letter.replace("<Date>", d)

print(l)