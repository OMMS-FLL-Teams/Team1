# Robot Lib Demonstration
#
# task revision number
task_number="2"      
task_revision="31"
#
import robot_library_rev33 as RL

async def T2_Run(): 

    print ("Task ",task_number," Rev ",task_revision," - Missions 01/Surface Brushing, 02/Map Reveal")
    await RL.initializeRobotForTask()

    waitForPrompt=False
    RL.debugL1=False
    RL.debugL2=False

    await RL.wait(500)

    if RL.debugL1: print("   mission 02 - pickup topsoil sample")
    await RL.driveRobotAndLift(725,750,700,"left",550,800,"hold",False,True,waitForPrompt)
    await RL.moveAttachment("left",1300,600,False,"hold",False,True,waitForPrompt)
    await RL.wait(500)
    await RL.driveRobot(-460,200,200,"hold",waitForPrompt)

    if RL.debugL1: print("   mission 01 - move spoil deposits")
    await RL.turnRobot(-45,400,250,False,waitForPrompt)
    await RL.driveRobot(60,450,500,"hold",waitForPrompt)
    await RL.moveAttachment("left",590,1000,False,"hold",False,True,waitForPrompt)
    await RL.driveRobot(-160,450,500,"hold",waitForPrompt)
    await RL.turnRobot(45,350,250,False,waitForPrompt)
 
    if RL.debugL1: print("   mission 02 - move left topsoil sample")
    await RL.driveRobot(360,520,350,False,waitForPrompt)
    await RL.turnRobot(-45,270,300,"hold",waitForPrompt)
    await RL.moveAttachment("right",-175,200,False,"coast",False,True,waitForPrompt)
    await RL.driveRobot(200,520,350,False,waitForPrompt)
    await RL.driveRobot(-20,520,350,False,waitForPrompt)
    await RL.turnRobot(10,270,300,"hold",waitForPrompt)
    await RL.turnRobot(-10,270,300,"hold",waitForPrompt)

    if RL.debugL1: print("   mission 02 - move back topsoil sample")
    await RL.moveAttachment("right",-1,200,False,"coast",False,True,waitForPrompt)
    await RL.driveRobot(-40,500,350,"hold",waitForPrompt)
    await RL.turnRobot(15,250,300,"hold",waitForPrompt)
    await RL.driveRobot(30,500,350,"hold",waitForPrompt)
    await RL.moveAttachment("right",-175,200,False,"hold",False,True,waitForPrompt)
    await RL.driveRobot(40,500,350,"hold",waitForPrompt)

    if RL.debugL1: print("   mission 3 - mineshaft explorer")
    await RL.moveAttachment("right",-1,600,False,"hold",False,True,waitForPrompt)
    await RL.driveRobot(-215,400,250,"hold",waitForPrompt)
    await RL.turnRobot(84,270,300,"hold",waitForPrompt)
    await RL.moveAttachment("left",160,900,False,"coast",False,True,waitForPrompt)
    await RL.driveRobot(345,400,250,"hold",waitForPrompt)
    await RL.moveAttachment("left",1750,950,False,"hold",False,True,waitForPrompt)
    await RL.wait(1500)

    if RL.debugL1: print("   Drive to right launch area")
    await RL.driveRobotAndLift(-330,400,250,"left",450,900,"coast",False,True,waitForPrompt)
    #await RL.moveAttachment("left",450,900,False,"coast",False,True,waitForPrompt)
    #await RL.driveRobot(-330,400,250,"hold",waitForPrompt)
    await RL.turnRobot(-45,270,300,"hold",waitForPrompt)
    await RL.driveRobot(-270,400,250,"hold",waitForPrompt)
    await RL.turnRobot(84,270,300,"hold",waitForPrompt)
    #await RL.driveRobot(1800,800,250,"hold",waitForPrompt)
    await RL.driveRobotAndLift(1800,700,250,"left",1850,900,"hold",False,True,waitForPrompt)

