

# RegEx Functions

# The re module offers a set of functions that allows us to search a string for a match:
# Function 	Description
# findall 	Returns a list containing all matches
# search 	Returns a Match object if there is a match anywhere in the string
# split 	Returns a list where the string has been split at each match
# sub 	Replaces one or many matches with a string

                  #### Metacharacters ####
# Character 	Description 	                             Example 	
# [] 	A set of characters 	                            "[a-m]" 	
# \ 	Signals a special sequence  	                    "\d"
#  	    (can also be used to escape special characters)
# . 	Any character (except newline character) 	        "he..o" 	
# ^ 	Starts with 	                                    "^hello" 	
# $ 	Ends with 	                                        "planet$" 	
# * 	Zero or more occurrences 	                        "he.*o" 	
# + 	One or more occurrences 	                        "he.+o" 	
# ? 	Zero or one occurrences 	                        "he.?o" 	
# {} 	Exactly the specified number of occurrences 	    "he.{2}o" 	
# | 	Either or 	                                        "falls|stays" 	
# () 	Capture and group

                ###Flags####
# Flag 	             Shorthand 	Description 	
# re.ASCII 	           re.A 	Returns only ASCII matches 	
# re.DEBUG 		                Returns debug information 	
# re.DOTALL 	        re.S 	Makes the . character match all characters (including newline character) 	
# re.IGNORECASE 	    re.I 	Case-insensitive matching 	
# re.MULTILINE 	        re.M 	Returns matches at the start/end of each line 	
# re.NOFLAG 		            Specifies that no flag is set for this pattern 	
# re.UNICODE 	        re.U 	Returns Unicode matches. This is default from Python 3. For Python 2: use this flag to return only Unicode matches 	
# re.VERBOSE 	        re.X 	Allows whitespaces and comments inside patterns. Makes the pattern more readable

                    ####### Special Sequences #######
# Character 	Description 	                                                                                    Example 	
# \A 	        Returns a match if the specified characters are at the beginning of the string 	                    "\AThe" 	
# \b 	        Returns a match where the specified characters are at the beginning or at the end of a word         r"\bain"
#               (the "r" in the beginning is making sure that the string is being treated as a "raw string")        r"ain\b"            	

# \B 	        Returns a match where the specified chars are prsnt, but NOT at the begng (or at the end) of word   r"\Bain"
#               (the "r" in the beginning is making sure that the string is being treated as a "raw string") 	    r"ain\B"      
    
# \d 	        Returns a match where the string contains digits (numbers from 0-9) 	                             "\d" 	
# \D 	        Returns a match where the string DOES NOT contain digits 	                                         "\D" 	
# \s 	        Returns a match where the string contains a white space character 	                                 "\s" 	
# \S 	        Returns a match where the string DOES NOT contain a white space character 	                         "\S" 	
# \w 	        Returns a match where the string contains any word characters (characters from a to Z, 
#                                               digits from 0-9, and the underscore _ character) 	                 "\w" 	
# \W 	        Returns a match where the string DOES NOT contain any word characters 	                             "\W" 	
# \Z 	        Returns a match if the specified characters are at the end of the string 	                         "Spain\Z"

                    #### SETS ##
# Set 	        Description 	
# [arn] 	    Returns a match where one of the specified characters (a, r, or n) is present 	
# [a-n] 	    Returns a match for any lower case character, alphabetically between a and n 	
# [^arn] 	    Returns a match for any character EXCEPT a, r, and n 	
# [0123] 	    Returns a match where any of the specified digits (0, 1, 2, or 3) are present 	
# [0-9] 	    Returns a match for any digit between 0 and 9 	
# [0-5][0-9] 	Returns a match for any two-digit numbers from 00 and 59 	
# [a-zA-Z]  	Returns a match for any character alphabetically between a and z, lower case OR upper case 	
# [+] 	        In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string

import re

txt = "The rain in Spain"

print("\n Check if the string starts with 'The' and ends with 'Spain'")

x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

print("\n Return a list containing every occurrence of 'ai':")

x = re.findall("ai", txt)
print(x)

print('\n Check if "Portugal" is in the string:')
x = re.findall("Portugal", txt)
print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

print("\n find the position of first found charactor, here white space")
x = re.search(r"\s", txt)

print("The first white-space character is located in position:", x.start())

print("\n search with no match")
x = re.search("Portugal", txt)
print(x)

print('\n Split the string at every white-space character:')

x = re.split(r"\s", txt)
print(x)

print("\n Split the string at the first white-space character:")

x = re.split(r"\s", txt, maxsplit=1)
print(x)

print("\n Sub()")
print('Replace all white-space characters with the digit "9":')

x = re.sub(r"\s", "9", txt)
print(x)
print('Replace the first two occurrences of a white-space character with the digit 9:')

x = re.sub(r"\s", "9", txt, count=2)
print(x)

print("\nThe search() function returns a Match object:")

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)

print('\nSearch for an upper case "S" character in the beginning of a word, and print its position:')
# starting position included and final position excluded 

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

print("\nThe string property returns the search string:")

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

print('\nSearch for an upper case "S" character in the beginning of a word, and print the word:')

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())