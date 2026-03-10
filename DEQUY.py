A = [0,4,0,1,2,3,8,9,0,1,2,3,17,-16,0,1,2]
P = [1,2,3]
def timMau(A,P):
    n = len(A)
    status = False
    for i in range(n - 2):
        if A[i] == P[0] and A[i+1] == P[1] and A[i+2] == P[2]:
            print("Tìm thấy mẫu tại vị trí: ", i)
            status = True
            break
    if not status:
        print("Không tìm thấy mẫu")

timMau(A,P)
