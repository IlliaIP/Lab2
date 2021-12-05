import numpy as np

with open('2.txt') as fd:
    for n, line in enumerate(fd):
        if n == 0:
            A = line.strip()
        elif n == 1:
            B = line.strip()
        elif n == 2:
            C = line.strip()
fd.close()

A = A.split(' ')
B = B.split(' ')
C = C.split(' ')

A = [float(i) for i in A]
B = [float(i) for i in B]
C = [float(i) for i in C]

i_A = 5 * A[1]
w_A = 5 * A[3]
win_A = i_A * A[2] + w_A * A[4] - A[0]
print("Results for stratege A for 5 years:")
print("  |\tM1\t | \t D1\t |  P1  | \tD2\t | \tP2\t  | \tincome\t| \twaste\t| win\t")
print("----------------------------------------------------------------------------")
print("A |", end=" "),
print(*A, sep='|\t', end =" "),
print(" | %4.2f \t| %3.2f \t| %3.2f \t" %(i_A, w_A, win_A))
print()

i_B = 5 * B[1]
w_B = 5 * B[3]
win_B = i_B * B[2] + w_B * B[4] - B[0]
print("Results for stratege B for 5 years:")
print("  |\tM2\t | \t D1\t |  P1  | \tD2\t | \tP2\t  | income\t| \twaste\t| win\t")
print("----------------------------------------------------------------------------")
print("B |", end=" "),
print(*B, sep='|\t', end =" "),
print(" | %4.2f \t| %3.2f \t| %3.2f \t" %(i_B, w_B, win_B))
print()

i_A1 = 4 * A[1]
w_A1 = 4 * A[3]
win_A1 = i_A1 * C[2] + w_A1 * C[3] - A[0]
A1 = np.copy(A)
A1[2] = C[2]
A1[4] = C[3]
print("Results for stratege A for 4 years:")
print("  |\tM1\t | \t D1\t |  P1  | \tD2\t | \tP2\t  | \tincome\t| \twaste\t| win\t")
print("----------------------------------------------------------------------------")
print("A |", end=" "),
print(*A1, sep='|\t', end =" "),
print(" | %4.2f \t| %3.2f \t| %3.2f \t" %(i_A1, w_A1, win_A1))
print()

i_B1 = 4 * B[1]
w_B1 = 4 * B[3]
win_B1 = i_B1 * C[2] + w_B1 * C[3] - B[0]
B1 = np.copy(B)
B1[2] = C[2]
B1[4] = C[3]
print("Results for stratege B for 4 years:")
print("  |\tM2\t | \t D1\t |  P1  | \tD2\t | \tP2\t  | income\t| \twaste\t| win\t")
print("----------------------------------------------------------------------------")
print("B |", end=" "),
print(*B1, sep='|\t', end =" "),
print(" | %4.2f \t| %3.2f \t| %3.2f \t" %(i_B1, w_B1, win_B1))
print()


if win_A1 > win_B1:
    win_С1 = win_A1
else:
    win_С1 = win_B1    

win_С_1 = C[0] * win_С1
win_С_2 = C[1] * 0

if win_С_1 > win_С_2:
    win_C = win_С_1
else:
    win_C = win_С_2
print("Results for stratege C for 5 years:")
print("  |\tP3  \t|\t P4 |\t win A1 |\t win B1 |\t win C1 | win C2|\t win C")
print("----------------------------------------------------------------------------")
print("C | %4.2f \t| %4.2f \t| %4.2f \t| %4.2f \t| %4.2f \t| %4.2f \t| %4.2f \t"
      %(C[0], C[1], win_A1, win_B1, win_С_1, win_С_2, win_C))
print()

win_st = max(win_A, win_B, win_C)
if win_st == win_A:
    print('Win strategy is A, because of average expected win is ', win_st)
    print('It is better to build a large plant')
elif win_st == win_B:
    print('Win strategy is B, because of average expected win is ', win_st)
    print('It is better to build a mini plant')
elif win_st == win_C:
    print('Win strategy is C, because of average expected win is ', win_st)
    print('It is better to postpone construction')