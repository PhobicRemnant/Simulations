import pybullet as p 
import time 
import pybullet_data 


physics_client = p.connect(p.GUI) 
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
robotStartPos = [0,0,0.15]
robotStartOrientation = p.getQuaternionFromEuler([0,0,0])
planeID = p.loadURDF("plane.urdf")
robotID = p.loadURDF("mobile.urdf", robotStartPos, robotStartOrientation)

for i in range(10000):
    p.stepSimulation()
    time.sleep(1./240.)

cubePos, cubeOrn = p.getBasePositionAndOrientation(robotID)
print(cubePos,cubeOrn)
p.disconnect()
