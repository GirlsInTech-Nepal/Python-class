
wordsToCount={'is':0,'the':0}
text = open('pg11.txt', 'r').read()



for line in text:

	words=line.split( )
	print(words)
	
	for word in words:
		if  word in wordsToCount:
	
			wordsToCount[word]+=1
print(wordsToCount)
