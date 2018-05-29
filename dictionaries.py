user = {'name': 'Маша', 'age': 25, 'have_airplane': False}
#print(len(user))
user['city'] = 'Moscow'
user['have_airplane'] = True

#print(user)
#print(user['name'])
#print(user.get('name'))
#print(user.get('country'))

#print(user.get('country', 'Russia'))

#print(user.get('balance', 0))


#del user['city']

print(user)
mylist = ['Вася', 'Маша', 'Саша']
user['friends'] = mylist
print(user)

