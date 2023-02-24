__author__ = "Christina Marcial"

from typing import Any

class Morse(object):
	"""_summary_

	Args:
		object (_type_): _description_
	"""
	def __init__(self, word: str) -> None:
		"""_summary_

		Args:
			word (str): given word
		"""
		self.word = word

	def set_word(self, word: str) -> None:
		"""_summary_

		Args:
			word (str): _description_
		"""
		self.word = word

	def get_word(self) -> str:
		"""_summary_

		Returns:
			str: _description_
		"""
		return self.word

	def solve(self) -> int:
		"""Returns whether the word is a
		palindrome in morse code or not

		Returns:
			int: 1 if palindrome, 0 if not
		"""
		#convert given word into 'morse code'

		#print("self.word: ")
		#print(self.word)
		word = self.word
		word = word.lower()
		#print(word)
		word = list(word)
		for i in word[:]:
			#print("i: ")
			#print(i)
			if (i.isalpha() == True):
				#print("is alpha!")
				pass
			elif (i.isdigit() == True):
				#print("is digit!")
				pass
			else:
				#print("remove!")
				word.remove(i)

		#print(word)

		for i in range(len(word)):
			if word[i] == 'a':
				word[i] = '._'

			elif word[i] == 'b':
				word[i] = '_...'

			elif word[i] == 'c':
				word[i] = '_._.'

			elif word[i] == 'd':
				word[i] = '_..'

			elif word[i] == 'e':
				word[i] = '.'
			
			elif word[i] == 'f':
				word[i] = '.._.'

			elif word[i] == 'g':
				word[i] = '__.'

			elif word[i] == 'h':
				word[i] = '....'

			elif word[i] == 'i':
				word[i] = '..'

			elif word[i] == 'j':
				word[i] = '.___'

			elif word[i] == 'k':
				word[i] = '_._'

			elif word[i] == 'l':
				word[i] = '._..'

			elif word[i] == 'm':
				word[i] = '__'

			elif word[i] == 'n':
				word[i] = '_.'

			elif word[i] == 'o':
				word[i] = '___'

			elif word[i] == 'p':
				word[i] = '.__.'

			elif word[i] == 'q':
				word[i] = '__._'

			elif word[i] == 'r':
				word[i] = '._.'

			elif word[i] == 's':
				word[i] = '...'

			elif word[i] == 't':
				word[i] = '_'

			elif word[i] == 'u':
				word[i] = '.._'

			elif word[i] == 'v':
				word[i] = '..._'

			elif word[i] == 'w':
				word[i] = '.__'

			elif word[i] == 'x':
				word[i] = '_.._'

			elif word[i] == 'y':
				word[i] = '_.__'

			elif word[i] == 'z':
				word[i] = '__..'

			elif word[i] == '0':
				word[i] = '_____'

			elif word[i] == '1':
				word[i] = '.____'

			elif word[i] == '2':
				word[i] = '..___'

			elif word[i] == '3':
				word[i] = '...__'

			elif word[i] == '4':
				word[i] = '...._'

			elif word[i] == '5':
				word[i] = '.....'

			elif word[i] == '6':
				word[i] = '_....'

			elif word[i] == '7':
				word[i] = '__...'

			elif word[i] == '8':
				word[i] = '___..'

			elif word[i] == '9':
				word[i] = '____.'

			#else:
			#	word[i] = 'xxxxxx'

		#print(word)
		#for i in word:
		#    word[i].split
		code = ""
		code = code.join(word)
		code = list(code)
		#print(code)

		newCode="".join([str(i) for i in code])
		#print(newCode)

		txt = newCode[::-1]
		#print(txt)

		if newCode == "":
			return f'0'
		elif newCode == txt:
			return f'1'
		else:
			return f'0'
		
	def get_solve(self) -> int:
		"""_summary_

		Returns:
			str: _description_
		"""
		return self.solve()
	
	def __str__(self) -> str:
		"""_summary_

		Returns:
			str: _description_
		"""
		return f'{self.get_solve()}'

	def _repr_(self) -> str:
		"""_summary_

		Returns:
			str: _description_
		"""
		return self.__str__()