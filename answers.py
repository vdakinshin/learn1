answers = {'привет': 'И тебе привет!', 'как дела': 'Лучше всех!', 'пока': 'Увидимся'}

def get_answer():
    question = input('что скажешь?: ')
    question = str.lower(question)
    relevant_answer = answers.get(question)
    return relevant_answer

result = get_answer()
print(result)
