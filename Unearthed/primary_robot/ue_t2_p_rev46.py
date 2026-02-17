# Robot Lib Demonstration
#
# task revision number
task_number="2"      
task_revision="45"
#
import robot_library_rev33 as RL

async def T2_Run(): 

    print ("Task ",task_number," Rev ",task_revision," - Missions 01/Surface Brushing, 02/Map Reveal")
    await RL.initializeRobotForTask()

    waitForPrompt=False
    RL.debugL1=True
    RL.debugL2=False
    
    RL.driveBase.use_gyro(True)

    await RL.wait(500)

    if RL.debugL1: print("   missions 1 & 2 - pickup topsoil sample, knockdown sides of mission 1")
    await RL.driveRobotAndLift(755,750,500,"left",550,800,"hold",False,True,waitForPrompt)
    await RL.moveAttachment("left",1300,600,False,"hold",False,True,waitForPrompt)
    await RL.wait(500)
    await RL.driveRobot(-410,800,300,"hold",waitForPrompt)

    if RL.debugL1: print("  mission 2 - drop off soil deposit")
    await RL.turnRobot(85,200,200,False,waitForPrompt)
    await RL.driveRobot(235,650,500,"hold",waitForPrompt)
    await RL.moveAttachment("left",400,1000,False,"hold",False,True,waitForPrompt)
    await RL.driveRobot(-180,650,500,"hold",waitForPrompt)
    await RL.turnRobot(-84,200,200,False,waitForPrompt)

    if RL.debugL1: print("   mission 3 - mineshaft explorer")
    await RL.moveAttachment("right",-1,600,False,"hold",False,True,waitForPrompt)
    await RL.driveRobot(220,600,250,"hold",waitForPrompt)
    await RL.turnRobot(61,200,200,"hold",waitForPrompt)
    await RL.moveAttachment("left",130,900,False,"coast",False,True,waitForPrompt)
    await RL.driveRobot(330,600,250,"hold",waitForPrompt)
    await RL.moveAttachment("left",1800,950,False,"hold",False,True,waitForPrompt)
    await RL.wait(500)

    if RL.debugL1: print("   mission 2 - move left two topsoil samples")
    await RL.driveRobotAndLift(-275,400,250,"left",300,900,"coast",False,True,waitForPrompt)
    await RL.moveAttachment("left",450,950,False,"hold",False,True,waitForPrompt)
    await RL.turnRobot(-105,270,300,False,waitForPrompt)
    await RL.driveRobot(255,150,100,"hold",waitForPrompt)
    #await RL.turnRobot(1,200,200,"coast",waitForPrompt)
    await RL.wait(250)
    #await RL.turnRobot(-8,200,200,"coast",waitForPrompt)
    await RL.driveRobot(-155,200,200,"hold",waitForPrompt)
    
    if RL.debugL1: print("   Drive to right launch area")
    await RL.turnRobot(50,270,300,"hold",waitForPrompt)
    await RL.driveRobot(-410,500,450,"hold",waitForPrompt)
    await RL.turnRobot(80,270,300,"hold",waitForPrompt)
    await RL.driveRobotAndLift(850,800,450,"left",1850,900,"hold",False,True,waitForPrompt)
    await RL.turnRobot(17,200,200,"hold",waitForPrompt)
    await RL.driveRobot(300,900,450,"hold",waitForPrompt)
    await RL.turnRobot(-10,200,200,"hold",waitForPrompt)
    await RL.driveRobot(550,900,450,"hold",waitForPrompt)

