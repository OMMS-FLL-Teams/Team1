# Team 1 Robot menu
#
# menu revision number
menu_revision="46"
#
from pybricks.tools import wait, run_task, hub_menu
import robot_library_rev33 as RL

#
# this is the list of tasks and the main function for each task
# add more as needed. tasks usually consist of 1 or more missions
#
# The name of the task file minus the .py file extension

from ue_t1_rev11 import T1_Run
from ue_t2a_rev23 import T2_Run
from ue_t3_rev31 import T3_Run
from ue_t4_rev25 import T4_Run
from ue_t5_rev14 import T5_Run
from ue_t6_rev1 import T6_Run

#
# start delay (in ms) for missions
#
StartDelay=500


#
# clear pybricks console
#
RL.clearConsole()

print("Robot Menu, rev#",menu_revision)

# uncomment following if you want to enter the hub number manually
#hubNum=input("Enter Hub Number: ")
#initiatizeRobot(int(hubNum))

# 0 = CoachHub
# 1 = T1PrimaryHub
# 2 = T1SecondaryHub
#
# Set your hub number!
HubNum=1
if HubNum == -2:
    print("ERROR, hub number=",HubNum," is not valid, pick a valid hub number in the menu!")
RL.initiatizeRobot(HubNum)


# Based on the selection, run a task .
print("Running Menu")

while True:
    #
    #  addd menu numbers/letts for your messions then update the "if" block below for the new mission
    #
    selected = hub_menu("M","1","2","3","4","5","6","X")

    try:
        if selected == "M":
            # does nothing. used to show menu is active
            break
        if selected == "1":
            wait(StartDelay)
            run_task(T1_Run())
            run_task(RL.stopEverything())
        elif selected == "2":
            wait(StartDelay)
            run_task(T2_Run())  
            run_task(RL.stopEverything())
        elif selected == "3":
            wait(StartDelay)
            run_task(T3_Run())  
            run_task(RL.stopEverything())
        elif selected == "4":
            wait(StartDelay)
            run_task(T4_Run())  
            run_task(RL.stopEverything())
        elif selected == "5":
            wait(StartDelay)
            run_task(T5_Run())  
            run_task(RL.stopEverything())            
        elif selected == "6":
            wait(StartDelay)
            run_task(T6_Run())  
            run_task(RL.stopEverything())        
        elif selected == "7":
            wait(StartDelay)
            #run_task(T7_Run())  
            run_task(RL.stopEverything()) 
        elif selected == "8":
            wait(StartDelay)
            #run_task(T8_Run())  
            run_task(RL.stopEverything()) 
        elif selected == "X":
            # does not nothing used to show end of menu
            run_task(RL.stopEverything())
            break

    except BaseException as menuException:
        print("Stop was Pressed or a Critical Error Occured. Stopping all motors.")
        print(menuException)
        run_task(RL.stopEverything())
        break
    print("    Back to Menu")
