
import cv2 
import time
  

cam_port = 0
cam = cv2.VideoCapture(cam_port)



cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
  
  
framenum= 0
string = "reaper/reaper"

while(1):

    result, image = cam.read()

    if result:
      

        direct_string = string + str(framenum) + ".png"
 
        cv2.imwrite(direct_string, image)
        print("saved image "+direct_string)




    else: #fail
        print("try again")
        
    framenum+=1
    time.sleep(10)