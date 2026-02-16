# Robot Lib Demonstration
#
# task revision number
task_number="5"     # enter the task number here 
task_revision="22"
#
import robot_library_rev33 as RL

async def T5_Run(): 

    #   enter the list of missions
    print ("Task ",task_number," Rev ",task_revision," -  13/Statue Rebuild, 10/Tip the Scales  - scale pan, 9/Whats on Sale (table/red stick), 8/Silo")

    await RL.initializeRobotForTask()

    waitForPrompt=False
    RL.debugL1=False
    RL.debugL2=False

    await RL.wait(500)
    if RL.debugL1: print("  statue rebuild")
    await RL.driveRobotAndLift(800,750,500,"left",-1905,900,"coast",False,True,waitForPrompt)

    await RL.turnRobot(51,100,100,"hold",waitForPrompt)
    await RL.driveRobot(280,750,500,"hold",waitForPrompt)
    await RL.turnRobot(5,100,200,"hold",waitForPrompt)
    await RL.moveAttachment("left",-890,500,False,"brake",False,True, waitForPrompt)
    await RL.turnRobot(20,100,200,"hold",waitForPrompt)
    await RL.wait(500)
    await RL.turnRobot(-47,100,200,"hold",waitForPrompt)    
    await RL.driveRobot(-530,750,500,"hold",waitForPrompt)

    if RL.debugL1: print("  Tip the Scales  - scale pan")
    await RL.turnRobot(24,100,200,"hold",waitForPrompt)
    await RL.moveAttachment("right",-168,500,False,"coast",False,True, waitForPrompt)
    await RL.turnRobot(-66,200,200,"hold",waitForPrompt)
    await RL.turnRobot(41,200,200,"hold",waitForPrompt)
    await RL.driveRobot(440,500,500,"hold",waitForPrompt)

    if RL.debugL1: print("  what's on sale - wares table")
    await RL.moveAttachment("right",0,100,False,"coast",False,True, waitForPrompt)
    await RL.driveRobot(-575,500,500,"hold",waitForPrompt)
    await RL.turnRobot(47,200,200,"hold",waitForPrompt)
    await RL.driveRobot(165,500,500,"hold",waitForPrompt)  
    await RL.moveAttachment("right",-154,500,False,"coast",False,True, waitForPrompt)  
    await RL.turnRobot(-32,300,200,"hold",waitForPrompt)

    if RL.debugL1: print("  silo")
    await RL.driveRobot(-210,500,500,"hold",waitForPrompt)  
    await RL.moveAttachment("right",-1,200,False,"coast",False,True, waitForPrompt)
    #await RL.driveRobot(-220,500,500,"hold",waitForPrompt)  
    await RL.turnRobot(50,200,200,"hold",waitForPrompt)
    await RL.driveRobot(305,500,500,"hold",waitForPrompt)  
    await RL.moveAttachment("right",-165,900,False,"coast",False,True, waitForPrompt)
    await RL.moveAttachment("right",-1,900,False,"coast",False,True, waitForPrompt)
    await RL.moveAttachment("right",-165,900,False,"coast",False,True, waitForPrompt)
    await RL.moveAttachment("right",-1,900,False,"coast",False,True, waitForPrompt)
    await RL.moveAttachment("right",-165,900,False,"coast",False,True, waitForPrompt)
    await RL.moveAttachment("right",-1,900,False,"coast",False,True, waitForPrompt)
    await RL.moveAttachment("right",-165,900,False,"coast",False,True, waitForPrompt)
    await RL.moveAttachment("right",-1,900,False,"coast",False,True, waitForPrompt)
    await RL.moveAttachment("right",-165,900,False,"coast",False,True, waitForPrompt)
    await RL.moveAttachment("right",-1,900,False,"coast",False,True, waitForPrompt)

