#!/usr/bin/python
# -*- coding: utf-8 -*-
#view_messages.py: pull messages from MYSQL table and visualize them
#Nicole Carlson

import MySQLdb as mdb
import sys
import matplotlib.pyplot as plt
	

#try:

con = mdb.connect('localhost', 'nicole', 'nicole', 'okc_messages');

with con: 

	cur = con.cursor()

	cur.execute("SELECT * FROM Messages") 

	rows=cur.fetchall()

	spam_x=[]
	spam_y=[]
	not_spam_x=[]
	not_spam_y=[]

	for row in rows:
		message = row[3]
		words=message.split()
		num_words=len(words)
		#print words
		match_p=int(row[4])
		enemy_p=int(row[5])
		spam=bool(row[6])
		if(spam):
			spam_x.append(match_p)
			spam_y.append(num_words)
		else:
			not_spam_x.append(match_p)
			not_spam_y.append(num_words)
	
cur.close()
con.close()

fig=plt.figure()
ax1=fig.add_subplot(111)

ax1.scatter(spam_x, spam_y, s=10, c='b', marker="x", label='spam')
ax1.scatter(not_spam_x,not_spam_y, s=10, c='r', marker="o", label='not spam')
plt.legend(loc='upper right');
plt.ylabel("Number of words")
plt.xlabel("Match Percentage")
plt.xlim([-10, 100])
plt.show()


#except:
	#print "Something went wrong or you exited."
