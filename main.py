import codecs
import re

if __name__ == '__main__':
   f = codecs.open( "text.txt", "r", "utf_8_sig" )
   text = f.read()
   f.close()
   c = text.count('大丈夫')
   print(c)

   fileWords = codecs.open( "words.txt", "r", "utf_8_sig" )
   words = []
   for line in fileWords:
      words.append(line.strip())
   f = codecs.open("result.txt", "w", "utf_8_sig")
   for word in words:
       f.write(word + ': ' + str(text.count(word)) + '\n')

