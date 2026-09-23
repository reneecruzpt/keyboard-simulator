#usando o fatiamento

palavra = input('Enter the word which you need verify: ')
palavra_invertida = palavra[::-1]

if palavra == palavra_invertida:
    print(f'{palavra} is a palindrome, reversed word: {palavra_invertida}')
else:
    print(f'{palavra} is not a palindrome, reversed word: {palavra_invertida}')