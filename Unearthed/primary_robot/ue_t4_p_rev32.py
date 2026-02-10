# Robot Lib Demonstration
#
# task revision number
task_number="4"     # enter the task number here 
task_revision="32"
#
import robot_library_rev33 as RL

# change # in T#_Run() to the number of the task
async def T4_Run(): 

    #   enter the list of missions
    print ("task# ",task_number," task_rev ",task_revision," Missions 5/Who Lived Here, 6/The Forge,  9/Whats on Sale (red paddle), 10/Tip the Scale (bucket), ")
    await RL.initializeRobotForTask()
    
    waitForPrompt=False
    RL.debugL1=False
    RL.debugL2=False

    await RL.wait(500)
    if RL.debugL1: print(" the forge ")
    await RL.driveRobot(525,600,500,"hold",waitForPrompt)
    await RL.moveAttachment("right",-162,500,False,"coast",False,True, waitForPrompt)
    await RL.turnRobot(22,300,400,"hold",waitForPrompt)


    if RL.debugL1: print(" who lived here ")
    await RL.turnRobot(-22,300,400,"hold",waitForPrompt)
    await RL.driveRobot(50,400,500,"hold",waitForPrompt)
    await RL.moveAttachment("right",-149,300,False,"hold",False,True, waitForPrompt)
    await RL.wait(500)
    await RL.turnRobot(-27,300,400,"hold",waitForPrompt)
    await RL.wait(500)
    await RL.turnRobot(10,300,400,"hold",waitForPrompt)
    await RL.moveAttachment("right",-49,500,False,"brake",False,True, waitForPrompt)
    await RL.driveRobot(20,200,500,"hold",waitForPrompt)
    await RL.moveAttachment("right",-1,500,False,"hold",False,True, waitForPrompt)
    await RL.driveRobot(20,200,500,"hold",waitForPrompt)

    if RL.debugL1: print("  what's on sale - red paddle")
    await RL.turnRobot(-47,300,400,"hold",waitForPrompt)
    await RL.driveRobot(300,600,500,"hold",waitForPrompt)
    await RL.turnRobot(-79,300,400,"hold",waitForPrompt)
    await RL.driveRobot(130,300,500,"hold",waitForPrompt)
    await RL.moveAttachment("right",-150,300,False,"hold",False,True, waitForPrompt)
    await RL.wait(500)

    
    if RL.debugL1: print("   tip the scales - bucket")
    await RL.moveAttachment("right",250,300,False,"hold",False,True, waitForPrompt)
    await RL.driveRobot(-70,800,600,"hold",waitForPrompt)
    await RL.turnRobot(80,400,400,"hold",waitForPrompt)
    await RL.driveRobot(150,800,600,"hold",waitForPrompt)
    await RL.turnRobot(9,400,400,"hold",waitForPrompt)
    await RL.driveRobot(-250,800,600,"hold",waitForPrompt)
    await RL.driveRobot(10,800,600,"hold",waitForPrompt)
    await RL.turnRobot(-28,400,400,"hold",waitForPrompt)
    await RL.driveRobot(-115,800,600,"hold",waitForPrompt) 
    await RL.turnRobot(30,400,400,"hold",waitForPrompt) 
    await RL.driveRobot(-150,800,600,"hold",waitForPrompt)
    await RL.turnRobot(29,400,400,"hold",waitForPrompt)
    await RL.driveRobot(-700,800,600,"hold",waitForPrompt)            
    #await RL.driveRobotAndLift(0,800,600,"left",50,200,"hold",False,True, waitForPrompt)



