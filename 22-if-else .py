#take a word from user to check if that is palindromic or not

print('Please input your word: ')
word = input()
word = word.casefold()
reversed_word = word[::-1]

if word == reversed_word:
    print('Great! It is a palindrome.')
else:
    print('LOL!! It is not a palindrome.')
