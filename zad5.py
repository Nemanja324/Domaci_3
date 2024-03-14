lista = [
    {
        'naziv': 'Español para principiantes',
        'br_pozitivni': 1000,
        'br_negativni': 10
    },
    {
        'naziv': 'Philophize This!',
        'br_pozitivni': 500,
        'br_negativni': 30
    },
    {
        'naziv': 'Science VS.',
        'br_pozitivni': 600,
        'br_negativni': 45
    },
]
maxi = 9999
ime = ''
for i in lista:
    if i['br_pozitivni'] / i['br_negativni'] < maxi:
        maxi = i['br_pozitivni'] / i['br_negativni']
        ime = i['naziv']
print(f'Najgori odnos ime {ime}, sa odnosom od {maxi}')
