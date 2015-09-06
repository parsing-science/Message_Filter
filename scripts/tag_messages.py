#!/usr/bin/python
# -*- coding: utf-8 -*-
#tag_messages.py: pull messages one by one from MYSQL table and tag them.
#Nicole Carlson

import MySQLdb as mdb
import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

	

try:
	try:
		print "Start at message: "+sys.argv[1]

		# User must input the number that represents where the messages should start
		start_message=int(sys.argv[1])
	except: 
		print "You need to enter one argument!"

	con = mdb.connect('localhost', 'nicole', 'nicole', 'okc_messages');

	with con: 

		cur = con.cursor()

		cur.execute("SELECT Count(*) FROM Messages") 

		num_messages=int(cur.fetchone()[0])

		print ("The number of messages is: ", num_messages)

		for i in range(start_message, num_messages):

			cur.execute("SELECT Message FROM Messages WHERE ID="+str(i)) 

			row = cur.fetchone()

			print row

			try: 
				spam_label=input('Is this spam? Enter True or False.\n')
				print ("You entered: ", spam_label)

				if(spam_label):
					cur.execute ("""
						  UPDATE Messages
						  SET Spam=%s
						  WHERE ID=%s
						""", (spam_label, str(i)))
					con.commit()
				else:
					pass

			except KeyboardInterrupt: 
				print ("last message: ", i)
				break 

			except: 
				print "Enter True or False."

			try: 
				terrible_label=input('Is this terrible? Enter True or False.\n')
				print ("You entered: ", terrible_label)

				cur.execute ("""
					  UPDATE Messages
					  SET Terrible=%s
					  WHERE ID=%s
					""", (terrible_label, str(i)))
				con.commit()

			except KeyboardInterrupt: 
				print ("last message: ", i)
				break 

			except: 
				print "Enter True or False."
		
		cursor.close()
		con.close()

except:
	print "Something went wrong or you exited."
