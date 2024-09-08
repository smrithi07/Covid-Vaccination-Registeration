                    #SRIRAMAJAYAM
import random
import pickle
import os

#CONDITIONS
from datetime import date,timedelta
t=date.today()

def ctd(a,b,c):
	dat=date(a,b,c)
	return dat

def ldate(x):
	y=int(x[0])
	m=int(x[1])
	d=int(x[2])
	return ctd(y,m,d)


def book():
        print()
        doseno=int(input("Dose no: (1/2) "))
        vaxlist=["1.Covaxin","2.Covishield","3.Sputnik"]
        print("Vaccines available: ")
        for i in vaxlist:
                print("\t\t\t",i)
        vno=int(input("Enter vaccine of choice: "))
        vac=vaxlist[vno-1][2:]
        vdate=t+timedelta(10)
        f={"Dose no": doseno, "Vaccine chosen": vac, "Date of vaccination": vdate}
        return f        
    
    
def covidpast(x):
        print()
        covidpast=input("""Have you been affected by covid before?
                    Press y for yes, n for no, x for not sure """)
        if covidpast=="n":
                g=book()
                return g
        elif covidpast=="x":
                test=input("  Antibody test taken?:(y/n)")
                if test=="n":
                        symptoms=input("\tDid you have any symptoms in the past week?:(y/n)")
                        if symptoms=="y":
                                print("\tTake test and come back")
                                exit
                        else:
                                g=book()
                                return g
            
                else:
                        result=input("""\tIs the test result +ve(p) or -ve(n)?
                                Press p for positive, n for negative """)
                        if result=="p":
                                dat=input(" \tEnter date of test taken(y-m-d): ")
                                da=ldate(dat.split('-'))
                                if (t-(da+timedelta(84))).days >=0:
                                        g=book()
                                        return g
                                else:
                                        print(" \tVisit from 84 days after test date ")
                                        exit
                        else:
                                g=book()
                                return g
        else:
                dat=input("  Enter date of recovery[y-m-d]: ")
                da=ldate(dat.split('-'))
                if (t-(da+timedelta(48))).days >=0:
                        g=book()
                        return g
                else:
                        print("Come after 48 days")
                        exit

def Ariyamangalam():
        Lm=["1.JOSEPH EYE HOSPITAL, MELAPUDUR", "2.APOLLO SPECIALITY HOSPITAL"]
        for i in Lm:
                print("\t\t",i)
        hno=int(input("Enter the hospital no. chosen:"))
        return Lm[hno-1]
def Abishekapuram():
    La=["1.TRICHY MEDICAL SERVICES","2.KAVERY MEDICAL CENTRE AND HOSPITAL", "3. A.J.HOSPITAL","4.JEYAM MULTISPECIALITY HOSPITAL","5.AMRISH ONCOLOGY","6.GITANJALI MEDICAL CENTRE","7.DR.G.VISWANATHAN SPECIALITY HOSPITALS","8.SMS HOSPITAL","9.STAR KIMS HOSPITALS","10.AIYSHWARIYA HOSPITAL","11.TRICHY SRM MEDICAL COLLEGE HOSPITAL AND RESEARCH CENTRE","12.VASAN EYE CARE","13.APOLLO HOSPITALS","14.MANGALAM HOSPITAL","15.SUGAM HOSPITAL","16.DAYAL NURSING HOME","17.SUNDARAM HOSPITAL","18. C.S.I. MISSION HOSPITAL","19.CETHAR HOSPITAL","20.ANANTHGIRI NURSING HOME","21.RETNA GLOBAL HOSPITAL","22.Q MED HOSPITAL","23.A G EYE HOSPITAL","24.ROYAL PEARL HOSPITAL","25.ATHREYA RETINAL CENTER","26.RATHNA MEDICAL CENTRE","27.KMC SPECIALITY","28.DEEPAN NURSING HOME","29.HARSHAMITRA SUPER SPECIALITY CANCER CENTRE"]
    for i in La:
        print("\t\t",i)
    hno=int(input("\nEnter the hospital no. chosen: "))
    return La[hno-1]

def Srirangam():
        Ls=["1.G V N HOSPITAL PVT LTD","2.ATLAS HOSPITAL","3.FRONTLINE HOSPITAL"]
        for i in Ls:
                print("\t\t",i)
        hno=int(input("Enter the hospital no. chosen:"))
        return Ls[hno-1]      

def GoldenRock():
        Lg=["1. DR.MALAS HOSPITAL","2.GKM HOSPITAL","3.SINDUJA HOSPITAL","4.MARUTI HOSPITAL","5.SRI KUMARAN HOSPITAL","6.VELAN SPECIALITY HOSPITALS PVT HOSPITAL"]
        for i in Lg:
                print("\t\t",i)
        hno=int(input("Enter the hospital no. chosen:"))
        print()
        return Lg[hno-1]




