import json
from difflib import get_close_matches as gcm

data = json.load(open("data.json"))

def lookup(key):
	key = key.lower()
	if key in data:
		return data[key]
	elif len(gcm(key, data.keys(), 1, 0.8)) > 0:
		suggestion = gcm(key, data.keys(), 1, 0.8)[0]
		answer = input("Did you mean '%s'? [Y/N] " % suggestion)

		if answer == 'Y':
			return data[suggestion]
		else:
			print("Please try another word.")
			return []
	else:
		print("This word does not exist.")
		return []

key = input("Enter a word: ")
result = (lookup(key))

number = 1

for definition in result:
	print(str(number) + ': ' + definition)
	number += 1
