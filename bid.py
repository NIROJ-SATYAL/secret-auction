import os
bid={}



end_game=True

while end_game:
    try:
        nam=str(input("enter your name:"))
        prize=int(input("enter your bid:"))
    except ValueError:
        print("enter correct answer according to question")

    bid[nam]=prize
   
    
    want=input("do you want to continue:('yes' or 'no')")
    if want=="no":
        end_game=False
        value=bid.values()
        max=max(value)
        print(f"  maximum bid is {max}")
        print(bid)

    elif want=="yes":
        os.system("clear")
    else:
        print("please enter only 'yes' or 'no'::::")
        


    
