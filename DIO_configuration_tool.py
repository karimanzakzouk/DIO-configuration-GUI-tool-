
################################################################################
## Form generated from reading UI file 'DIO_configuration.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
################################################################################

import sys
import os

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt , SIGNAL)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


pins=[]
ports=[]
directions=[]
types=[]
names=[]
value_ddr=[]
value_port=[]
x=0


for s in range(8):
  ports.append("PORTA")
for s in range(8):
  ports.append("PORTB") 
for s in range(8):
  ports.append("PORTC")  
for s in range(8):
  ports.append("PORTD")
  
for x in range(32): 
  pins.append("PIN"+str(x))
  directions.append("OUTPUT")
  types.append("LOW")
  names.append("PIN"+str(x))
  value_ddr.append(1)
  value_port.append(0)
  
  
#print(ports)
#print(pins)
#print(directions)
#print(types)
#print(names)


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(583, 550)
        self.groupBox_tab1 = QGroupBox(Form)
        self.groupBox_tab1.setObjectName(u"groupBox_tab1")
        self.groupBox_tab1.setGeometry(QRect(30, 20, 521, 521))
        self.labelName = QLabel(self.groupBox_tab1)
        self.labelName.setObjectName(u"labelName")
        self.labelName.setGeometry(QRect(50, 250, 47, 20))
        self.groupBox_output = QGroupBox(self.groupBox_tab1)
        self.groupBox_output.setObjectName(u"groupBox_output")
        self.groupBox_output.setGeometry(QRect(190, 120, 271, 61))
        self.high = QRadioButton(self.groupBox_output)
        self.high.setObjectName(u"high")
        self.high.setGeometry(QRect(20, 20, 83, 18))
        self.high.setChecked(False)
        self.low = QRadioButton(self.groupBox_output)
        self.low.setObjectName(u"low")
        self.low.setGeometry(QRect(150, 20, 83, 18))
        self.low.setChecked(True)
        self.groupBox_input = QGroupBox(self.groupBox_tab1)
        self.groupBox_input.setObjectName(u"groupBox_input")
        self.groupBox_input.setGeometry(QRect(190, 190, 271, 61))
        self.Pull_Up = QRadioButton(self.groupBox_input)
        self.Pull_Up.setObjectName(u"Pull_Up")
        self.Pull_Up.setGeometry(QRect(20, 20, 81, 18))
        self.Pull_Up.setCheckable(True)
        self.Pull_Up.setChecked(False)
        self.High_Imp = QRadioButton(self.groupBox_input)
        self.High_Imp.setObjectName(u"High_Imp")
        self.High_Imp.setGeometry(QRect(150, 20, 111, 18))
        self.pin_name_edit_line = QLineEdit(self.groupBox_tab1)
        self.pin_name_edit_line.setObjectName(u"pin_name_edit_line")
        self.pin_name_edit_line.setGeometry(QRect(50, 270, 113, 20))
        self.groupBox_mode = QGroupBox(self.groupBox_tab1)
        self.groupBox_mode.setObjectName(u"groupBox_mode")
        self.groupBox_mode.setGeometry(QRect(50, 120, 120, 80))
        self.input = QRadioButton(self.groupBox_mode)
        self.input.setObjectName(u"input")
        self.input.setGeometry(QRect(10, 40, 83, 41))
        self.output = QRadioButton(self.groupBox_mode)
        self.output.setObjectName(u"output")
        self.output.setGeometry(QRect(10, 20, 83, 31))
        self.output.setChecked(True)
        self.checkBox_defaultName = QCheckBox(self.groupBox_tab1)
        self.checkBox_defaultName.setObjectName(u"checkBox_defaultName")
        self.checkBox_defaultName.setGeometry(QRect(190, 260, 131, 41))
        self.comboBox_PORT = QComboBox(self.groupBox_tab1)
        self.comboBox_PORT.addItem(str())
        self.comboBox_PORT.addItem(str())
        self.comboBox_PORT.addItem(str())
        self.comboBox_PORT.addItem(str())
        self.comboBox_PORT.setObjectName(u"comboBox_PORT")
        self.comboBox_PORT.setGeometry(QRect(50, 50, 62, 22))
        self.comboBox_PORT.setEditable(False)
        self.comboBox_PIN = QComboBox(self.groupBox_tab1)
        self.comboBox_PIN.addItem(str())
        self.comboBox_PIN.addItem(str())
        self.comboBox_PIN.addItem(str())
        self.comboBox_PIN.addItem(str())
        self.comboBox_PIN.addItem(str())
        self.comboBox_PIN.addItem(str())
        self.comboBox_PIN.addItem(str())
        self.comboBox_PIN.addItem(str())
        self.comboBox_PIN.setObjectName(u"comboBox_PIN")
        self.comboBox_PIN.setGeometry(QRect(150, 50, 62, 22))
        self.comboBox_PIN.setEditable(False)
        self.savepinconfig = QPushButton(self.groupBox_tab1)
        self.savepinconfig.setObjectName(u"savepinconfig")
        self.savepinconfig.setGeometry(QRect(340, 270, 121, 21))
        self.path_edit_line = QLineEdit(self.groupBox_tab1)
        self.path_edit_line.setObjectName(u"path_edit_line")
        self.path_edit_line.setGeometry(QRect(40, 430, 241, 31))
        self.labelPath = QLabel(self.groupBox_tab1)
        self.labelPath.setObjectName(u"labelPath")
        self.labelPath.setGeometry(QRect(40, 400, 81, 21))
        self.generate = QPushButton(self.groupBox_tab1)
        self.generate.setObjectName(u"generate")
        self.generate.setGeometry(QRect(320, 430, 151, 31))
        self.save = QPushButton(self.groupBox_tab1)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(340, 330, 121, 31))
        self.new_2 = QPushButton(self.groupBox_tab1)
        self.new_2.setObjectName(u"new_2")
        self.new_2.setGeometry(QRect(190, 330, 121, 31))
        self.load = QPushButton(self.groupBox_tab1)
        self.load.setObjectName(u"load")
        self.load.setGeometry(QRect(40, 330, 121, 31))

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)


        QObject.connect(self.output,SIGNAL("clicked(bool)"),self.groupBox_input.setDisabled)
        QObject.connect(self.input, SIGNAL("clicked(bool)"),self.groupBox_output.setDisabled)
        QObject.connect(self.output,SIGNAL("clicked(bool)"),self.groupBox_output.setEnabled)
        QObject.connect(self.input,SIGNAL("clicked(bool)"),self.groupBox_input.setEnabled)
        QObject.connect(self.checkBox_defaultName,SIGNAL("clicked(bool)"),self.pin_name_edit_line.setDisabled)


        self.savepinconfig.clicked.connect(self.MyHandler1)
        self.generate.clicked.connect(self.MyHandler2)
        self.new_2.clicked.connect(self.MyHandler3)
        self.save.clicked.connect(self.MyHandler4)
        self.load.clicked.connect(self.MyHandler5)

