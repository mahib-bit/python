number_pad = [[1,2,3],
              [4,5,6],
              [7,8,9],
              ["*",0,"#"]]

#for x in range(4):
#    for y in range (3):
#        print(number_pad[x][y],end = " ")
#    print()

for row in number_pad:
    for num in row:
        print(num, end= " ")
    print()