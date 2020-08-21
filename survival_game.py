print("welcome to the SUICIDE game")
name = input("What is your name? ")
age = int(input("What is your age? "))
print("Hello", name, "you are", age,"years old")

health = 10

if age >= 12:
  print("You are old enough to play !")
  wants_to_play = input("Do you want to play? ").upper()
  if wants_to_play == "YES" or wants_to_play=="Y":
   print("You are starting with", health,"% health")
   print("Let's Play!!")
   

   left_or_right = input("First choice...Left or Right(left/right)? ")
   if left_or_right == "right":
        ans = input("Nice, you follow the path and reach a lake...Do you swim or take a boat(swim/boat)? ")

        if ans == "boat":
            print("You took the boat and reached the other side of the lake")

        elif ans == "swim":
            print("You were bit by a human eating fish...Lost 5% health")
            health -= 5
        ans = input("You noticed a house and a river. Which do you go to(river/house)?")
        if ans == "house":
            print("You go to the house and you are greeted by the owner who doen't like you and hurts you...Lost 5 health")
            health -= 5
            
            if health <= 0:
                print("You now have 0 health and you LOST the game.....")
            else:
                print("CONGRATULATIONS,You have survived")


        else:
            print("You fell into the river and lost")

        

   else:
     print("You fell down a cliff and died....LOST")

  else:
    print("Bye bye...come back soon")
else:
  print("You are not old enough to play...")
