__author__ = "Christina Marcial"

from typing import overload

class Morse(object):
	"""Class for finding morse code translation
	"""
	def __init__(self, word: str) -> None:
		"""

		Args:
			word (str): given word
		"""
		self.word = word

	def set_word(self, word: str) -> None:
		"""Set world

		Args:
			word (str): word in ASCII
		"""
		self.word = word

	def get_word(self) -> str:
		"""Get word

		Returns:
			str: word
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
		wordArray = list(word)
		for i in wordArray[:]:
			if (i.isalpha() == True):
				pass
			elif (i.isdigit() == True):
				pass
			else:
				wordArray.remove(i)

		#print(word)
		length = len(wordArray)

		for x in range(length):
			string = wordArray[int(x)]
			if string == 'a':
				wordArray[int(x)] = '._'

			elif string == 'b':
				wordArray[int(x)] = '_...'

			elif string == 'c':
				wordArray[int(x)] = '_._.'

			elif string == 'd':
				wordArray[int(x)] = '_..'

			elif string == 'e':
				wordArray[int(x)] = '.'
			
			elif string == 'f':
				wordArray[int(x)] = '.._.'

			elif string == 'g':
				wordArray[int(x)] = '__.'

			elif string == 'h':
				wordArray[int(x)] = '....'

			elif string == 'i':
				wordArray[int(x)] = '..'

			elif string == 'j':
				wordArray[int(x)] = '.___'

			elif string == 'k':
				wordArray[int(x)] = '_._'

			elif string == 'l':
				wordArray[int(x)] = '._..'

			elif string == 'm':
				wordArray[int(x)] = '__'

			elif string == 'n':
				wordArray[int(x)] = '_.'

			elif string == 'o':
				wordArray[int(x)] = '___'

			elif string == 'p':
				wordArray[int(x)] = '.__.'

			elif string == 'q':
				wordArray[int(x)] = '__._'

			elif string == 'r':
				wordArray[int(x)] = '._.'

			elif string == 's':
				wordArray[int(x)] = '...'

			elif string == 't':
				wordArray[int(x)] = '_'

			elif string == 'u':
				wordArray[int(x)] = '.._'

			elif string == 'v':
				wordArray[int(x)] = '..._'

			elif string == 'w':
				wordArray[int(x)] = '.__'

			elif string == 'x':
				wordArray[int(x)] = '_.._'

			elif string == 'y':
				wordArray[int(x)] = '_.__'

			elif string == 'z':
				wordArray[int(x)] = '__..'

			elif string == '0':
				wordArray[int(x)] = '_____'

			elif string == '1':
				wordArray[int(x)] = '.____'

			elif string == '2':
				wordArray[int(x)] = '..___'

			elif string == '3':
				wordArray[int(x)] = '...__'

			elif string == '4':
				wordArray[int(x)] = '...._'

			elif string == '5':
				wordArray[int(x)] = '.....'

			elif string == '6':
				wordArray[int(x)] = '_....'

			elif string == '7':
				wordArray[int(x)] = '__...'

			elif string == '8':
				wordArray[int(x)] = '___..'

			elif string == '9':
				wordArray[int(x)] = '____.'

		#print(word)
		code = ""
		code = code.join(wordArray)
		codeList = list(code)
		#print(code)

		newCode="".join([str(i) for i in codeList])
		#print(newCode)

		txt = newCode[::-1]
		#print(txt)

		if newCode == "":
			return 0
		elif newCode == txt:
			return 1
		else:
			return 0

	def get_solve(self) -> int:
		"""Get solution

		Returns:
			str: solution
		"""
		return self.solve()
	
	def __str__(self) -> str:
		"""String rep of answer

		Returns:
			str: solution as string
		"""
		return f'{self.get_solve()}'

	def _repr_(self) -> str:
		"""Return string rep

		Returns:
			str: string rep
		"""
		return self.__str__()