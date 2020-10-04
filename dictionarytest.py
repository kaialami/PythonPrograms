def relation_to_luke(name):
	dic = {
	'Darth Vader' : 'father',
		'Leia' : 'sister',
		'Han' : 'brother in law',
		'R2D2' : 'droid',
	}
	
	return 'Luke, I am your ' + dic.get(name) + '.'

print(relation_to_luke('Leia')) 