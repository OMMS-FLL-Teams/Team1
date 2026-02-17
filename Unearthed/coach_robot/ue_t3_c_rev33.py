# Robot Lib Demonstration
#
# task revision number
task_number="3"     # enter the task number here 
task_revision="33"
#
import robot_library_rev33 as RL

async def T3_Run(): 

    #   enter the list of missions
    print ("Task ",task_number," Rev ",task_revision," - transit to right launch")

    await RL.initializeRobotForTask()
    
    waitForPrompt=False
    RL.debugL1=False
    RL.debugL2=False

    await RL.wait(500)
    if RL.debugL1: print("  transit to right launch")

    await RL.driveRobot(390,800,800,"hold",waitForPrompt)
    await RL.turnRobot(37,300,300,"coast",waitForPrompt)
    await RL.driveRobot(1450,900,900,"hold",waitForPrompt)

