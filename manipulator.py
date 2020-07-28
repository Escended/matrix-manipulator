def main():
    menu()


def multiply_constant():
    print("Enter size of matrix: ", end="")
    ai, aj = matrix_size()
    print("Enter matrix:")
    A = matrix(ai)
    m = float(input("Enter constant: "))
    multi = [[A[i][j] * m for j in range(aj)] for i in range(ai)]
    original = [[A[i][j] * m for j in range(aj)] for i in range(ai)]
    for idx, lst in enumerate(multi):
        for idy, fl in enumerate(lst):
            if fl.is_integer():
                multi[idx][idy] = int(fl)
            elif not fl.is_integer():
                multi = original
                break
        else:
            continue
        break
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
        multiplied = [[sum(A*B for A,B in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
        original = [[sum(A*B for A,B in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
        for idx, lst in enumerate(multiplied):
            for idy, fl in enumerate(lst):
                if fl.is_integer():
                    multiplied[idx][idy] = int(fl)
                elif not fl.is_integer():
                    multiplied = original
                    break
            else:
                continue
            break
        print("The result is:")
        print('\n'.join(" ".join(map(str, row)) for row in multiplied))


def main_diag():
    print("Enter size of matrix: ", end="")
    ai, aj = matrix_size()
    print("Enter matrix:")
    A = matrix(ai)
    m_diag = [[A[j][i]for j in range(aj)] for i in range(ai)]
    original = [[A[j][i] for j in range(aj)] for i in range(ai)]
    for idx, lst in enumerate(m_diag):
        for idy, fl in enumerate(lst):
            if fl.is_integer():
                m_diag[idx][idy] = int(fl)
            elif not fl.is_integer():
                m_diag = original
                break
        else:
            continue
        break
    print("The result is:")
    print('\n'.join(" ".join(map(str, row)) for row in m_diag))


def side_diag():
    print("Enter size of matrix: ", end="")
    ai, aj = matrix_size()
    print("Enter matrix:")
    A = matrix(ai)
    s_diag = [[A[-aj + j][i]for j in reversed(range(aj))] for i in reversed(range(ai))]
    original = [[A[-aj + j][i] for j in reversed(range(aj))] for i in reversed(range(ai))]
    for idx, lst in enumerate(s_diag):
        for idy, fl in enumerate(lst):
            if fl.is_integer():
                s_diag[idx][idy] = int(fl)
            elif not fl.is_integer():
                s_diag = original
                break
        else:
            continue
        break
    print("The result is:")
    print('\n'.join(" ".join(map(str, row)) for row in s_diag))


def v_mirror():
    print("Enter size of matrix: ", end="")
    ai, aj = matrix_size()
    print("Enter matrix:")
    A = matrix(ai)
    v_mirror = [[A[i][j] for j in reversed(range(aj))] for i in range(ai)]
    original = [[A[i][j] for j in reversed(range(aj))] for i in range(ai)]
    for idx, lst in enumerate(v_mirror):
        for idy, fl in enumerate(lst):
            if fl.is_integer():
                v_mirror[idx][idy] = int(fl)
            elif not fl.is_integer():
                v_mirror = original
                break
        else:
            continue
        break
    print("The result is:")
    print('\n'.join(" ".join(map(str, row)) for row in v_mirror))


def h_mirror():
    print("Enter size of matrix: ", end="")
    ai, aj = matrix_size()
    print("Enter matrix:")
    A = matrix(ai)
    h_mirror = [[A[i][j] for j in range(aj)] for i in reversed(range(ai))]
    original = [[A[i][j] for j in range(aj)] for i in reversed(range(ai))]
    for idx, lst in enumerate(h_mirror):
        for idy, fl in enumerate(lst):
            if fl.is_integer():
                h_mirror[idx][idy] = int(fl)
            elif not fl.is_integer():
                h_mirror = original
                break
        else:
            continue
        break
    print("The result is:")
    print('\n'.join(" ".join(map(str, row)) for row in h_mirror))


def add():
    print("Enter size of first matrix: ", end="")
    ai, aj = matrix_size()
    print("Enter first matrix:")
    A = matrix(ai)
    print("Enter size of second matrix: ", end="")
    bi, bj = matrix_size()
    print("Enter first matrix:")
    B = matrix(bi)
    if ai == bi and aj == bj:
        addition = [[A[i][j] + B[i][j] for j in range(aj)] for i in range(ai)]
        original = [[A[i][j] + B[i][j] for j in range(aj)] for i in range(ai)]
        for idx, lst in enumerate(addition):
            for idy, fl in enumerate(lst):
                if fl.is_integer():
                    addition[idx][idy] = int(fl)
                elif not fl.is_integer():
                    addition = original
                    break
            else:
                continue
            break

        print("The result is:")
        print('\n'.join(" ".join(map(str, row)) for row in addition))
        # print('\n'.join(" ".join(str(x) for x in addition)))
    else:
        print("The operation cannot be performed.\n")


def menu():
    option = None
    #transposer = None
    while option != 0:
        print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose matrix\n0. Exit")
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
            side_diag()
        elif option == 6:
            v_mirror()
        elif option == 0:
            option = 0


def matrix_size():
    mi, mj = [int(m) for m in input().split()]
    return mi, mj


def matrix(mi):
    M = [[float(m) for m in input().split()] for m_row in range(mi)]
    return M


main()
