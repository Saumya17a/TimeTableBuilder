import urllib
from bs4 import BeautifulSoup
import  requests
from slimit.parser import Parser
from slimit.visitors import nodevisitor
from slimit import ast
import jsbeautifier
import xlwt 
from datetime import datetime
from xlwt import Workbook 
import  xlsxwriter
import itertools 
import p14 as p
import sqlite3

#this function checks all sequences and checks the one which have time clash
def timeclash(combo):
    flag=0
    combo_new=list()
    comm=sqlite3.connect('database.db')
    for temp in combo:
        l=temp.split(',')
        table=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],
        [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],
        [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],
        [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        table[0][0]=99
        for a in l:
            curr=comm.cursor()
            atemp=int(a)
            curr.execute("SELECT TIME FROM INFO WHERE (CRN =? )", [a])
            time=curr.fetchall()
            ltemp=p.realtime(time)
            tstart=ltemp[0]
            tend=ltemp[1]
            curr.execute("SELECT DAY FROM INFO WHERE (CRN =? )", [a])
            day=curr.fetchall()
            daytemp=p.days(day)
            #table=[[0]*6]*40

            for d in daytemp:
                ttemp=tstart
                if(d=='MONDAY'):
                    index_day=0
                elif(d=='TUESDAY'):
                    index_day=1
                elif(d=='WEDNESDAY'):
                    index_day=2
                elif(d=='THURSDAY'):
                    index_day=3
                elif(d=='FRIDAY'):
                    index_day=4
                #print(tstart)
                #print(tend)

                while(ttemp<tend):
                    if(ttemp==8):
                        index_time=0
                    if(ttemp==8.5):
                        index_time=1
                    if(ttemp==9):
                        index_time=2
                    if(ttemp==9.5):
                        index_time=3
                    if(ttemp==10):
                        index_time=4
                    if(ttemp==10.5):
                        index_time=5
                    if(ttemp==11):
                        index_time=6
                    if(ttemp==11.5):
                        index_time=7
                    if(ttemp==12):
                        index_time=8
                    if(ttemp==12.5):
                        index_time=9
                    if(ttemp==1):
                        index_time=10
                    if(ttemp==1.5):
                        index_time=11
                    if(ttemp==2):
                        index_time=12
                    if(ttemp==2.5):
                        index_time=13
                    if(ttemp==3):
                        index_time=14
                    if(ttemp==3.5):
                        index_time=15
                    if(ttemp==4):
                        index_time=16
                    if(ttemp==4.5):
                        index_time=17
                    if(ttemp==5):
                        index_time=18
                    if(ttemp==5.5):
                        index_time=19
                    if(ttemp==6):
                        index_time=20
                    if(ttemp==6.5):
                        index_time=21
                    if(ttemp==7):
                        index_time=22
                    if(ttemp==7.5):
                        index_time=23
                    info=table[index_time][index_day]
                    if(info!=0):
                        flag=-1
                        #print('breaking 1')
                        break
                    else:
                        table[index_time][index_day]=1   
                        
                    ttemp=ttemp+0.5
                if(flag==-1):
                    #print('breaking 2')
                    break
                #print(table)
        if(flag==-1):
            flag=0
            #print('continue')
            #continue
        else:
            #print('adding')
            combo_new.append(temp)   
        #print(table)        
    comm.commit()
    comm.close() 
    return combo_new




# def insert(sub, time, crn):
#     table= sqlite3.connect(table.db)
    

#     table.commit()
#     table.close()


def delete():
    table= sqlite3.connect(table.db)
    cursor=table.cursor()
    cursor.execute('''DELETE FROM ranking WHERE ()''')
    table.commit()
    table.close()


def ranking(list_of_crn):
    q1_type= input("Are you an morning person? (y/n)")
    q2_frequency= input(" Do you like back to back classes? (y/n)")
    q3_holidays= input("Do u want to try a particular day to be free?  (y/n)")
    q1_count=0
    q2_count=0
    q3_count=0
    table= sqlite3.connect(ranking.db)
    cursor=table.cursor()
    cursor.execute('''CREATE TABLE ranking(Subject TEXT, Time Text, CRN TEXT)''')
    table.commit()
    table.close()
    time_start_list=[]
    item_list=[]  #will store all the items from INFO that is to be transfered to new table
    crn_list_individual=[]
    conn= sqlite3.connect('database.db')
    curr= conn.cursor()
    for i in list_of_crn:
        for j in i:
            crn_list_individual+=j      #makes a list of crns after timeclash
    for k in crn_list_individual:
        curr.execute("SELECT * from INFO where CRN= ?",k)
        item_list=curr.fetchall()
    for m in item_list:
        cursor.execute("INSERT ")
    cursor.execute("SELECT TIME FROM INFO ")
    time_start_list=cursor.fetchall()
    print(time_start_list)
    #for time in time_start_list:
        

#This function uses the combo function to make all combinations  Author-vibhu
def seperator(l,combo):
    conn=sqlite3.connect('database.db')
    curr=conn.cursor()
    i=0
    for temp in l:
        combo_temp=[]
        curr.execute("SELECT CRN FROM INFO WHERE (NAME= ? AND TYPE ='Lab') ",[temp])
        lab=curr.fetchall()
        curr.execute("SELECT CRN FROM INFO WHERE (NAME= ? AND TYPE ='Tutorial') ",[temp])
        tutorial=curr.fetchall()
        curr.execute("SELECT CRN FROM INFO WHERE (NAME= ? AND TYPE ='Lecture') ",[temp])
        lecture=curr.fetchall()
        n=0
        l1=[]
        lab2=[]
        tutorial2=[]
        while(True):
            if(n<len(lecture)):                
                l1.append(str(lecture[n][0]))
            if(n<len(lab)):                
                lab2.append(str(lab[n][0]))
            if(n<len(tutorial)):                
                tutorial2.append(str(tutorial[n][0]))
            if(n>=len(lecture) and n>=len(tutorial) and n>len(lab)):
                break
            n=n+1
        lecture=l1
        lab=lab2
        tutorial= tutorial2
        #print(type(lecture[0]))
        if(i==0):
            if(lecture!=None):
                combo=lecture
                if(lab!=None):
                    p.combinations(lab,combo,combo_temp)
                    combo=combo_temp
                if(tutorial!=None):
                    p.combinations(tutorial,combo,combo_temp)
                    combo=combo_temp
            elif(lab!=None):
                combo=lab
                if(lecture!=None):
                    p.combinations(lecture,combo,combo_temp)
                    combo=combo_temp
                if(tutorial!=None):
                    p.combinations(tutorial,combo,combo_temp)
                    combo=combo_temp
            else:
                combo=tutorial
                if(lecture!=None):
                    p.combinations(lecture,combo,combo_temp)
                    combo=combo_temp
                if(lab!=None):
                    p.combinations(lab,combo,combo_temp)
                    combo=combo_temp
            
        else:
            if(lecture!=None):
                p.combinations(lecture,combo,combo_temp)
                combo=combo_temp
            if(lab!=None):
                p.combinations(lab,combo,combo_temp)
                combo=combo_temp
            if(tutorial!=None):
                p.combinations(tutorial,combo,combo_temp)
                combo=combo_temp
        i=i+1
   
    conn.commit()
    conn.close()
    return combo
        
crnl=[]
def assembler():
    ans= 'y'
    n=0
    name=[]
    crn_Combination=[]  
    while(ans=='y'):
        crsname=input("Enter Course Name")
        crsnum=input("Enter Course Number")
        name_temp=crsname+' '+crsnum
        name.append(name_temp)
        #print(name_temp)
        url=p.urlmaker(crsname,crsnum)
        list1=[]
        date=[]
        place=[]
        day=[]
        typec=[]
        time1=[]
        crn1=[]
        crn_temp=[]
        p.crn(url,crn1)
        p.listmaker(list1,url)
        p.lister(list1,date,place,time1,day,typec)  
        #print(time1)  
        p.sql(place,time1,day,typec, crsname,crsnum,crn1 )
        n=n+1
        ans=input("If you want to continue enter 'y'")
    crn_Combination= seperator(name,crn_Combination)
    combo_new=[]
    print(crn_Combination)
    combo_new=timeclash(crn_Combination)
    print('after')
    print(combo_new) #use this, it has the correct combination.
    ranking(combo_new)
assembler()