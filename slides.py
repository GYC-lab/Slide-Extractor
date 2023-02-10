import numpy as np
import progressbar
import cv2
import os

def video2slide(input_video,final_directory,perc,ch):
    
    cap = cv2.VideoCapture(input_video)

    if cap.isOpened()==False:
        print("ERROR:Failed to open video file")
        exit()

    os.chdir(final_directory)
    count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    n=cap.get(cv2.CAP_PROP_FRAME_WIDTH)*cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    old_frame = None
    f=0
    i=0
    sl_count=1

    bar = progressbar.ProgressBar(maxval=count, \
        widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
    bar.start()

    while i<count:

        ret, frame = cap.read()
        f=f+1
        if ret == True and f==ch:

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            if old_frame is not None:
                diff_frame = cv2.absdiff(frame, old_frame)
                diff_per=float(cv2.countNonZero(cv2.cvtColor(diff_frame, cv2.COLOR_BGR2GRAY))/n)
                frame_blank=float(cv2.countNonZero(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))/n)
                if diff_per>perc and frame_blank>0.40:
                    name=('slide' + "% d"+'.jpg') % sl_count
                    cv2.imwrite(name,frame)
                    sl_count=sl_count+1
                    old_frame = frame
            else:
                old_frame = frame
            f=0
        bar.update(i+1)
        i=i+1
    print("capture %d slides"%sl_count)
    bar.finish()
    cap.release()

if __name__ == "__main__":
    
    folderpath = os.getcwd()
    path_in = folderpath + "\input_video\\"
    path_out = folderpath + "\output_silde\\"
    files = os.listdir(path_in)

    perc=0.25   
    ch=25       

    for file in files:
        input_location=path_in+file
        output_location=path_out+file
        i = output_location.rfind('.')
        output_location = output_location[:i]

        final_directory = os.path.join(folderpath,output_location)

        if not os.path.exists(final_directory):
            os.makedirs(final_directory)

        print("handling "+file)
        input_location=path_in+file
        video2slide(input_location,final_directory,perc,ch)