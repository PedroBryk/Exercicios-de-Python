n = input('Digite algo: ')
print('Você digitou: {}'.format(n), 'É alfanúmerico?', n.isalnum())
print('Você digitou: {}'.format(n), 'É alfabetico?', n.isalpha())
print('Você digitou: {}'.format(n), 'É decimal?', n.isdecimal())
print('Você digitou: {}'.format(n), 'É em minúsculo?', n.islower())
print('Você digitou: {}'.format(n), 'É em maiusculo?', n.isupper())
print('Você digitou: {}'.format(n), 'Tem espaço?', n.isspace())