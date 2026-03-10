# Unearthed Task 1 
# Mission 12 - all 3 parts
#
#
# task revision number
task_number="1"    
task_revision="12"
#
import robot_library_rev33 as RL

async def T1_Run(): 

    print("Task ",task_number," Rev ",task_revision," - Mission 12/Salvage Operation")
    await RL.initializeRobotForTask()
    
    waitForPrompt=False
    RL.debugL1=False
    RL.debugL2=False

    await RL.wait(500)
    if RL.debugL1: print("  Push lever and pull sand for shipwreck")
    await RL.driveRobot(460,200,500,"coast",waitForPrompt)
    await RL.moveAttachment("right",50,100,False,"hold",False,True,waitForPrompt)
    await RL.driveRobot(-160,400,200,"hold",waitForPrompt)
    await RL.driveRobot(50,400,200,"hold",waitForPrompt)
    await RL.driveRobot(-400,400,200,"hold",waitForPrompt)
