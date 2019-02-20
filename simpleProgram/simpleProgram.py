#python3 simple

#1 Output
print ('Hello, world!')

#2 Input, assignment
name = input('What is your name?\n')
print ('Hi, %s.' % name)

#3 For loop, built-in enumerate function, new style formatting
friends = ['Tina', 'Able', 'Penda', 'Rose']
for i, name in enumerate(friends):
    print ("iteration {iteration} is {name}".format(iteration=i, name=name))

#4 Fibonacci, tuple assignment
parents, babies = (1, 1)
#parents = 1
#babies  = 1
while babies < 100:
    print ('This generation has {0} parents {1} babies'.format(parents, babies))
    parents, babies = (babies, parents + babies)
    #parents = babies
    #babies = parents + babies

#5 Functions
def greet(name):
    print ('Hello', name)
greet('Jack')
greet('Jill')
greet('Bob')

#6 import, regular expressions
import re
for test_string in ['555-1212', 'ILL-EGAL']:
    #test_string is 3 number + '-' + 4 number
    if re.match(r'^\d{3}-\d{4}$', test_string):
        print (test_string, 'is a valid US local phone number')
    else:
        print (test_string, 'rejected')

#7 Dictionaries, generator expressions
prices = {'apple': 0.40, 'banana': 0.50}
my_purchase = {
        'apple': 1,
        'banana': 6}
grocery_bill = sum(prices[furit] * my_purchase[furit]
        for furit in my_purchase)
#furit is the keyword in my_purchase, prices[furit] use keyword value furit get response value in dictionary prices
print ('I own the grocer $%.2f' % grocery_bill)

