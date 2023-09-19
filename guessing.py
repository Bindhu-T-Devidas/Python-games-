secret_number=0
i=1
while i<4:
    guess1=int(input(f"Guess {i} : "))
    i+=1
    if guess1 == secret_number:
        print("The guess is right!!")
        break
        
else:
    print("Better luck next time")   

