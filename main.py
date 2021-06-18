from flask import Flask, render_template, request
import cv2
from pyzbar.pyzbar import decode 
import time
app=Flask(_name_)
global desc
@app.route("/")
def home():
   
    return render_template("welcome.html")

@app.route("/scan")
def scan():
    cap=cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    used_codes=[]
    desc=""
    camera=True
    while camera==True:
        success,frame=cap.read()
        
        for code in decode(frame):
            if code.data.decode('utf-8') not in used_codes:
                print('Approved.You enter!')
                print(code.data.decode('utf-8'))
                desc=code.data.decode('utf-8')
                used_codes.append(code.data.decode('utf-8'))
                time.sleep(5)
                return render_template("scan.html", desc=desc)
            
            elif code.data.decode('utf-8') in used_codes:
                print('sorry,this code is already used!')
                time.sleep(5)
            else:
               pass
        cv2.imshow('Testing-code-scan',frame)
        cv2.waitKey(1)

@app.route("/result")
def result():
    desc=""
    list_of_chemicals=["parabens","sodium laureth sulphate","sodium lauryl sulphate","fluoride, propylene glycol","ammonium chloride","tryclone, sugar"]
    for i in list_of_chemicals:
        if i in desc:
            return render_template("result.html", desc="There are harmful chemicals present in the product")
        else:
            return render_template("result.html",desc="The Product is eco-friendly")

if _name_ == '_main_':
    app.run()