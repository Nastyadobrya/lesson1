def get_answer(question):
	question = question.lower()
	answers = {'hi': 'Hello', 'How are you?':'I am fine','Goodbye':'Bye'}
	a = answers.get(question)
	return a#.lower()
print(get_answer('HI'))
