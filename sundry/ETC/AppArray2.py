lucky_numbers = [4, 8, 15, 16, 32, 43]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)  # res: ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby', 4, 8, 15, 16, 32, 43]
friends.append("Martin")  # res: ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby', 4, 8, 15, 16, 32, 43, 'Martin']
friends.insert(1, "Kelly")  # res: ['Kevin', 'Kelly', 'Karen', 'Jim', 'Oscar', 'Toby', 4, 8, 15, 16, 32, 43, 'Martin']

friends.remove("Jim")  # res: ['Kevin', 'Kelly', 'Karen', 'Oscar', 'Toby', 4, 8, 15, 16, 32, 43, 'Martin']

pop = friends.pop()  # res: ['Kevin', 'Kelly', 'Karen', 'Oscar', 'Toby', 4, 8, 15, 16, 32, 43]
print(pop == "Martin")  # res: True

print(friends)

friends2 = friends.copy()  # deep copy
friends2.pop()
print(friends2)


lucky_numbers.sort()  # reference
print(lucky_numbers)

