test_cases=int(input())
for i in range(test_cases):
    clss_id=input()
    clss_id1=clss_id.upper()
    if clss_id1=="B":
        print("Battleship")
    elif clss_id1=="C":
        print("Cruiser")
    elif clss_id1=="D":
        print("Destroyer")
    elif clss_id1=="F":
        print("Frigate")
    else:
        print("type b or c or d or f")
    
        
