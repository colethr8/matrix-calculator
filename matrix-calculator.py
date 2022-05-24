import sys

operations = {
    1: "Addition",
    2: "Subtraction",
    3: "Multiplication",
    4: "Reduced Row Echelon Form",
    5: "Transpose",
    6: "Inverse",
    7: "Determinant"
}

def main():
    # Print options
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Reduced Row Echelon Form")
    print("5. Transpose")
    print("6. Inverse")
    print("7. Determinant")

    # Select operation
    while True:
        try:
            op = input("\nSelect an Operation: ")

            if op == "quit" or op == "exit":
                sys.exit()
            else:
                op = int(op)

            break
        except ValueError:
            print("Please input a number 1-" + str(len(operations)))
    
    # Generate first matrix (always guaranteed)
    matrix1_rows = get_num_rows("1")
    matrix1_cols = get_num_cols("1")
    matrix1 = input_matrix(matrix1_rows, matrix1_cols, "1")

    # Perform operations
    match op:
        # Addition
        case 1:
            print("\nMatrix 2 must also be " + str(matrix1_rows) + "x" + str(matrix1_cols))
            matrix2_rows = matrix1_rows
            matrix2_cols = matrix1_cols
            matrix2 = input_matrix(matrix2_rows, matrix2_cols, "2")
            sum = add(matrix1, matrix2)
            print("\nMatrix 1 + Matrix 2:")
            print_matrix(sum)
        # Subtraction
        case 2:
            print("\nMatrix 2 must also be " + str(matrix1_rows) + "x" + str(matrix1_cols))
            matrix2_rows = matrix1_rows
            matrix2_cols = matrix1_cols
            matrix2 = input_matrix(matrix2_rows, matrix2_cols, "2")
            difference = sub(matrix1, matrix2)
            print("\nMatrix 1 - Matrix 2:")
            print_matrix(difference)
        # Multiplication
        case 3:
            print("\nMatrix 2 must also have " + str(matrix1_cols) + " rows")
            matrix2_rows = matrix1_cols
            matrix2_cols = get_num_cols("2")
            matrix2 = input_matrix(matrix2_rows, matrix2_cols, "2")
            product = multiply(matrix1, matrix2)
            print("\nMatrix 1 * Matrix 2:")
            print_matrix(product)
        # RREF
        case 4:
            pass
        # Transpose
        case 5:
            print("\nTranspose Matrix 1:")
            print_matrix(transpose(matrix1))
        # Inverse
        case 6:
            if matrix1_rows != matrix1_cols or det(matrix1) == 0:
                print("\nMatrix is not invertible!")
            else:
                print("\nInverse Matrix 1:")
                print_matrix(invert(matrix1))
        # Determinant
        case 7:
            if matrix1_rows != matrix1_cols:
                print("\nNon-square matrices do not have determinants!")
            else:
                print("\nDeterminant of Matrix 1 = " + str(det(matrix1)))
        case _:
            print("Something went wrong!")
            sys.exit()

def get_num_rows(num):
    while True:
        try:
            matrix1_rows = input("\nNumber of rows in matrix " + num + ": ")

            if matrix1_rows == "quit" or matrix1_rows == "exit":
                sys.exit()
            else:
                matrix1_rows = int(matrix1_rows)
                if matrix1_rows <= 0:
                    raise ValueError
            break
        except ValueError:
            print("Please enter a valid number. Input must be greater than 0.")

    return matrix1_rows

def get_num_cols(num):
    while True:
        try:
            matrix1_cols = input("Number of columns in matrix " + num + ": ")

            if matrix1_cols == "quit" or matrix1_cols == "exit":
                sys.exit()
            else:
                matrix1_cols = int(matrix1_cols)
                if matrix1_cols <= 0:
                    raise ValueError
            break
        except ValueError:
            print("Please enter a valid number. Input must be greater than 0.")

    return matrix1_cols

def input_matrix(rows, cols, num):
    while True:
        try:
            matrix1 = []
            for row in range(rows):
                row_input = input("Enter " + str(cols) + " columns of row " + str(row + 1) + " separated by spaces: ")

                if row_input == "quit" or row_input == "exit":
                    sys.exit()
                else:
                    row_split = row_input.split()
                    if len(row_split) != cols:
                        raise ValueError

                    row = []
                    for val in row_split:
                        row.append(int(val))

                    matrix1.append(row)
            
            print("\nMatrix " + num + ":")
            print_matrix(matrix1)

            while True:
                confirmation = input("Matrix " + num + " Correct? Y/N: ")
                confirmed = False
                try:
                    if confirmation.lower() == "y" or confirmation.lower() == "yes":
                        confirmed = True
                        break
                    elif confirmation.lower() == "n" or confirmation.lower() == "no":
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("Invalid input.")

            if confirmed:
                break
        except ValueError:
            print("Invalid input. Please enter " + str(cols) + " numbers seperated by spaces.")
            print("For example: \"1 2 3 4\"")

    return matrix1

def add(m1, m2):
    rows = len(m1)
    cols = len(m1[0]) 
    sum = []

    for row in range(rows):
        new_row = []
        for col in range(cols):
            new_row.append(m1[row][col] + m2[row][col])
        sum.append(new_row)

    return sum

def sub(m1, m2):
    rows = len(m1)
    cols = len(m1[0])
    diff = []

    for row in range(rows):
        new_row = []
        for col in range(cols):
            new_row.append(m1[row][col] - m2[row][col])
        diff.append(new_row)

    return diff

def multiply(m1, m2):
    product = []

    for row in range(len(m1)):
        new_row = []
        for col in range(len(m2[0])):
            value = 0
            for curr_row in range(len(m2)):
                value += m1[row][curr_row] * m2[curr_row][col]
            new_row.append(value)
        product.append(new_row)

    return product

def rref():
    pass

def reduce_row(m, r):
    pass

def swap_rows(m, r1, r2):
    pass

def transpose(m):
    new_matrix = []

    for col in range(len(m[0])):
        new_row = []
        for row in range(len(m)):
            new_row.append(m[row][col])
        new_matrix.append(new_row)

    return new_matrix

def invert(m):
    pass

def det(m):
    if len(m) == 2:
        ad = m[0][0] * m[1][1]
        bc = m[0][1] * m[1][0]
        return ad - bc
    else:
        return 0

def print_matrix(m):
    # obtained from https://stackoverflow.com/questions/13214809/pretty-print-2d-list
    s = [[str(e) for e in row] for row in m]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))

if __name__ == "__main__":
    print("Matrix Calculator by Cole Thrailkill")
    print("Input \"quit\" or \"exit\" to quit at any time!\n")
    main()