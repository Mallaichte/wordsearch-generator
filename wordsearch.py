import math
import random
import string
import sys
import os
# Get search words (or display help)
wordlist = []
if len(sys.argv) > 1:
	if sys.argv[1] == "-h" or sys.argv[1] == "--help":
		print("Run without arguments for interface or \"-sw [search-words-seperated-by-hyphen-here]\" to give your search words in the command line.")
		os._exit(os.EX_OK)
	elif sys.argv[1] == "-sw":
		searchwords = sys.argv[2]
		searchwords = searchwords.upper()
		wordlist = searchwords.split("-")
else:
	searchwords = input ("Enter the words to search separated by a space: ")  + "  "
	searchwords = searchwords.upper().rstrip(" ")
	wordlist = searchwords.split(" ")

print()
print("Words are: " + str(wordlist))
print()
# Generate grid
full_content = []
i = 0
row_col_size = int(math.sqrt(len(searchwords.replace(" ",""))*5)+1)
# Check if any word is larger than row_col_size and increase to suit
for nextword in wordlist:
	if len(nextword) > row_col_size:
		row_col_size = len(nextword)
gridsize = row_col_size * row_col_size

#print("rows and columns are: " + str(row_col_size) + " and grid size is: " + str(gridsize))
while i in range(0,gridsize):
	full_content.append("|.")
	i += 1

# Place words
x, y = 0, 0
for nextword in wordlist:
	if random.randint(1,2) == 1:
		if random.randint(1,2) ==1:
			#horizontal
			#forward
			tcount = 0
			while tcount < 1:
				#set coords
				x = random.randint(0,row_col_size - len(nextword))
				y = random.randint(0,row_col_size)
				pos = x + (y * row_col_size)
				#check for clash with other words
				checkword = False
				nchar_count = 0
				npos = pos
				nx = x
				while nchar_count < len(nextword):
					if full_content[npos] != "|." and  full_content[npos] != "|" + nextword[nchar_count]:
						checkword = True
					nchar_count += 1
					nx += 1
					npos = nx + (y * row_col_size)
				if checkword:
					continue
				else:
					#insert word
					nchar_count = 0
					while nchar_count < len(nextword):
						pos = x + (y * row_col_size)
						full_content[pos] = "|" + nextword[nchar_count]
						nchar_count += 1
						x += 1
				tcount += 1
		else:
			#horizontal
			#backward
			tcount = 0
			while tcount < 1:
				#set coords
				x = random.randint(len(nextword),row_col_size-1)
				y = random.randint(0,row_col_size)
				pos = x + (y * row_col_size)
				#check for clash with other words
				checkword = False
				nchar_count = 0
				npos = pos
				nx = x
				while nchar_count < len(nextword):
					if full_content[npos] != "|." and  full_content[npos] != "|" + nextword[nchar_count]:
						checkword = True
					nchar_count += 1
					nx -= 1
					npos = nx + (y * row_col_size)
				if checkword:
					continue
				else:
					#insert word
					nchar_count = 0
					while nchar_count < len(nextword):
						pos = x + (y * row_col_size)
						full_content[pos] = "|" + nextword[nchar_count]
						nchar_count += 1
						x -= 1
				tcount += 1

	else:
		if random.randint(1,2) ==1:
			#vertical
			#forwards
			tcount = 0
			while tcount < 1:
				#set coords
				x = random.randint(0,row_col_size)
				y = random.randint(0,row_col_size - len(nextword))
				pos = x + (y * row_col_size)
				#check for clash with other words
				checkword = False
				nchar_count = 0
				npos = pos
				ny = y
				while nchar_count < len(nextword):
					if full_content[npos] != "|." and full_content[npos] != "|" + nextword[nchar_count]:
						checkword = True
					nchar_count += 1
					ny += 1
					npos = x + (ny * row_col_size)
				if checkword:
					continue
				else:
					#insert word
					nchar_count = 0
					while nchar_count < len(nextword):
						pos = x + (y * row_col_size)
						full_content[pos] = "|" + nextword[nchar_count]
						nchar_count += 1
						y += 1
				tcount += 1
		else:
			#backwards
			tcount = 0
			while tcount < 1:
				#set coords
				x = random.randint(0,row_col_size)
				y = random.randint(len(nextword),row_col_size-1)
				pos = x + (y * row_col_size)
				#check for clash with other words
				checkword = False
				nchar_count = 0
				npos = pos
				ny = y
				while nchar_count < len(nextword):
					if full_content[npos] != "|." and full_content[npos] != "|" + nextword[nchar_count]:
						checkword = True
					nchar_count += 1
					ny -= 1
					npos = x + (ny * row_col_size)
				if checkword:
					continue
				else:
					#insert word
					nchar_count = 0
					while nchar_count < len(nextword):
						pos = x + (y * row_col_size)
						full_content[pos] = "|" + nextword[nchar_count]
						nchar_count += 1
						y -= 1
				tcount += 1
# Get solution
count = 0
solutionstr = ""
while count < len(full_content):
	solutionstr += full_content[count]
	count += 1
# Generate random letter to insert into blank spaces
# Go through full_content list by index and if index has value of "." then replace it with a random letter.
count = 0
letters = string.ascii_uppercase
while count < len(full_content):
	if full_content[count] == "|.":
		full_content[count] = "|" + random.choice(letters)
	count += 1
# Print wordsearch
count = 0
fullstr = ""
while count < len(full_content):
	fullstr += full_content[count]
	count += 1
count = 0
print("+-"*row_col_size+"+")
while count < len(fullstr):
	print(fullstr[count:count+row_col_size*2]+"|")
	count += row_col_size*2
print("+-"*row_col_size+"+")

# Show solution
print()
if input ("Show solution [y/n]: ").lower() == "y":
	print()
	print("Solution:")
	print("=========")
	count = 0
	print("+-"*row_col_size+"+")
	while count < len(solutionstr):
		print(solutionstr[count:count+row_col_size*2]+"|")
		count += row_col_size*2
	print("+-"*row_col_size+"+")

input ("All done. ")
