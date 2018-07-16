# Example 1
squares = {1:1, 2:4, 3:9, 4:16, 5:25}  
print(squares.pop(4))  
del squares[5]  
squares.clear()
del squares

#Example 2
my_dict = {'name':'Jack', 'age': 26}
my_dict['age'] = 27
my_dict['address'] = 'Downtown'
print(my_dict.get('age'))

#Ex 3
#fromkeys(seq,[,v]) Return a new dictionary with keys from seq and value equal to v (defaults to None).
#items() returns new view of (key, value)
marks = {}.fromkeys(['Math','English','Science'], 0)

for item in marks.items():
    print(item)

# Output: ['English', 'Math', 'Science']
list(sorted(marks.keys()))

#other Functions
#keys(), pop(key,[,d]), values(), 

#Python Dictionary Comprehension
squares = {x: x*x for x in range(6)}
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares)

odd_squares = {x: x*x for x in range(11) if x%2 == 1}
# Output: {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
print(odd_squares)

#Membership test for keys only and not value. for ex
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
# Output: True
print(1 in squares)
