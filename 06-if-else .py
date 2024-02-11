#take a character from user and check if that character is vowel or consonant.

print('Please, input the character: ')
character = input()

if character>='a'and character<='z' or character>='A' and character<'Z':
    if character in 'aeiouAEIOU':
        print("The character is Vowel!")
    else:
        print("The character is consonant!")

else:
    print("Nothing!")