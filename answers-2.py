answers = {'привет': 'И тебе привет!', 'как дела': 'Лучше всех!', 'пока': 'Увидимся'}

def get_answer():
    while True:
        question = input('что скажешь?: ')
        question = str.lower(question)
        relevant_answer = answers.get(question)
        if question == 'пока':
            return relevant_answer
        if relevant_answer == None:
            return 'Ну и бывай как знаешь!'
        print(relevant_answer)


result = get_answer()
print(result)

