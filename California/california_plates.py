from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PyPDF2 import PdfFileMerger
from datetime import date
from datetime import datetime
from datetime import timedelta
import random
import qrcode
import PySimpleGUI as sg
from tkinter import messagebox

pdfmetrics.registerFont(TTFont('times', 'times.ttf'))
pdfmetrics.registerFont(TTFont('timesbd', 'timesbd.ttf'))
pdfmetrics.registerFont(TTFont('rage', 'rage-italic.ttf'))
pdfmetrics.registerFont(TTFont('dealer', 'dealerplate california.ttf'))
pdfmetrics.registerFont(TTFont('helvetica', 'Helvetica.ttf'))
pdfmetrics.registerFont(TTFont('helvetica_bold', 'Helvetica-Bold.ttf'))

year = "2022"
make = "TOYO"
vin = "1FAFP34N65W214191"
major_color = "SILVER"
minor_color = "GREEN"
body = "4D"
model = "ZX4"
owner = "ARTURO SANCHEZ"
address = "2302 LOCKWOOD DR."
city = "HOUSTON"
state = "TX"
zip_code = "77020"

today = date.today()
issue_date = str(today.month) + "/" + str(today.day) + "/" + str(today.year)
now = datetime.now()
new_date = now + timedelta(days=90)
expiration_date = str(new_date.month) + "/" + str(new_date.day) + "/" + str(new_date.year)
expiration_year = str(new_date.year)
month = str(new_date.month)

if(month=="1"):
	expiration_month="JAN"
elif(month=="2"):
	expiration_month="FEB"	
elif(month=="3"):
	expiration_month="MAR"	
elif(month=="4"):
	expiration_month="APR"	
elif(month=="5"):
	expiration_month="MAY"	
elif(month=="6"):
	expiration_month="JUN"	
elif(month=="7"):
	expiration_month="JUL"	
elif(month=="8"):
	expiration_month="AUG"	
elif(month=="9"):
	expiration_month="SEP"	
elif(month=="10"):
	expiration_month="OCT"	
elif(month=="11"):
	expiration_month="NOV"	
elif(month=="12"):
	expiration_month="DEC"	

def generatePDF(year, make, issue_date, expiration_date, vin, major_color, minor_color, body, model, owner, address, city, state, zip_code, expiration_month, expiration_year,odometer):
	plate = chr(random.randint(65, 90)) + chr(random.randint(65, 90)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
	ros = str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))	
	qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
	messagebox.showinfo(message="The plate will be: "+plate, title="New Plate: ")
	qr.add_data("OWR:"+owner+"COL:"+major_color+"MDL:"+model+"TAG:"+plate)
	qr.make(fit=True)
	img = qr.make_image(fill='black', back_color='white')
	img.save('qrcode.png')

	c = canvas.Canvas("newfile.pdf", landscape(letter))
	c.drawImage('fondo.png', 290, 160, 260, 290)
	c.drawImage('qrcode.png', 130, 425, 78, 78)
	c.setFont('rage', 105)
	c.drawString(205, 460, "California")
	c.setFont('dealer', 280)
	c.drawString(18, 200, plate)
	c.setFont('helvetica', 16)
	c.drawString(23, 440, "ROS#")
	c.setFont('helvetica_bold', 16)
	c.drawString(69, 440, ros)
	c.setFont('helvetica_bold', 18)
	c.drawString(205, 435, make)
	c.drawString(600, 435, "EXPIRES: "+expiration_date)
	c.setFont('helvetica', 16)
	c.drawString(383, 435, "VIN: "+vin)
	c.setFont('helvetica_bold', 40)
	c.drawString(23, 460, expiration_month)
	c.drawString(640, 460, expiration_year)
	c.showPage()
	c.drawImage('fondo.png', 290, 160, 260, 290)
	c.drawImage('qrcode.png', 130, 425, 78, 78)
	c.setFont('rage', 105)
	c.drawString(205, 460, "California")
	c.setFont('dealer', 280)
	c.drawString(18, 200, plate)
	c.setFont('helvetica', 16)
	c.drawString(23, 440, "ROS#")
	c.setFont('helvetica_bold', 16)
	c.drawString(69, 440, ros)
	c.setFont('helvetica_bold', 18)
	c.drawString(205, 435, make)
	c.drawString(600, 435, "EXPIRES: "+expiration_date)
	c.setFont('helvetica', 16)
	c.drawString(383, 435, "VIN: "+vin)
	c.setFont('helvetica_bold', 40)
	c.drawString(23, 460, expiration_month)
	c.drawString(640, 460, expiration_year)
	c.showPage()
	c.save()
