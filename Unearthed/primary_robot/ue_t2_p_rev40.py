# Robot Lib Demonstration
#
# task revision number
task_number="2"      
task_revision="40"
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

    if RL.debugL1: print("   mission 02 - pickup topsoil sample")
    await RL.driveRobotAndLift(725,750,700,"left",550,800,"hold",False,True,waitForPrompt)
    await RL.moveAttachment("left",1300,600,False,"hold",False,True,waitForPrompt)
    await RL.wait(500)
    await RL.driveRobot(-680,800,300,"hold",waitForPrompt)


    #RL.driveBase.use_gyro(False)
    #await RL.wait(100)
    if RL.debugL1: print("  mission 01 - drop off spoil deposit")
    await RL.turnRobot(43,200,200,False,waitForPrompt)
    #RL.driveBase.use_gyro(True)
    await RL.driveRobot(350,650,500,"hold",waitForPrompt)
    await RL.moveAttachment("left",590,1000,False,"hold",False,True,waitForPrompt)
    await RL.driveRobot(-250,650,500,"hold",waitForPrompt)
    await RL.turnRobot(-39,200,200,False,waitForPrompt)

    if RL.debugL1: print("   mission 3 - mineshaft explorer")
    await RL.moveAttachment("right",-1,600,False,"hold",False,True,waitForPrompt)
    await RL.driveRobot(420,600,250,"hold",waitForPrompt)
    await RL.turnRobot(57,300,200,"hold",waitForPrompt)
    await RL.moveAttachment("left",130,900,False,"coast",False,True,waitForPrompt)
    await RL.driveRobot(320,600,250,"hold",waitForPrompt)
    await RL.moveAttachment("left",1800,950,False,"hold",False,True,waitForPrompt)
    await RL.wait(500)

    if RL.debugL1: print("   mission 02 - move left two topsoil samples")
    await RL.driveRobotAndLift(-305,400,250,"left",300,900,"coast",False,True,waitForPrompt)
    await RL.moveAttachment("left",450,950,False,"hold",False,True,waitForPrompt)
    await RL.turnRobot(-107,270,300,False,waitForPrompt)
    await RL.moveAttachment("right",-170,200,False,"coast",False,True,waitForPrompt)
    await RL.driveRobot(235,200,200,"hold",waitForPrompt)
    await RL.wait(250)
    await RL.moveAttachment("right",-80,500,False,"hold",False,True,waitForPrompt)
    await RL.driveRobot(-145,200,200,"hold",waitForPrompt)
    await RL.moveAttachment("right",-1,400,False,"hold",False,True,waitForPrompt)
    
    if RL.debugL1: print("   Drive to right launch area")
    #await RL.driveRobotAndLift(-140,400,250,"left",450,900,"coast",False,True,waitForPrompt)
    #await RL.moveAttachment("left",450,900,False,"coast",False,True,waitForPrompt)
    await RL.turnRobot(50,270,300,"hold",waitForPrompt)
    await RL.driveRobot(-380,500,450,"hold",waitForPrompt)
    await RL.turnRobot(81,270,300,"hold",waitForPrompt)
    #await RL.driveRobot(1800,800,250,"hold",waitForPrompt)
    await RL.driveRobotAndLift(900,800,450,"left",1850,900,"hold",False,True,waitForPrompt)
    await RL.turnRobot(6,270,300,"hold",waitForPrompt)
    await RL.driveRobot(900,900,450,"hold",waitForPrompt)

