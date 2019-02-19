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

