# open file in write mode
file = open('do_now.txt', 'w')

# TODO: create the list 
for n in range (5):
    file.write(input('SPEAK! ') + '\n')
    print(file) 

file.close()