#save pin config
    def MyHandler1(self):
    
        port = self.comboBox_PORT.currentText()
        if port == "PORTA":
          i= self.comboBox_PIN.currentIndex()
          pins[i]="PIN"+str(i)
          ports[i]=self.comboBox_PORT.currentText()
        elif  port == "PORTB": 
          i= self.comboBox_PIN.currentIndex()+8
          pins[i]="PIN"+str(i)
          ports[i]=self.comboBox_PORT.currentText()
        elif  port == "PORTC": 
          i= self.comboBox_PIN.currentIndex()+16
          pins[i]="PIN"+str(i)
          ports[i]=self.comboBox_PORT.currentText()
        elif  port == "PORTD": 
          i= self.comboBox_PIN.currentIndex()+24
          pins[i]="PIN"+str(i)
          ports[i]=self.comboBox_PORT.currentText()
        else:
           None

        if self.output.isChecked():
          directions[i]="OUTPUT"
          value_ddr[i]=1
          if self.high.isChecked():
            value_port[i]=1
            types[i]="HIGH"
          else:
            value_port[i]=0
            types[i]="LOW"

        if self.input.isChecked():
          value_ddr[i]=0
          directions[i]="INPUT"
          if self.Pull_Up.isChecked():
            value_port[i]=1
            types[i]="PULL_UP"
          else:
            value_port[i]=0
            types[i]="High_IMPEDENCE"

        if self.checkBox_defaultName.isChecked():
          names[i]="PIN"+str(i)
        else:
          names[i]=self.pin_name_edit_line.text()
          
        #print("#define "+pins[i] +"        "+directions[i]+"_"+types[i]+"\n")  
        #print("#define "+names[i]+"        "+pins[i]+"\n")


