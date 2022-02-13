import sys

N = int(sys.stdin.readline())
Books = {None:0}
Best_Seller = None

for n in range(N):
    book = sys.stdin.readline().rstrip()
    if book not in Books:
        Books[book] = 0
    Books[book] += 1
    if Books[book] > Books[Best_Seller]:
        Best_Seller = book
    elif Books[book] == Books[Best_Seller]:
        Best_Seller = sorted([book, Best_Seller])[0]

print(Best_Seller)
