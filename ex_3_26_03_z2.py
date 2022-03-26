def palindrome(word):
    if word == word[::-1]:
        print(f'{word} \033[32myes, the word is a palindrome\033[0m')
    else:
        print(f'{word} \033[31m the word is not a palindrome\033[0m')


list_1 = ['deed', 'nun', 'level', 'peep', 'love', 'cow', 'deified', 'sagas', 'gas']
for i in list_1:
    palindrome(i)
