alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

link = input('Добро пожаловать в шифровщик Цезаря, введите путь к файлу, который вы хотите зашифровать: ')
parol = int(input('Введите число - ключ шифрования, и обязательно запомните его, если захотите расшифровать текст обратно:')) % 36
raznica = 33
mode = input('введите Y, если хотите зашифровать текст, и N, если расшифровать ')
if mode == 'N':
    parol = -parol
    raznica = -raznica
    print('Расшифрование текста')
elif mode == 'Y':
    print('Шифрование текста')

f = open(link, 'r')
text = []
for line in f:
    copyline = ''
    for char in line.lower():
        if char in alphabet:
            simbol = alphabet.index(char)
            if simbol + parol < 33 and simbol + parol >= 0:
                copyline += alphabet[simbol + parol]
            else:
                copyline += alphabet[simbol + parol - raznica]
        else:
            copyline += char
    text.append(copyline)
f.close()
f = open(link, 'w')

for line in text:
    f.write(line)
f.close()