#generate
    def MyHandler2(self):
      j=0
      S=0
      DDRA=0
      DDRB=0
      DDRC=0
      DDRD=0
      PORTA=0
      PORTB=0
      PORTC=0
      PORTD=0
           
      INITIAL_Handler= open(self.path_edit_line.text() + '\Initialization' + '.h', 'w')
      MFIC_Handler= open(self.path_edit_line.text() + '\MFIC' + '.h', 'w')
      DIO_Handler = open(self.path_edit_line.text() + '\DIO_cfg' + '.h' , 'w')

      for s in range(8):
        PORTA = PORTA  + (value_port[s]<<s)
        DDRA = DDRA  + (value_ddr[s]<<s)
        
        PORTB = PORTB  + (value_port[s+8]<<s)
        DDRB = DDRB  + (value_ddr[s+8]<<s)
        
        PORTC = PORTC  + (value_port[s+16]<<s)
        DDRC = DDRC  + (value_ddr[s+16]<<s)
        
        PORTD = PORTD  + (value_port[s+24]<<s)
        DDRD = DDRD  + (value_ddr[s+24]<<s)
    
    
      DIO_Handler.write("\n/**************** pins configurations ******************/\n\n")  
      MFIC_Handler.write("\n/******************** pins names **********************/\n\n")        
      
      for j in range(len(pins)):
     
        DIO_Handler.write("#define  "+pins[j]+"        "+directions[j]+"_"+types[j]+"\n\n")
        #print("#define  "+pins[j]+"        "+directions[j]+"_"+types[j]+"\n")
        
        MFIC_Handler.write("#define  "+names[j]+"       "+pins[j]+"\n\n")
        #print("#define  "+names[j]+"       "+pins[j]+"\n")

     
      INITIAL_Handler.write("\n\n\n/**************** Ports registers initial value ***********************/\n")      
      INITIAL_Handler.write("#define  PORTA"+"        "+ str(PORTA) + "\n")
      INITIAL_Handler.write("#define  PORTB"+"        "+ str(PORTB) + "\n")
      INITIAL_Handler.write("#define  PORTC"+"        "+ str(PORTC) + "\n")
      INITIAL_Handler.write("#define  PORTD"+"        "+ str(PORTD) + "\n")
      
      INITIAL_Handler.write("\n\n\n/**************** Directions registers initial value ******************/\n")
      INITIAL_Handler.write("#define  DDRA"+"        "+  str(DDRA) + "\n")
      INITIAL_Handler.write("#define  DDRB"+"        "+  str(DDRB) + "\n")
      INITIAL_Handler.write("#define  DDRC"+"        "+  str(DDRC) + "\n")
      INITIAL_Handler.write("#define  DDRD"+"        "+  str(DDRD) + "\n")

      #print("#define  PORTA"+"        "+ str(PORTA) + "\n")
      #print("#define  PORTB"+"        "+ str(PORTB) + "\n")
      #print("#define  PORTC"+"        "+ str(PORTC) + "\n")
      #print("#define  PORTD"+"        "+ str(PORTD) + "\n")

      #print("#define  DDRA"+"        "+  str(DDRA) + "\n")
      #print("#define  DDRB"+"        "+  str(DDRB) + "\n")
      #print("#define  DDRC"+"        "+  str(DDRC) + "\n")
      #print("#define  DDRD"+"        "+  str(DDRD) + "\n")
      
      
      MFIC_Handler.close()
      DIO_Handler.close()
      INITIAL_Handler.close()


#new
    def MyHandler3(self):
    
      INITIAL_Handler= open(self.path_edit_line.text() + '\Initialization' + '.h', 'w')
      MFIC_Handler= open(self.path_edit_line.text() + '\MFIC'    + '.h', 'w') 
      DIO_Handler = open(self.path_edit_line.text() + '\DIO_cfg' + '.h' , 'w')
      
      MFIC_Handler.close()
      DIO_Handler.close()
      INITIAL_Handler.close()