def register():
        dreg={}
        name=input("Enter your name: ")
        gender=input("""Enter your gender:
m or f or t """)
        byear=int(input("Enter year of birth: "))
        age=2021 - byear
        if age not in range(15,108):
                print("Not eligible for vaccination")
        else:
                idnum=random.randint(10000000,99999999)
                code=int(str(idnum)[len(str(idnum))-4:])
                zns=["Ariyamangalam","Abishekapuram","Srirangam","Golden Rock"]
                print("\nTHE ZONES ARE:  ")
                for i in range(len(zns)):
                        print(str(i+1)+".",zns[i])
                zone=int(input("Enter your zone no: "))
                print("\n\tHOSPITAL LIST:")
                if zone==1:
                        h=Ariyamangalam()
                elif zone==2:
                        h=Abishekapuram()
                elif zone==3:
                        h=Srirangam()
                elif zone==4:
                        h=GoldenRock()
                else:
                        exit
                dreg={"Name":name,"ID Number":idnum,"Code":code,"Gender":gender,"Age":age,"Zone":zns[zone-1],"Vaccination Centre":h}
                v=covidpast("x")
                for j in list(v):
                        dreg[j]=v[j]
                        return dreg


def edit():
        fe=open("redd.dat","rb+")
        dic={}
        codeno=int(input("enter your code to modify:"))
        try:
                while True:
                        pos=fe.tell()
                        dic=pickle.load(fe)
                        if dic['Code']==codeno:
                                e=input("Press H to change hospital")
                                if e=="H":
                                        zns=["Ariyamangalam","Abishekapuram","Srirangam","Golden Rock"]
                                        print("\nTHE ZONES ARE:  ")
                                        for i in range(len(zns)):
                                            print(str(i+1)+".",zns[i])
                                        zone=int(input("Enter your zone no: "))
                                        print("\n\tHOSPITAL LIST:")
                                        if zone==1:
                                                ho=Ariyamangalam()
                                        elif zone==2:
                                                ho=Abishekapuram()
                                        elif zone==3:
                                                ho=Srirangam()
                                        elif zone==4:
                                                ho=GoldenRock()    
                                        if zns[zone-1]!=zone:
                                                dic["Zone"]=zns[zone-1]
                                                dic["Vaccination Centre"]=ho
                                        fe.seek(pos)
                                        pickle.dump(dic,fe)
                                        print("Changes are successful\n","Plese refer to the new registration.")
                                        
        except EOFError:
                fe.close()
def show():
        fi=open("redd.dat","rb")
        k={}
        cd=int(input("Enter your code:"))
        try:
                while True:
                        k=pickle.load(fi)
                        if k["Code"]==cd:
                                for i in k.items():
                                        print(i[0]," - ", i[1])
                                        
        except EOFError:
                fi.close()
def cancel():
        fo=open("redd.dat","rb")
        fd=open("temp.dat","wb")
        do={}
        dn=int(input("Enter your code number to cancel:"))
        try:
                while True:
                        do=pickle.load(fo)
                        if do['Code']!=dn:
                                pickle.dump(do,fd)
                                print("\t\t\t Registeration Cancelled.")        
        except EOFError:
                fo.close()
                fd.close()
        os.remove("redd.dat")
        os.rename("temp.dat","redd.dat")
        




print("\t\t\t\t  PYTHON PACKAGE")
print("""\nDONE BY:
                ANUVARSANA - 22PD06
                SMRITHI L  - 22PD33""")
print("\nAMCS DEPARTMENT")
print("\n DATA SCIENCE")
print("\n PSG COLLEGE OF TECHNOLOGY ")
print("\n\n\t\t\tDHANVANTHRI VACCINE REGISTRATION")

while True:
    print("""Services provided:
                1.Registration
                2.Modification
                3.Display
                4.Cancellation""")

    user_input=int(input("Enter your choice of procedure: "))
    print()
    if user_input==1:
        file=open("redd.dat","ab+")
        a=register()
        x=a.items()
        print("Check your details and note the code.")
        print("\n\n\t\t\t")
        for i in x:
                print("\t\t\t",i[0]," - ", i[1])
        print()
        pickle.dump(a,file)
        file.close()
    elif user_input==2:
            edit()
    elif user_input==3:
            show()
    elif user_input==4:
            cancel()
    else:
            print("Invalid choice, kindly try again")
            admin=int(input("Enter your personal code:"))
            if admin==101725:
                    fi=open("redd.dat","rb")
                    k={}
                    try:
                            while True:
                                    k=pickle.load(fi)
                                    for i in k.items():
                                            print(i[0]," - ", i[1])
                    except EOFError:
                            fi.close()
                   

    cont=input("\n\nDo you want to continue(y/n): ")
    if cont=="y":
        pass
    elif cont=="n":
        print("""\n\n\n\t\t  THANK YOU FOR WORKING WITH US
                        STAY HOME. STAY SAFE
                            JAI HIND""")
        break
    else:
        break



