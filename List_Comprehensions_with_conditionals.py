##ages = [21 ,34,39,56,89,78]
##odds = [age for age in ages if  age % 2 == 1 ]
##print(odds)


friends = ["Rajat","Samyak","Yadav"]
guests = ["rajat","samyak","Ron","Harry","Hermonie"]

friends_lower = set([f.lower() for f in friends])
guests_lower = set([g.lower() for g in guests])

print(friends_lower.intersection(guests_lower))

present_friends = [
    name.title() for name in guests if name.lower() in friends_lower
]
print(present_friends)


