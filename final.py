import time
import sys


# Here are some handy constants for recognizing your locations.
Room_HW_F1 = "First Floor Hallway"
Room_PR_F1 = "First Floor Patient Room"
Room_BR_F1 = "First Floor Bathroom"
Room_SC_F1 = "First Floor Staircase"
Room_HW_F2 = "Second Floor Hallway"
Room_PR_F2 = "Second Floor Patient Room"
Room_BR_F2 = "Second Floor Bathroom"
Room_SC_F2 = "Second Floor Staircase"
Room_HW_F3 = "Third Floor Hallway"
Room_PR_F3 = "Third Floor Patient Room"
Room_BR_F3 = "Third Floor Bathroom"
Room_SC_F3 = "Third Floor Staircase"

Start_Room = "You wake up and you are in a dark and gloomy room. \nIt looks as though someone was just in there. You start to feel uneasy and you sit up. \nYou get up and leave the room. You walk to the doorway and you see a staircase and a bathroom. Where will you be going? "
Hallway_F1 = "You are in the hallway. It is dim and all you can see is a figure."
Patient_Room_F1 = "You are in the patient room."
Bathroom_F1 = "You are in the bathroom."
Staircase_F1 = "You are in the staircase."
Hallway_F2 = "You are in the hallway."
Patient_Room_F2 = "You are in the patient room."
Bathroom_F2 = "You are in the bathroom."
Staircase_F2 = "You are in the staircase."
Hallway_F3 = "You are in the hallway."
Patient_Room_F3 = "You are in the patient room."
Bathroom_F3 = "You are in the bathroom."
Staircase_F3 = "You are in the staircase."

won = False
location = Start_Room
door_open = False
get_key = False

#def timer():
#   seconds = 60
#   for i in range(seconds):
#     r = seconds - i
#     t.sleep(1)    
#     #print (r)    
#     if r == 30:        
#       print ("You have " + str(r) + " seconds left")
#     if r == 10:        
#       print ("You have " + str(r) + " seconds left")
#     if r == 1:
#       print("Game Over!!")
    
def time_convert(sec) :
  mins = sec // 60
  sec = sec % 60 
  hours = mins // 60
  mins = mins % 60
  return "Time lapsed = {0} hour(s): {1} minute(s) : {2} seconds".format(int(hours),int(round(mins,2)),round(sec,2))

input("Press Enter to start")
start_time = time.time()
timeout = time.time() + 60*1
count = 0

print(Start_Room)

while count <= 10 or time.time() < timeout:
    command = input("> ")
    print(count)
    
    if command == "quit":
      end_time = time.time()
      time_lapsed = end_time - start_time
      print(time_convert(time_lapsed))
      break

    if location == Start_Room:
        if command == "bathroom":
            count += 1
            location = Bathroom_F3
        elif command == "staircase":
            count += 1
            location = Staircase_F3
            print("The floor is damp and the light bulb is flickering. You hear steps below you because you are on the third floor.\nDo you want to run back to the patient room, continue down the staircase, run into the hallway, or hide in the bathroom? Pick a location.")
        else:
            print("Choose the bathroom or the staircase")
    
    elif location == Staircase_F3:
        if command == "hallway":
            count += 1
            location = Hallway_F2
            print("The floor is composed of black tile. It is smeared in blood and you hear a scream come from the bathroom.\nThere are also 3 nurses talking in the patient room you started in.\nAre you going to help the person in the bathroom or ask the nurses in the patient room about why you were admitted to an asylum? Pick a location.")
        elif command == "bathroom":
            count += 1
            location = Bathroom_F3
            print("The bathroom is pitch dark and a little girl is standing by the window. She is holding a teddy bear and counting the floor tiles. You do not want to disturb her, so you leave the bathroom. You can either go to the patient room or the hallway. Pick a location.")
            
            
    elif location == Hallway_F2:
        if command == "bathroom":
            count += 1
            location = Bathroom_F2
            print("In the bathroom there is a little girl in a white dress facing away from the door. She slowly turns around with her head down and says, 'Have you seen my mommy?'. \n You quickly run out the bathroom and into the hallway. Do you want to run to the patient room for help from the 3 nurses or to the first floor hallway? Pick a location.")
        
        # elif command == "hallway":
        #     location = Hallway_F2
        #     print("The little girl from the bathroom guides you to the first floor. You decide to follow her because she must know the way out. Type 'first floor' to follow her.")

        elif command == "patient room":
            count += 1
            location = Patient_Room_F2
            print("You walk into the patient room and the three nurses are in a frenzy. They have a lady on the bed bleeding out crying for her daughter. You look around trying to help. The nurses tell you to go to the hallway on the first floor and get a gauze. Type first floor to rush out the room and go to the first floor hallway")
        

                
    elif location == Bathroom_F2:
        if command == "first floor" or "hallway":
            count += 1
            location = Hallway_F1
            print("There is a lady that seems harmless. She is wearing pearls and looks like she does not belong here. We are in the same boat. You approach her to ask why she is here and she grabs your shoulders and tells you to escape and she starts running. You want to escape with the lady, but she starts to morphe into a hideous creature. Her eyes start to turn white. Her hair starts to turn orange and her nails start to form claws. She smirks at you and tells you that you have 4 moves to escape the asylum before she finds you.")
            
    
        elif command == "patient room":
            count += 1
            location = Patient_Room_F2
            print("You walk into the patient room and the three nurses are in a frenzy. They have a lady on the bed bleeding out crying for her daughter. You look around trying to help. The nurses tell you to go to the hallway on the first floor and get a gauze.Type first floor, to rush out the room and go to the first floor hallway.")
                
    elif location == Patient_Room_F2:
        if command == "first floor":
            count += 1
            location == Hallway_F1
            print("There is a lady that seems harmless. She is wearing pearls and looks like she does not belong here. We are in the same boat. You approach her to ask why she is here and she grabs your shoulders and tells you to escape and she starts running. You want to escape with the lady, but she starts to morphe into a hideous creature. Her eyes start to turn white. Her hair starts to turn orange and her nails start to form claws. She smirks at you and tells you that you have 4 moves to escape the asylum before she finds you.")
        else:
            print("Type first floor")
                
    elif location == Hallway_F1:
        if command == "patient room":
            count += 1
            location = Hallway_F1
            print("There is a lady that seems harmless. She is wearing pearls and looks like she does not belong here. We are in the same boat. You approach her to ask why she is here and she grabs your shoulders and tells you to escape and she starts running. You want to escape with the lady, but she starts to morphe into a hideous creature. Her eyes start to turn white. Her hair starts to turn orange and her nails start to form claws. She smirks at you and tells you that you have 4 moves to escape the asylum before she finds you.")
           

    if won:
        print ("You've escaped :)")
        end_time = time.time()
        time_lapsed = end_time - start_time
        print(time_convert(time_lapsed))
        break
    elif count == 10:
        end_time = time.time()
        time_lapsed = end_time - start_time
        print(time_convert(time_lapsed))
        print('Looks like you ran out of moves!')
        break
    elif time.time() >= timeout:
        end_time = time.time()
        time_lapsed = end_time - start_time
        print(time_convert(time_lapsed))
        print('Looks like you ran out of time!')
        break
