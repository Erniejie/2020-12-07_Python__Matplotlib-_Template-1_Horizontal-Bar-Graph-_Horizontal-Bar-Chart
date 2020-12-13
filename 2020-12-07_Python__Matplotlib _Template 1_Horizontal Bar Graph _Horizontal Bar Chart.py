#Python__Matplotlib _Template 1_Horizontal Bar Graph _Horizontal Bar Chart

import matplotlib.pyplot as plt

Major = ["Soil Mechanics","Structural Analysis","Hydraulics","Pystructures"]
Enrolled= [300,500,700,1000]

c = ["yellow","red","green","orange"]

##EXPLANING  : HORIZONTAL BAR SYNTAX:
"""bar(y,width,height = #,left =None,align ="center",**kwargs)"""


#plt.barh(Major,Enrolled,height =0.4,color=c)   # for a constat height =0.4
#plt.barh(Major,Enrolled,0.4,color=c)   # also valid
plt.barh(Major,Enrolled,[0.3,0.5,0.6,0.8],color=c)
#plt.barh(Major,Enrolled,height =[0.9,0.5,0.6,0.7],color=c) # also valid

plt.xlabel("Number of Students")
plt.ylabel("Academic Program")
plt.title("2021 STUDENT TAKE")
plt.show()
