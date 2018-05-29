def cut_cake():
    try:
        parts = input('На сколько частеей будем делить пирог?: ')
        cake_part = 1 / int(parts)
        return 'каждому достается по {} части пирога'.format(cake_part)
    except (ZeroDivisionError, ValueError):
        return "Вы что, с ума посходили?"
cake = cut_cake()
print(cake)