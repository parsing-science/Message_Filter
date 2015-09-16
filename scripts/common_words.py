#!/usr/bin/python
# -*- coding: utf-8 -*-
#common_words.py: most common words in lists
#Nicole Carlson

import MySQLdb as mdb
import sys
import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import stopwords
	

#try:

con = mdb.connect('localhost', 'nicole', 'nicole', 'okc_messages');

with con: 

	cur = con.cursor()

	cur.execute("SELECT * FROM Messages") 

	rows=cur.fetchall()

	spam_words=[]
	not_spam_words=[]

	stop=set(stopwords.words('english'))

	for row in rows:
		message = row[3]

		#NEED TO STRIP OUT PUNCTUATION!!!!

		words=filter(lambda w: not w in stop, message.lower().split())
		num_words=len(words)
		spam=bool(row[6])
		
		if(spam):
			spam_words.extend(words)
		else:
			not_spam_words.extend(words)
cur.close()
con.close()

spam_word_counts=Counter(spam_words)
not_spam_word_counts=Counter(not_spam_words)

print "SPAM"

for word, count in spam_word_counts.most_common(10):
	print word, count

print "NOT SPAM"

for word, count in not_spam_word_counts.most_common(10):
	print word, count

#except:
	#print "Something went wrong or you exited."
