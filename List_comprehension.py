numbers =[0,1,2,3,4,5]
doubled_numbers =[]

#for number in numbers:
 #   doubled_numbers.append(number *2)

#print(doubled_numbers)

##with list comprehensions
doubled_numbers = [number * 2 for number in numbers ]
print(doubled_numbers)

doubled_numbers = [ 5 for number in range(5)]
print(doubled_numbers)