#save
    def MyHandler4(self):
      j=0
      backup_Handler= open(self.path_edit_line.text() +'\\backup'+ '.txt', 'w')
      
      for j in range(len(pins)):
        backup_Handler.write(pins[j]+","+directions[j]+","+types[j]+","+names[j]+"\n")
        #print(pins[j]+","+directions[j]+","+types[j]+","+names[j]+"\n")
      
      backup_Handler.close()  

        
#load
    def MyHandler5(self):
      u=0
      l=[]
      backup_Handler= open(self.path_edit_line.text() +'\\backup'+ '.txt', 'r')
      
      list = backup_Handler.readlines()
      
      for line in list:
         l= line.rstrip().split(',')
         pins[u]=l[0]
         directions[u]=l[1]
         types[u]=l[2]
         names[u]=l[3]
         
         #print(pins[u]+","+directions[u]+","+types[u]+","+names[u]+"\n")
         u=u+1 
      backup_Handler.close()   


    #setupUi
    def retranslateUi(self, Form):
    
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox_tab1.setTitle(QCoreApplication.translate("Form", u"Pin configeration", None))
        self.labelName.setText(QCoreApplication.translate("Form", u"Pin Name", None))
        self.groupBox_output.setTitle(QCoreApplication.translate("Form", u"Output Cfg", None))
        self.high.setText(QCoreApplication.translate("Form", u"High", None))
        self.low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.groupBox_input.setTitle(QCoreApplication.translate("Form", u"Input Cfg", None))
        self.Pull_Up.setText(QCoreApplication.translate("Form", u"Pull Up", None))
        self.High_Imp.setText(QCoreApplication.translate("Form", u"High Impedence", None))
        self.pin_name_edit_line.setText(QCoreApplication.translate("Form", u"Enter Pin Name", None))
        self.groupBox_mode.setTitle(QCoreApplication.translate("Form", u"Mode", None))
        self.input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.checkBox_defaultName.setText(QCoreApplication.translate("Form", u"Use Default Name", None))
        self.comboBox_PORT.setItemText(0, QCoreApplication.translate("Form", u"PORTA", None))
        self.comboBox_PORT.setItemText(1, QCoreApplication.translate("Form", u"PORTB", None))
        self.comboBox_PORT.setItemText(2, QCoreApplication.translate("Form", u"PORTC", None))
        self.comboBox_PORT.setItemText(3, QCoreApplication.translate("Form", u"PORTD", None))

        self.comboBox_PORT.setCurrentText(QCoreApplication.translate("Form", u"PORTA", None))
        self.comboBox_PIN.setItemText(0, QCoreApplication.translate("Form", u"PIN0", None))
        self.comboBox_PIN.setItemText(1, QCoreApplication.translate("Form", u"PIN1", None))
        self.comboBox_PIN.setItemText(2, QCoreApplication.translate("Form", u"PIN2", None))
        self.comboBox_PIN.setItemText(3, QCoreApplication.translate("Form", u"PIN3", None))
        self.comboBox_PIN.setItemText(4, QCoreApplication.translate("Form", u"PIN4", None))
        self.comboBox_PIN.setItemText(5, QCoreApplication.translate("Form", u"PIN5", None))
        self.comboBox_PIN.setItemText(6, QCoreApplication.translate("Form", u"PIN6", None))
        self.comboBox_PIN.setItemText(7, QCoreApplication.translate("Form", u"PIN7", None))

        self.savepinconfig.setText(QCoreApplication.translate("Form", u"Save Pin Configuration", None))
        self.path_edit_line.setText(QCoreApplication.translate("Form", u"C:\\Users\\kimoz\\Desktop\\DIO3\\PY3", None))
        self.labelPath.setText(QCoreApplication.translate("Form", u"Output Path", None))
        self.generate.setText(QCoreApplication.translate("Form", u"Generate", None))
        self.save.setText(QCoreApplication.translate("Form", u"Save", None))
        self.new_2.setText(QCoreApplication.translate("Form", u"New", None))
        self.load.setText(QCoreApplication.translate("Form", u"Load", None))



app = QApplication(sys.argv)
Widget = QWidget()
Form = Ui_Form()
Form.setupUi(Widget)
Widget.show()
sys.exit(app.exec_())

