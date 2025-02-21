# file = open('data.txt', 'w')
# file.write('Hello world!')
# file.close()

with open('data.txt', 'a') as file:
    file.write('Hell, world!\n')