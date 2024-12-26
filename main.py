import sys
correct = "London"
counter = 0
while counter != 5:
    answer = input("What is the capital of England")
    if correct == answer:
        print("Correct")
        sys.exit()
    else:
        print("incorrect")
        counter = counter + 1
    if counter == 5:
        print("You are out of attempts")