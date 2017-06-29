# Hangman game

import random

WORDS_FILE = 'hw7_words.txt'

# retrieves words from WORDS_FILE
def load_words():
	print("Loading random word from word bank ")
	text_file = open(WORDS_FILE, "r")
	words = text_file.read().split(' ')
	
	# after opening a file, must close
	text_file.close()

	return words

def get_random_word(words):
	a_word = random.choice(words)
	return a_word

words = load_words()

word = get_random_word(words)

print(word)

word_l = len(word)
guess = word_l * 2

ans = ['_'] * word_l

print("====================== Welcome to Hangman Game !! ======================")
print("I am thinking of a word that is %d letters long" % (word_l))
print("========================================================================")

alphabets = "abcdefghijklmnopqrstuvwxyz"
available_items = []
for c in alphabets:
	available_items.append(c)

win = False

while guess > 0:
	print('================= You have %d guesses left. =================' % (guess))
	
	letter = raw_input('Please guess a letter: ')

	if letter in available_items:
		available_items.remove(letter)
		print("Available Letters: [%s]" % ("".join(available_items)))

		if letter in word:
			indices = [i for i, ltr in enumerate(word) if ltr == letter]

			for i in indices:
				ans[i] = letter
			print("Good Guess: %s" % ("".join(ans)))

			if word == "".join(ans):
				win = True
				break

		else:
			print("Oops! That letter is not in my word: ")

		guess = guess - 1
	else:
		print("You've already guessed that letter")
	

if win:
	print("Congratulations, You've guessed the word correctly. ")
else:
	print("You failed. ")
