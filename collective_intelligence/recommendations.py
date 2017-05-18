#create critics library contain critic, movie and rating
critics = {
	'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5, 
		'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 
		'The Night Listener': 3.0}, 
	'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 
		'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
		'You, Me and Dupree': 3.5},
	'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0, 
		'Superman Returns': 3.5, 'The Night Listener': 3.0},
	'Claudia Puig': {'Snakes on a Plane': 3.5, 'The Night Listener': 4.5,
		'Just My Luck': 3.0, 'Superman Returns': 4.0, 'You, Me and Dupree': 2.5}, 
	'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 
		'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0, 
		'You, Me and Dupree': 2.5},
	'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 
		'Superman Returns': 5.0, 'You, Me and Dupree': 3.5, 
		'The Night Listener': 3.0},
	'Toby': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0, 
		'Superman Returns': 4.0}, 
		}

#print(critics['Lisa Rose']['Lady in the Water'])
#print(critics['Toby'])



'''
Euclidean distance - calculates similarity score based on how closely 
critics' scores match, distance between scores, 1 is 100%--perfect correlation
'''

from math import sqrt;
def sim_distance(prefs, person1, person2):  #define sim_distance function that takes parameters prefs, person1 and person2
	si = {} 								#create an empty dictionary to hold shared item, si
	for item in prefs[person1]:  			#create for loop to iterate through items in person 1 prefs
		if item in prefs[person2]: 			#if item also found in person 2
			si[item] = 1; 					#then add '1' to shared item, si dictionary

	if len(si) == 0:						#if there are no shared items, if 'si' dict is empty, then return 0
		return 0;

	sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2) for item in si])
	return 1/(1+sqrt(sum_of_squares))

#print(sim_distance(critics, 'Lisa Rose', 'Gene Seymour'))  #call sim_distance function and pass parameters critics as prefs, 'Lisa Rose' as person1, 'Gene Seymoure' as person2


#################
#Pearson coefficient--how well scores between people correlate. Can be between -1 to 1

def sim_pearson(prefs, p1, p2):
	si = {};
	for item in prefs[p1]:
		if item in prefs[p2]:
			si[item] = 1;

	n = len(si)

	if n == 0:
		return 0;

	#add the preferences for each person
	sum1 = sum([prefs[p1][it] for it in si])
	sum2 = sum([prefs[p2][it] for it in si])

	#Sum up the squares
	sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
	sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])

	#Sum up the products
	pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

	#Calcuate Pearson score
	num = pSum - (sum1 * sum2 / n)
	den = sqrt((sum1Sq - pow(sum1, 2) / n ) * (sum2Sq - pow(sum2, 2 ) / n ))

	r = num / den
	return r

#print(sim_pearson(critics, 'Lisa Rose', 'Gene Seymour')


##############
#score everyone against a given person, e.g. which movie critics have same tastes as mine


def topMatches(prefs, person1, n = 5, similarity = sim_pearson):
	scores = [(similarity(prefs, person1, person2), person2) for person2 in prefs if person2 != person1]
	scores.sort()
	scores.reverse()
	return scores[0:n]
     
#print(topMatches(critics, 'Toby', n = 3))


#######################
#provides a ranked list of movies with guess of what 'Toby' ratings might be

def getRecommendations(prefs, person, similarity = sim_pearson):
	totals = {}
	simSums = {}
	for other in prefs:
		if other == person: 
			continue
		
		sim = similarity(prefs, person, other)
		if sim <= 0: 
			continue
		
		#only score movies I haven't seen yet
		for item in prefs[other]:
			if item not in prefs[person] or prefs[person][item] == 0:
				totals.setdefault(item, 0)
				totals[item] += prefs[other][item] * sim

				simSums.setdefault(item, 0)
				simSums[item] += sim

		rankings = [(totals / simSums[item], item) for item, totals in totals.items()]

		rankings.sort()
		rankings.reverse()
		return rankings


'''print(getRecommendations(critics, 'Toby'))
print('\n')
print(getRecommendations(critics, 'Toby', similarity = sim_distance))
'''

#look at similarities between items

def transformPrefs(prefs): 
	result = {}
	for person in prefs:
		for item in prefs[person]:
			result.setdefault(item, {})
			result[item][person] = prefs[person][item]
	return result

movies = transformPrefs(critics)
print(movies)
print('\n')
print(topMatches(movies, 'Superman Returns'))

'''

d = {'small': 2, 'medium': 5, 'large': 10}

print(d.items())
print(d.values())
print(d.keys())   

''' 




