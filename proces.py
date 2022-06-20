#############################################################################################
#
#   Application :Periodic process logger with Auto scheduling LOg report facility.
#   Description :It is used to provide the information about PID,Username,name,and memory usage.
#   Functions   :1.Entry functtion, 2.ProcessDisplay, 3.Pack and mailsender
#   Input       :Directory.
#   output      :Log report of process running on syetem.
#   Author      :Chandan Vijay Bavne
#
#############################################################################################


#Required Packages import
from sys import *
import os
import psutil
import time
import schedule
import smtplib
from email.message import EmailMessage

#############################################################################################

# Function to get the p[rocess information.
def ProcessDisplay(FolderName="ProcessLog"):
    """
    Function:ProcessDisplay()
    it is used to create directory and file for regural report.
    input:dircetory
    output:Directory and log file creation.
    Pass the log file path to mail seder function.
    """
    if not os.path.exists(FolderName):      #check directory present
        os.mkdir(FolderName)                #if not presnt create
    
    FilePath=os.path.join(FolderName,"LogReport%s.txt"%time.ctime())# create path to create log file.
    FilePath=FilePath.replace(":"," ")
    fd=open(FilePath,'a')               # create log file.

    Data=[]                     #create empty list for processs information.
    
    for proc in psutil.process_iter():  #get the process information.
        value=proc.as_dict(['pid','username','name'])
        Data.append(value)
    for i in Data:
        fd.write("%s\n"%i)      # write a process information in to file

    MemoryUsage=str(psutil.virtual_memory())   # information about memory usage.
    fd.write(f"information about memory usage{MemoryUsage}")
    fd.close()
    MailSender(FilePath)       # call a function to send mail.
     
#########################################################################################

     
# Function is used to send mail.
def MailSender(FilePath):
    """
    Function is used to send mail.
    Input:Filepath
    output:senmail with log file attachment.
    """
    
    Mail=EmailMessage()         # object of EmailMessage.
    Mail['subject']="Log report of processes running on system and its application"
    Mail['from']="chandan"
    Mail['To']='harishbavne@gmail.com'              # receiver mail id.
    
    with open("msg.txt") as txt:             # draft template file.
        text=txt.read()
        Mail.set_content(text)                      #Draft.
    
    with open(FilePath,'rb')as LogFile:
           FileName=LogFile.name
           Data=LogFile.read()
           Mail.add_attachment(Data,maintype="Log File",subtype="txt",filename=FileName)
           # attach attachment
            
            
    server=smtplib.SMTP_SSL("smtp.gmail.com",465)   #SMTP server 
    server.login("chandanbavne@gmail.com","furygxxccneemmcr")       # login credential.(sender mail id& password)
    server.send_message(Mail)                        #send mail   
    server.quit()
    
#############################################################################################
#Entry function:

def main():
    print("******** log report of process running on system***************")
    if(len (argv)<2):
        print("Insufficient arguments")
    print("Application file name is:",argv[0])
    
    if((argv[1]=="-u") or(argv[1]=='-U')):
        print("usage: Application_name Shedule_Time Directory_Name")
        
    if((argv[1]=='-h')or(argv[1]=='-H')):
        print("Help: It is used to create log file of running processess")
        
    schedule.every(int(argv[1])).minutes.do(ProcessDisplay) #schedular
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        
#############################################################################################

#main starter

if __name__=="__main__":

    main()
 
############################################################################################# 

