import csv
import cv2
import os


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False


# noinspection PyUnresolvedReferences,PyUnusedLocal
def takeImages():
    Id = input("Enter Your Id: ")
    name = input("Enter Your Name: ")

    if is_number(Id) and name.isalpha():
        # noinspection PyUnresolvedReferences
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0

        while sampleNum<30:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 4, minSize=(30 ,30),flags = cv2.CASCADE_SCALE_IMAGE)
            for(x,y,w,h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

                #saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage" + os.sep + name + "."+Id + '.' +
                            str(sampleNum) + ".jpg", gray[y:y+h, x:x+w])
                sampleNum+=1
                cv2.imshow('frame', img)
                key = cv2.waitKey(10)
                if key == 27:
                    break
               # elif sampleNum > 30:
                 #   break
        cam.release()
        cv2.destroyAllWindows()
        res: str ="Images Saved for ID : " + Id + " Name : " + name
        row = [Id, name]
        with open("StudentDetails"+os.sep+"StudentDetails.csv", 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
    else:
        if is_number(Id):
            print("Enter Alphabetical Name")
        if name.isalpha():
            print("Enter Numeric ID")