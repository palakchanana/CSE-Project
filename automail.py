import datetime

import yagmail
import os
import datetime
date = datetime.date.today().strftime("%B %d, %Y")
path = 'Attendance'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)

receiver = "palakchanana.pc@gmail.com"  # receiver email address
body = "Attendence File"  # email body
# noinspection PyTypeChecker
fileName = "Attendance_2022-01-06_03-54-07.csv"

yag = yagmail.SMTP("cseprojectgroup6@gmail.com", "group@06")

yag.send(
    to=receiver,
    subject="Attendance Report",
    contents=body,
    attachments=fileName,
)
print("Email Sent!")


