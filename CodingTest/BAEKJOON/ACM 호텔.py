T = int(input())
Hotels = tuple( tuple(map(int, input().split())) for i in range(T) )

for Hotel in Hotels:
    Hotel_Rooms = tuple( str(y)+str(x).zfill(2) for x in range(1, Hotel[1]+1) for y in range(1, Hotel[0]+1) )
    print(Hotel_Rooms[Hotel[2]-1])
