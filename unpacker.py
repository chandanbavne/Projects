#############################################################################################
#   Appilication:File unpacker.
#   Description: it is used to unpack files from given file into separate files.
#   Functions:1.Entry function,2.Fileunpacker & 3.UnpackFile.
#   input:  File name.
#   output:Unpack files into separate files.
#   Author:CHandan Vijay Bavne 
#
#############################################################################################


#Required python package

import os
import pathlib

############################################################################################

# function is used to get File name and its size to unpack.
def Fileunpacker(File):

    """
    function is used to get file name & its size to unpack.
    parameter:file path to unpack.
    """
    
    fd=open(File,"rb")                           #open i/p file in read binary mode.
    Readoffset=0                                 #readoffset counter.
    Filesize=os.path.getsize(File)               #get size of file.    
    Count=0                                      #to count no of files to unpacked.
    while(Filesize>Readoffset):
        Count=Count+1
        Header=fd.read(100)                     #read header to get packed file nameand size.
        Header=Header.decode('utf8').strip()    #Convert Header into string and remove spaces(trailing and leading)
        
        Name,size=Header.split(" ")             # get file name & size to create unpack file
        
        UnpackFile(Name,size,fd)                # call unpackfunction.
        Readoffset=fd.tell()                    #update Readoffset Conter.
    
    fd.close()
    print(f"{Count} files are unpacked.")
        
#############################################################################################
# function is used to create unpack file.

def UnpackFile(Name,size,fd):
    """
    function is used to create new file top retrive data from pack file.
    parameter:file name=to create unpacked file,,size=to read number of bytes and packed file name
    """
    outFile=open(Name,'wb')         #create file in write binary mode
    Data=fd.read(int(size))         #get data in specific byte
    outFile.write(Data)              #write data in file   
    outFile.close()

#############################################################################################

#Entry function.
def main():
    """
       Entry Function.
       Input:File name from user to unpack file and retrive original files.
    """
    File=input("Enter  file name:")
    Fileunpacker(File)
    
############################################################################################    

#main starter
if __name__=="__main__":
    
    print("function main:",main.__doc__)
    print("function Fileunpacker:",Fileunpacker.__doc__)
    print("function UNpackFile:",UnpackFile.__doc__)
    
    main()

#############################################################################################    