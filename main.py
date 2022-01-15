import random

def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

# chr function return the letter corresponding to a ASCII value
# random.randint return a random numeric value between the 2 parameters given

#2 uppercase letters from A to Z
uppercaseLetter1=chr(random.randint(65,90))
uppercaseLetter2=chr(random.randint(65,90))

#2 lowercase letters from a to z
lowercaseLetter1=chr(random.randint(97,122))
lowercaseLetter2=chr(random.randint(97,122))
#2 digits from 0 to 9,
digits1=chr(random.randint(48,57))
digits2=chr(random.randint(48,57))
#2 punctuation signs such as !, ?, “,
punctuation1=chr(random.randint(58,64))
punctuation2=chr(random.randint(58,64))

password=uppercaseLetter1+uppercaseLetter2+lowercaseLetter1+lowercaseLetter2+digits1+digits2+punctuation1+punctuation2

#Shuffle the several parts of the passwords
password=shuffle(password)

print(shuffle(password))
