from copy import deepcopy
import numpy as np

def main():
    menu()


def inverse_matrix():
    print("Enter size of matrix: ", end="")
    ai, aj = matrix_size()
    print("Enter matrix:")
    A = matrix(ai)
    try:
        inverse = np.linalg.inv(A)
        print("The result is:")
        print('\n'.join(" ".join(map(str, np.round(row, decimals=4))) for row in inverse))
        print()
    except:
        print("This matrix doesn't have an inverse.")
        print()
    #print(np.round(inverse, decimals=2))



def matrix_n_by_n_determinant(nb_rows, nb_cols, matrix):
    if nb_rows == 1:
        return matrix[0][0]
    if nb_rows == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        determinant = 0
        for i in range(nb_rows):
            minor = [[matrix[_][j] for j in range(nb_cols) if j != i] for _ in range(1, nb_rows)]
            determinant += matrix[0][i] * matrix_n_by_n_determinant(nb_rows - 1, nb_cols - 1, minor) * (-1) ** (
                        1 + i + 1)
        return determinant


def determine():
    print("Enter size of matrix: ", end="")
    ai, aj = matrix_size()
    print("Enter matrix:")
    A = matrix(ai)
    print("The result is:")
    print(matrix_n_by_n_determinant(ai, aj, A))
    print()


def multiply_constant():
    print("Enter size of matrix: ", end="")
    ai, aj = matrix_size()
    print("Enter matrix:")
    A = matrix(ai)
    m = float(input("Enter constant: "))
    multi = [[A[i][j] * m for j in range(aj)] for i in range(ai)]

    print("The result is:")
    print('\n'.join(" ".join(map(str, row)) for row in multi))
    print()


def multiply_matrices():
    print("Enter size of first matrix: ", end="")
    ai, aj = matrix_size()
    print("Enter first matrix:")
    A = matrix(ai)
    print("Enter size of second matrix: ", end="")
    bi, bj = matrix_size()
    print("Enter first matrix:")
    B = matrix(bi)

    if aj == bi:
        multiplied = [[sum(A * B for A, B in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]

        print("The result is:")
        print('\n'.join(" ".join(map(str, row)) for row in multiplied))


def main_diag():
    print("Enter size of matrix: ", end="")
    ai, aj = matrix_size()
    print("Enter matrix:")
    A = matrix(ai)
    m_diag = [[A[j][i] for j in range(aj)] for i in range(ai)]

    print("The result is:")
    print('\n'.join(" ".join(map(str, row)) for row in m_diag))


def side_diag():
    print("Enter size of matrix: ", end="")
    ai, aj = matrix_size()
    print("Enter matrix:")
    A = matrix(ai)
    s_diag = [[A[-aj + j][i] for j in reversed(range(aj))] for i in reversed(range(ai))]

    print("The result is:")
    print('\n'.join(" ".join(map(str, row)) for row in s_diag))


def v_mirror():
    print("Enter size of matrix: ", end="")
    ai, aj = matrix_size()
    print("Enter matrix:")
    A = matrix(ai)
    v_mirror = [[A[i][j] for j in reversed(range(aj))] for i in range(ai)]
    print("The result is:")
    print('\n'.join(" ".join(map(str, row)) for row in v_mirror))


def h_mirror():
    print("Enter size of matrix: ", end="")
    ai, aj = matrix_size()
    print("Enter matrix:")
    A = matrix(ai)
    h_mirror = [[A[i][j] for j in range(aj)] for i in reversed(range(ai))]

    print("The result is:")
    print('\n'.join(" ".join(map(str, row)) for row in h_mirror))


def add():
    print("Enter size of first matrix: ", end="")
    ai, aj = matrix_size()
    print("Enter first matrix:")
    A = matrix(ai)
    print("Enter size of second matrix: ", end="")
    bi, bj = matrix_size()
    print("Enter second matrix:")
    B = matrix(bi)
    if ai == bi and aj == bj:
        addition = [[A[i][j] + B[i][j] for j in range(aj)] for i in range(ai)]
        print("The result is:")
        print('\n'.join(" ".join(map(str, row)) for row in addition))
        # print('\n'.join(" ".join(str(x) for x in addition)))
    else:
        print("The operation cannot be performed.\n")


def menu():
    option = None
    while option != 0:
        print(
            "1. Add matrices\n\
2. Multiply matrix by a constant\n\
3. Multiply matrices\n\
4. Transpose matrix\n\
5. Determinant\n\
6. Inverse Matrix\n\
0. Exit")
        print("Your choice: ", end="")
        option = int(input())
        if option == 1:
            add()
        elif option == 2:
            multiply_constant()
        elif option == 3:
            multiply_matrices()
        elif option == 4:
            print("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
            print("Your choice: ", end="")
            transposer = int(input())
            if transposer == 1:
                main_diag()
            elif transposer == 2:
                side_diag()
            elif transposer == 3:
                v_mirror()
            elif transposer == 4:
                h_mirror()
        elif option == 5:
            determine()
        elif option == 6:
            inverse_matrix()
        elif option == 0:
            option = 0


def matrix_size():
    mi, mj = [int(m) for m in input().split()]
    return mi, mj


def matrix(mi):
    M = [[int(m) if m.isdecimal() else float(m) for m in input().split()] for m_row in range(mi)]
    return M


main()
