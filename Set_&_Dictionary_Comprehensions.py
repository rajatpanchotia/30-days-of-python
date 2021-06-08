friends = ["Rajat","Samyak","Yadav"]
guests = ["rajat","samyak","Ron","Harry","Hermonie"]

friends_lower = {n.lower() for n in friends}
guests_lower = {n.lower() for n in guests}

present_friends = friends_lower.intersection(guests_lower)
present_friends = {name.title()  for name in present_friends}

print(present_friends)

friends = ["Rajat","Samyak","Yadav","naini"]
time_since_seen =[3,4,6,9]

long_timers = {
    friends[i]:time_since_seen[i]
    for i in range(len(friends))
    if time_since_seen(i)> 5   
}
print(long_timers)