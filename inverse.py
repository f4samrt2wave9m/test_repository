def inverse(matrix):
    def determinant(matrix):
        l = len(matrix)
        u = [0 for r in range(0,l)]  
        d = 1
        def reduct(matrix):
            w = [[0 for j in range(len(matrix[0])-1)] for k in range(len(matrix)-1)]
            for row in range(1,len(matrix[0])):
                for column in range(1,len(matrix)):
                    s = matrix[column][row]-(matrix[column][0]/matrix[0][0])*matrix[0][row]
                    w[column-1][row-1] = s
            return w
        
        def loop(matrix):
            if len(matrix) > 1:
                u[-len(matrix)] = matrix[0][0]
                matrix = reduct(matrix)
            elif len(matrix) == 1:
                u[-1]= matrix[0][0]
            else:
                print("error")
            return matrix
            
        while l > 0:
            matrix = loop(matrix)
            l = l-1
            
        for ele in range(0,len(u)):
            d = d*u[ele]
        return d

    def coef(matrix,row,column):
        u = [[0 for k in range(len(matrix[0])-1)] for l in range(len(matrix)-1)]
        for j in range(0,len(matrix[0])):
            for i in range(0,len(matrix)):
                if   (j < (row-1)) and (i < (column-1)):
                    u[i][j] = matrix[i][j]
                elif (j < (row-1)) and (i > (column-1)):
                    u[i-1][j] = matrix[i][j]
                elif (j > (row-1)) and (i < (column-1)):
                    u[i][j-1] = matrix[i][j]
                elif (j > (row-1)) and (i > (column-1)):
                    u[i-1][j-1] = matrix[i][j]
                else :
                    pass
        return u

    inv=[[0 for i in range(0,len(matrix[0]))]for j in range(0,len(matrix))]   

    for column in range(1,len(inv[0])+1):
        for row in range(1,len(inv)+1):
            inv[row-1][column-1] = ((-1)**(row+column))*determinant(coef(matrix,row,column))/determinant(matrix)
    return inv




def matrix_product(matrix_1,matrix_2):
    t = 0
    w = [[0 for i in range(len(matrix_1[0]))] for j in range(len(matrix_2))]
    for column in range(0,len(matrix_2)):
        for row in range(0,len(matrix_1[0])):
            for i in range(0,len(matrix_2[column])):
                s = matrix_1[i][row]*matrix_2[column][i]
                t += s
            w[column][row] = t
            t = 0 
    return w

def determinant(matrix):
    l = len(matrix)
    u = [0 for r in range(0,l)]  
    d = 1
    def reduct(matrix):
        w = [[0 for j in range(len(matrix[0])-1)] for k in range(len(matrix)-1)]
        for row in range(1,len(matrix[0])):
            for column in range(1,len(matrix)):
                s = matrix[column][row]-(matrix[column][0]/matrix[0][0])*matrix[0][row]
                w[column-1][row-1] = s
        return w
    
    def loop(matrix):
        if len(matrix) > 1:
            u[-len(matrix)] = matrix[0][0]
            matrix = reduct(matrix)
        elif len(matrix) == 1:
            u[-1]= matrix[0][0]
        else:
            print("error")
        return matrix
    
    while l > 0:
        matrix = loop(matrix)
        l = l-1
        
    for ele in range(0,len(u)):
        d = d*u[ele]
    
    return d


A=[[1,2,3,4],[4,1,2,3],[3,4,1,2],[2,3,4,1]]
print("|A|=",determinant(A))
print("A^(-1)=",inverse(A))
print("E=",matrix_product(A,inverse(A)))

