from csv import reader
###   CSV HEADERS
###   word_id,word,up_votes,down_votes,author,definition
###   0000007,Janky,296,255,dc397b2f,"Undesirable; less-than optimum."

class DictItem:
	def __init__(self, word, definition, score):
		self.word = word
		self.definition = definition
		self.definition = definition
		self.score = score


answerlist = []

#answer list will be a list of word objects
with open ('urbandict-word-defs.csv', 'r') as read_obj:
	csv_reader = reader(read_obj)
	for row in csv_reader:
		if len(row[1]) == 5:
			#instantiate DictItem object
			try:
				votescore = int(row[2]) - int(row[3])
			except:
				votescore = '?'
			if votescore == '?' or votescore > 15:
				newword = DictItem(row[1],row[5],votescore)
				answerlist.append(newword)
		else:
			continue

print("Length before dupe cuts:" + str(len(answerlist)))

#cut duplicates
answerlist2 = []
for answer in answerlist:
	if answer.word not in answerlist2:
		answerlist2.append(answer.word)




print("Length after dupe cuts:" + str(len(answerlist2)))

for answer in answerlist2[10:500]:
	print(answer)
