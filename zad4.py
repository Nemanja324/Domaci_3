tekst = input('Unesite string: ')
br = 0
for i in range(len(tekst)-1):
    if tekst[i] == tekst[i+1]:
        br += 1
    else:
        pass
print(br)
