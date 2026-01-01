# List compreshsion
# Divisible by 4 from 0 to 5 :
def diviFour():
    l = [i for i in range(0,51) if i%4 == 0]
    print(l)

diviFour()

# Upper case all the string in a list :
def upper(l1):
    l2 = [i.upper() for i in l1 ]
    print(l2)

l = ['hia','raja','how']
upper(l)

# Print only the string contain 'a' in the list :
def onlya(l):
    l2 = [i for i in l if 'a' in i]
    print(l2)

onlya(l)



# Print the 5*5 matrix
matrix_5x5 = [[0 for j in range(5)] for i in range(5)]
print(matrix_5x5)




