
friends = ["Rolf", "John", "Anna"]

for counter, friend in enumerate(friends, start=1):
	print(counter, friend)

friends = ["Rolf", "John", "Anna"]
friends_dict = dict(enumerate(friends))  # {0: 'Rolf', 1: 'John', 2: 'Anna'}