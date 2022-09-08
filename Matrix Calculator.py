mat1=[]
mat2=[]
result=[]
ans=[]
rows=0

def input_mat():            #inputs 1 matrix
    x=True
    while x:
        matrix=list()
        for col in range( 1, rows+1):
            print ("Enter values for row", col, "separated by commas: ", end ="")
            values = input ()
            lvalues=values.split(',')
            if len(lvalues)!= rows:
                print()
                print ("Enter the same number of values as of the no. of rows")
                print()
                matrix.clear()
                break
            else:
                matrix.append(lvalues)
            if col==rows:
                x=False
    return matrix

def add_mat():  #addition func
    for i in range(rows):
        for j in range (rows):
            result[i][j]=int(mat1[i][j]) + int(mat2[i][j])
    return result

def sub_mat():    #subtraction func
    for i in range(rows):
        for j in range (rows):
            result[i][j]=int(mat1[i][j]) - int(mat2[i][j])
    return result

def mult_mat():       #multiplication func
    for i in range(len(mat1)):
        for j in range (len(mat2[0])):
          for k in range(len(mat2)):
              result[i][j]+= int(mat1[i][k])*int(mat2[k][j])
    return result

def print_mat(lst):             #print func for matrix form
    for i in lst:
        for j in i:
            print (j, end=" ")
        print ()
        
menu = {2:add_mat(),3:sub_mat(),4:mult_mat()}       

print ("*" *10, "OPERATIONS MENU", "*"*10)      #only printed once
print("""Please choose the desired operand from the given menu:
        1. Enter a pair of matrices
        2. Add
        3. Subtract
        4. Multiply
        5. Exit
        """)

while True:         #main loop starts
    c=input("Choose operand number: ")
    print()
    if not c.isdigit() or (int(c)>5) or (int(c)<1):
        print ("""Please choose a correct operand number. 
Also note that choosing 5 will end the program :)
""")
    else:
        choice=int(c)
        if choice ==1:          #matrix input
            y=  True
            while y:            #check for rows
                r=(input("Enter the no. of rows for square matrix: "))
                if not r.isdigit() or (int(r)>5) or (int(r)<0):
                    print ("""Please enter a correct value for the number of rows.
Also note that the number of rows can not exceed 5 or go below 0. :)
""")
                else:
                    rows=int(r)
                    y= False
            for i in range (1,3):           #2 inputs
                print()
                print("ENTER VALUES FOR MATRIX NO.", i)
                print()
                matrix=input_mat()
                if i ==1:
                    mat1=matrix
                if i ==2:
                    mat2=matrix
            print()
            print("The first matrix is: ")
            print_mat(mat1)
            print()
            print("The second matrix is: ")
            print_mat(mat2)
            print()
            if rows==1:             #null matrix to calculate result
                result=[[0],[0]]
            elif rows==2:
                result=[[0,0],[0,0]]
            elif rows==3:
                result=[[0,0,0],[0,0,0],[0,0,0]]
            elif rows==4:
                result=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
            elif rows ==5:
                result=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        elif choice==2:
            ans=add_mat()
            print ("The added matrix is: ")
            print_mat(ans)
            print()
        elif choice == 3:
            ans=sub_mat()
            print ("The subtracted matrix is: ")
            print_mat(ans)
            print()
        elif choice == 4:
            ans=mult_mat()
            print ("The multiplied matrix is: ")
            print_mat(ans)
            print()
        elif choice==5:
            print ("Hope I was of help. \nHave a good day!")
            break                   #main loop breaks
          
