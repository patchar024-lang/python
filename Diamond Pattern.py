rowSize = int(input("Enter the number of rows: "))
if rowSize%2 == 0:
    halfDiamRows = int(rowSize/2)
else:
    halfDiamRows = int((rowSize/2)+1)

    space = halfDiamRows-1
    for i in range(1, halfDiamRows+1):
        for j in range(1, space+1):
            print(" ", end="")
        space = space-1
        num = 1
        for j in range(2*i-1):
            print(end=str(num))
            num = num + 1
        print()
        for i in range(halfDiamRows):
            for j in range(1, space+1):
                print(" ", end="")
                space = space + 1

            
                       
                       
                       

                       