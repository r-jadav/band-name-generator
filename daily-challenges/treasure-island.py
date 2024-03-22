print('''
                                                      
88                      88 88                         
""                      88 ""                         
                        88                            
88 8b,dPPYba,   ,adPPYb,88 88 ,adPPYYba, 8b,dPPYba,   
88 88P'   `"8a a8"    `Y88 88 ""     `Y8 88P'   `"8a  
88 88       88 8b       88 88 ,adPPPPP88 88       88  
88 88       88 "8a,   ,d88 88 88,    ,88 88       88  
88 88       88  `"8bbdP"Y8 88 `"8bbdP"Y8 88       88  

''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

left_right = input("Where do you want to go? Type \"left\" or \"right\"?\n")
if left_right.lower() == 'left':
    swim_wait = input("Whether you want to swim or wait?\n")
    if swim_wait.lower() == 'wait':
        which_door = input("Which door you would like to choose? Red, Blue or Yellow?\n")
        if which_door.lower() == 'yellow':
            print("You win!")
        else:
            print("Game Over!")
    else:
        print("Game Over!")
else:
    print("Game Over!")