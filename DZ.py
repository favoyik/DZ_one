slovo = str.lower(input('Впишите слово, чтобы проверить его на палиндром: '))
rev = reversed(slovo)
if list(slovo) == list(rev):
    print('True')
else:
    print('False')
