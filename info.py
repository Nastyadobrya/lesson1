user_info = {'first_name': 'Анастасия', 'last_name':'Добрянская'}
print (user_info.get('first_name'))
user_info['first_name'] = str(input('Как вас зовут? '))
print (user_info.get('first_name'))
user_info['last_name'] = str(input('Ваша фамилия? '))
print (user_info.get('first_name'))
print (user_info)