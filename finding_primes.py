while True:
	p=int(input('Primes below:'))
	x=range(1,p+1)
	for i in x:
		b=[]
		m=0
		for j in x:
			if i/j in x:
				b.insert(m,j)
				m=m+1
			else:
				continue
		if len(b)==2:
			print(i)
		else:
			continue