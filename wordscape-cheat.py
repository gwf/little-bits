
import re, sys

###############################################################################

def decode(code):
  word = []
  even = True
  for c in code:
    if even: word.append(c)
    even = not even
  return ''.join(word)

###############################################################################

def encode(word):
  chars = {}
  code = []
  for char in word:
    chars[char] = chars.get(char, 0) + 1
    code.append(char + str(chars[char]))
  return ''.join(code)

###############################################################################

def build_regex(word):
  chars = {}
  code = []
  for char in word:
    chars[char] = chars.get(char, 0) + 1
    code.append(char + str(chars[char]))
  return re.compile('^((' + '|'.join(code) + '){3,})$', re.M)

###############################################################################

def build_data():
  allWords = []
  infile = open("/usr/share/dict/words")
  for word in infile:
    code = encode(word.strip())
    allWords.append(code)
  return '\n'.join(allWords)

###############################################################################

def main():
  allWords = build_data()
  emptyInput = 0
  while True:
    print('query> ', end='', flush=True)
    query = sys.stdin.readline().strip()

    if query == '':
      emptyInput += 1
      if emptyInput > 2: break
      continue
    emptyInput = 0

    regex = build_regex(query)
    match = regex.findall(allWords)
    for hit in match:
      print(decode(hit[0]))
    print()

###############################################################################

main()

