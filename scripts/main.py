#!/usr/bin/python
# -*- coding: utf-8 -*-
#main.py: loads in okc messages to MYSQL table
#Nicole Carlson

import csv
import MySQLdb as mdb

con = mdb.connect('localhost', 'nicole', 'nicole', 'okc_messages');


# Headers: timestamp|username|message|match_percentage|enemy_percentage
f = open("../data/okcmessages.csv", 'rU')
try:
  reader = csv.DictReader(f, delimiter='|', quotechar='"')

  # List structure for all of the messages
  messages=[];
  
  for row in reader:
  	row.update({"tags": []})
  	messages.append(row)

  #print messages[0]
finally:
  f.close()

with con:
    
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS Messages")
	cur.execute("CREATE TABLE Messages(Id INT PRIMARY KEY AUTO_INCREMENT, \
							Time Timestamp, \
	            Username VARCHAR(25), \
	            Message TEXT, \
	            Match_Percentage INT, \
	            Enemy_Percentage INT, \
	            Spam BOOL, \
	            Short BOOl \
	            )")

	for item in messages:
		temp_timestamp=item["timestamp"]
		temp_username=item["username"]
		temp_message=item["message"]
		temp_match=item["match_percentage"]
		temp_enemy=item["enemy_percentage"]
		temp_short=False

		# Count number of characters in message. If message is fewer than 50 characters, Short boolean is set to true.
		if len(temp_message) < 50:
			item["tags"].append("short")
			temp_short=True

		# # If low match percentage, tag as low_match.
		# if item["match_percentage"] < 40:
		# 	item["tags"].append("low_match")

		# # If high enemy percentage, tag as high_enemy
		# if item["enemy_percentage"] < 50:
		# 	item["tags"].append("high_enemy")


		cur.execute ("""
          	INSERT INTO Messages(Time, Username, Message, Match_Percentage, Enemy_Percentage, Spam, Short)
          	VALUES
              	(%s, %s, %s, %s, %s, %s, %s)

      	""", (temp_timestamp, temp_username, temp_message, temp_match, temp_enemy, False, temp_short))