###############################################################################################################################################
	c = canvas.Canvas("newfile2.pdf", letter)
	c.drawImage('footer.png', 0, 0, 615.51, 122.22)
	c.drawImage('center.png', 0, 122.3, 613.62, 320.04)
	c.drawImage('header.png', 0, 442.34, 612.36, 360.99)
	c.setFont('helvetica', 6)
	c.drawString(27, 351, "MAKE")
	c.drawString(27, 327, "DEALER'S NUMBER")
	c.drawString(27, 303, "SOLD TO: PRINT TRUE FULL NAME(S)")
	c.drawString(27, 279, "BUSINESS OR RESIDENCE ADDRESS")
	c.drawString(147, 351, "YEAR")
	c.drawString(202, 351, "MODEL")
	c.drawString(261, 351, "BODY TYPE")
	c.drawString(316, 351, "VEHICLE IDENTIFICATION NUMBER")
	c.drawString(150, 327, "SALESPERSON'S NUMBER")
	c.drawString(287, 327, "TEMPORARY OR PERMANENT LICENSE PLATE NUMBER")
	c.drawString(469, 327, "DATE SOLD (MO/DAY/YR)")
	c.drawString(317, 279, "APT./STE. NO.")
	c.drawString(363, 279, "CITY")
	c.drawString(484, 279, "STATE")
	c.drawString(519, 279, "ZIP CODE")
	c.setFont('helvetica', 7)
	c.drawString(27, 252, "NOTE: ")
	c.drawString(317, 252, "IMPORTANT: ")
	c.drawString(27, 252, "NOTE: UPON TRANSFER OR SALE, DEALER")
	c.drawString(27, 242, "MUST ENTER ODOMETER READING HERE:")
	c.drawString(317, 252, "IMPORTANT: ENTER BOTH DEALERS AND SALESPERSON'S NUMBERS. This is a")
	c.drawString(317, 242, "notice of purchase of vehicle. Do not use as an application for registration or title")
	c.setFont('helvetica', 8)
	c.drawString(27, 288, "(1)")
	c.drawString(317, 288, "(2)")
	c.drawString(28, 338, make)
	c.drawString(204, 338, model)
	c.drawString(318, 338, vin)
	c.drawString(50, 293, owner)
	c.drawString(28, 267, address)
	c.drawString(363, 267, city)
	c.drawString(484, 267, state)
	c.drawString(519, 267, zip_code)
	c.setFont('times', 8)
	c.drawString(149, 338, year)
	c.drawString(28, 316, "52810")
	c.drawString(263, 338, body)
	c.drawString(150, 316, "Del Mar Motor Cars")
	c.drawString(289, 316, plate)
	c.drawString(474, 316, issue_date)
	c.setFont('times', 16)
	c.drawString(185, 246, odometer[0])
	c.drawString(206, 246, odometer[1])
	c.drawString(227, 246, odometer[2])
	c.drawString(255, 246, odometer[3])
	c.drawString(276, 246, odometer[4])
	c.drawString(296, 246, odometer[5])
	c.save()
	
	pdfs = ['newfile.pdf', 'newfile2.pdf']

	merger = PdfFileMerger()

	for pdf in pdfs:
		merger.append(pdf)

	merger.write("../pdf/"+plate+".pdf")
	merger.close()	
	
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Issue Date: '+issue_date)],
            [sg.Text('Expiration Date: '+expiration_date)],
            [sg.Text('Vehicle Year:')],
            [sg.InputText()],
            [sg.Text('Make:')],
            [sg.InputText()],
            [sg.Text('VIN:')],
            [sg.InputText()],
            [sg.Text('Body Style:')],
            [sg.InputText()],
            [sg.Text('Model:')],
            [sg.InputText()],
            [sg.Text('Owner:')],
            [sg.InputText()],
            [sg.Text('Address:')],
            [sg.InputText()],
            [sg.Text('City:')],
            [sg.InputText()],
            [sg.Text('State:')],
            [sg.InputText()],
            [sg.Text('Zip Code:')],
            [sg.InputText()],
            [sg.Text('Odometer Reading:')],
            [sg.InputText()],
            [sg.Button('Generate'), sg.Button('Close')] ]

# Create the Window
window = sg.Window('Plates Generator', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Close': # if user closes window or clicks cancel
        break
    if event == 'Generate':    
    	generatePDF(values[0], values[1], issue_date, expiration_date, values[2], major_color, minor_color, values[3], values[4], values[5], values[6], values[7], values[8], values[9], expiration_month, expiration_year, values[10])
window.close()