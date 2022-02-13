import sys

while True:
    N = int(sys.stdin.readline())
    result = 0

    def set_tile(s):
        global result
        
        if len(s) == N:
            result += 1
            
        else:
            for tile in ["1", "00"]:
                if len(s)+len(tile) <= N:
                    set_tile(s + tile)
                    
    set_tile("")
    print( result )
