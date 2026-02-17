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
    await RL.turnRobot(6,100,200,"hold",waitForPrompt)
    await RL.moveAttachment("left",-875,500,False,"brake",False,True, waitForPrompt)
    await RL.turnRobot(20,100,200,"hold",waitForPrompt) 
    await RL.wait(500)
    await RL.turnRobot(-50,100,200,"hold",waitForPrompt)    
    await RL.driveRobot(-540,750,500,"hold",waitForPrompt)

    if RL.debugL1: print("  Tip the Scales  - scale pan")
    await RL.turnRobot(23,100,200,"hold",waitForPrompt)
    await RL.moveAttachment("right",-168,500,False,"coast",False,True, waitForPrompt)
    await RL.turnRobot(-66,200,200,"hold",waitForPrompt)
    await RL.turnRobot(41,200,200,"hold",waitForPrompt)
    await RL.driveRobot(430,500,500,"hold",waitForPrompt)

    if RL.debugL1: print("  what's on sale - wares table")
    await RL.moveAttachment("right",0,100,False,"coast",False,True, waitForPrompt)
    await RL.driveRobot(-590,500,500,"hold",waitForPrompt)
    await RL.turnRobot(47,200,200,"hold",waitForPrompt)
    await RL.driveRobot(150,400,400,"hold",waitForPrompt)  
    await RL.moveAttachment("right",-154,500,False,"coast",False,True, waitForPrompt)  
    await RL.turnRobot(-32,300,200,"hold",waitForPrompt)

    if RL.debugL1: print("  silo")
    await RL.driveRobot(-230,500,500,"hold",waitForPrompt)  
    await RL.moveAttachment("right",-1,200,False,"coast",False,True, waitForPrompt)
    #await RL.driveRobot(-220,500,500,"hold",waitForPrompt)  
    await RL.turnRobot(53,200,200,"hold",waitForPrompt)
    await RL.driveRobot(295,500,500,"hold",waitForPrompt)  
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

