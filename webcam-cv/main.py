import re
import cv2 
import numpy


def returnCameraIndexes():
    # checks the first 10 indexes.
    index = 0
    arr = []
    i = 10
    while i > 0:
        cap = cv2.VideoCapture(index)
        if cap.read()[0]:
            arr.append(index)
            cap.release()
        index += 1
        i -= 1
    return arr

if __name__ == "__main__":
    # choices = returnCameraIndexes()
    # print(choices)
# define a video capture object 
    vid = cv2.VideoCapture(2) 

    while(True): 

        # Capture the video frame 
        # by frame 
        ret, frame = vid.read() 

        # Display the resulting frame 
        cv2.imshow('frame', frame) 

        # the 'q' button is set as the 
        # quitting button you may use any 
        # desired button of your choice 
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

# After the loop release the cap object 
    vid.release() 
# Destroy all the windows 
    cv2.destroyAllWindows() 
