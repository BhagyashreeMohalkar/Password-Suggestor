import random
import string

adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'fat', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'fluffy', 'white', 'proud', 'brave']
nouns = ['apple', 'dinosaur', 'ball', 'toaster', 'goat', 'dragon', 'hammer', 'duck', 'panda']

print('Welcome to Password Picker!')
print('This tool generates a random password for you.')

while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)
    password = adjective.capitalize() + noun.capitalize() + str(number) + special_char
    print('\nYour new password is:', password)
    
    while True:
        response = input('\nWould you like another password? (yes/no): ').strip().lower()
        if response in ['yes', 'no']:
            break
        else:
            print('Invalid input! Please enter "yes" or "no".')
    
    if response == 'no':
        print('Thank you for using Password Picker!')
        break
