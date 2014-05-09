for article in myQuery:
	myChunk = pull(start = article
	, number = 200
	)
	a = 1
	for article in myChunk:
		for keyword in article.keywords:
			print '\n'.join([keyword])