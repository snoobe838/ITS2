import tkinter as ttk
import cv2
import pandas as pd
import face_recognition as fr
from tkinter import font

def register(name):
    fname = 'features.csv'

    try:
        df=pd.read_csv(fname)
    except:
        df = pd.DataFrame({'name':[],'enc':[]})

    fd = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )
    vid = cv2.VideoCapture(0)
    counter = 0
    names =[]
    feats = []  
    name = input('Enter your name:')
    while True:
        ack, img = vid.read()
        if ack:
            faces = fd.detectMultiScale(img, 1.2,10)
            if len(faces) == 1:
                x,y,w,h = faces[0]
                face_img = img[y:y+h,x:x+w,:].copy()
                face_enc = fr.face_encodings(face_img)
                if len(face_enc) == 1:
                    counter += 1
                    print(counter)
                    names += [name]
                    feats += [face_enc[0].tolist()]
                    #f= pd.DataFrame({'name':[name], 'enc':face_enc})
                    #df = pd.concat([df,f],axis=0, ignore_index=True
                    
            #...
                if counter == 20:
                    f= pd.DataFrame({'name':names, 'enc':feats})
                    df = pd.concat([df,f],axis=0, ignore_index=True)
                    df.to_csv(fname)
                    print('saved')
                    break 
            cv2.imshow('preview', img) #depends on requirement
            key = cv2.waitKey(1)
            if key == ord('x'):
                break
    cv2.destroyAllWindows()
    vid.release()