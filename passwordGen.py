import random
import string


def validate(password):
    '''Check if password meets the following conditions:
    1 - Starts with a letter
    2 - Contains at least one digit
    3 - Contains both upper and lower case
    returns True or False'''
    for char in password:
        if char.isalpha() == True:
            break
        else:
            return False
    if any(i.isdigit() for i in password) == True:
    	pass
    else:
        return False
    if any(i.isupper() for i in password) == True:
    	pass
    else:
    	return False
    if any(i.islower() for i in password) ==  True:
    	pass
    else:
    	return False
    return True

def generate():
	'''Generates a password using SystemRandom, choosing from uppercase, lowercase and numbers.
	Checks if password meets the criteria (validate): If not, loops until it returns 
	with a working password'''
	while True:
	    length = random.randint(6,10)
	    password = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for i in range(length))
	    if validate(password) == True:
	    	print(f'Your password is {password}')
	    	print('')
	    	break
	    else:
	    	continue


while True:
	print('Password Generator')
	choice = input('Enter Y to generate new password, enter any other key to exit: ')
	if choice.lower() == 'y':
		generate()
	else:
		break
