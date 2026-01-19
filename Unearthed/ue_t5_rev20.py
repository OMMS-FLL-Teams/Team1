# Robot Lib Demonstration
#
# task revision number
task_number="5"     # enter the task number here 
task_revision="20"
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
    await RL.driveRobotAndLift(780,750,500,"left",-1910,900,"coast",False,True,waitForPrompt)

    await RL.turnRobot(51,100,100,"hold",waitForPrompt)
    await RL.driveRobot(280,750,500,"hold",waitForPrompt)
    await RL.turnRobot(6,100,200,"hold",waitForPrompt)
    await RL.moveAttachment("left",-860,500,False,"brake",False,True, waitForPrompt)
    await RL.turnRobot(14,100,200,"hold",waitForPrompt) 
    await RL.turnRobot(-43,100,200,"hold",waitForPrompt)    
    await RL.driveRobot(-530,750,500,"hold",waitForPrompt)

    if RL.debugL1: print("  Tip the Scales  - scale pan")
    await RL.turnRobot(18,100,200,"hold",waitForPrompt)
    await RL.moveAttachment("right",-162,500,False,"coast",False,True, waitForPrompt)
    await RL.turnRobot(-66,200,200,"hold",waitForPrompt)
    await RL.turnRobot(48,200,200,"hold",waitForPrompt)
    await RL.driveRobot(420,500,500,"hold",waitForPrompt)

    if RL.debugL1: print("  what's on sale - wares table")
    await RL.moveAttachment("right",0,100,False,"coast",False,True, waitForPrompt)
    await RL.driveRobot(-610,500,500,"hold",waitForPrompt)
    await RL.turnRobot(47,200,200,"hold",waitForPrompt)
    await RL.driveRobot(155,500,500,"hold",waitForPrompt)  
    await RL.moveAttachment("right",-154,500,False,"coast",False,True, waitForPrompt)  
    await RL.turnRobot(-32,300,200,"hold",waitForPrompt)

    if RL.debugL1: print("  silo")
    await RL.driveRobot(-240,500,500,"hold",waitForPrompt)  
    await RL.moveAttachment("right",-1,200,False,"coast",False,True, waitForPrompt)
    #await RL.driveRobot(-220,500,500,"hold",waitForPrompt)  
    await RL.turnRobot(49,200,200,"hold",waitForPrompt)
    await RL.driveRobot(260,500,500,"hold",waitForPrompt)  
    await RL.moveAttachment("right",-162,900,False,"coast",False,True, waitForPrompt)
    await RL.moveAttachment("right",-1,900,False,"coast",False,True, waitForPrompt)
    await RL.moveAttachment("right",-162,900,False,"coast",False,True, waitForPrompt)
    await RL.moveAttachment("right",-1,900,False,"coast",False,True, waitForPrompt)
    await RL.moveAttachment("right",-162,900,False,"coast",False,True, waitForPrompt)
    await RL.moveAttachment("right",-1,900,False,"coast",False,True, waitForPrompt)
    await RL.moveAttachment("right",-162,900,False,"coast",False,True, waitForPrompt)
    await RL.moveAttachment("right",-1,900,False,"coast",False,True, waitForPrompt)
    await RL.moveAttachment("right",-162,900,False,"coast",False,True, waitForPrompt)
    await RL.moveAttachment("right",-1,900,False,"coast",False,True, waitForPrompt)

