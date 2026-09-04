def match_words(words):
   ctr = 0 
   lst = []
   for word in words:
     if len(word) > 1 and word[0] == word[-1]:
        ctr += 1
        lst.append(word)
   print("List of words with the first and last character the same:", lst)
   return ctr, lst

count = match_words(['bob', 'blank', 'abc', '9999'])

