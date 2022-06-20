##############################################################################################
#   Appilication: File packer.
#   Description : It is used to pack files into single file.
#   Functions   : 1.Entry Function, 2.Filepacker,3.Pack,4.CreateFile.
#   Input       : Directory, file name.
#   output      : Packed data of many files into one file.
#   Author      : Chandan Vijay Bavne . 
#############################################################################################

# Required python packages
import os
import pathlib
#############################################################################################

#Function to travel directory
def Filepacker(Directory,Name):
       """
       function is used to travel Directory to get the file names.
       Parameter:Directory to travel, string for output file name.
       
       """
       
       Extension=[".txt",".c",".cpp",".java",".py"]
       path=os.getcwd()
       Filepath=os.path.join(path,Name)
       print(Filepath) 
       fd=CreateFile(Filepath)          #call CreateFile function to creat outputfile
       Count=0
       for Folder,Subfolder,Filename in os.walk(Directory):
        
            for file in Filename:
                ext=pathlib.Path(file).suffix
            
                if (ext in Extension):              #to check extenstion
                    Count=Count+1
                    name=os.path.join(Directory,file)
                    size=os.path.getsize(name)
                    Pack(name,size,Filepath)        # call to pack function for packing file into one file
       print(f"{Count} file are packed.")
       fd.close()
                
#############################################################################################            
#Function to pack files in one File.
def Pack(FileN,size,outfile):
      """
      function is used to pack file into output file with its name and size.
      Parameter:1.filename whcih get packed,2.size of that file and 3.combine file
      """
      fdout=open(outfile,"a")       # open output file in append mode
      fdin=open(FileN,"r")       #open input file in read mode
      Filename=os.path.basename(FileN)
      print(Filename) 
      Header=(Filename+" "+str(size))   # Header string is created.
      Data=fdin.read()
      n=len(Header)
      
      for i in range(n+1,101):
            Header=Header+" "           #add space in header
            
      
      fdout.write(Header)              #write header in outputfile.
      fdout.write(Data)                 #write Date into output file.   
      fdout.close()
      fdin.close() 

############################################################################################################
#function to create file

def CreateFile(Filepath):

    """
    Function is used to create output file.
    Parameter: Filepath to create output file.
    Return: output file.
    """
    
    return open(Filepath,"a")
#############################################################################################
    
# Entry function.
def main():
    """
    
    Entry Function.
    Input: Takes Directory name and string for output file for file name from user.
    """
    Directory=input("Enter a folder name:")
    Name=input("Provide file name for packing:")
    Filepacker(Directory,Name)          # call function(Filepacker)
    
#############################################################################################

#main starter.
if __name__=="__main__":
    print("Functions details",main.__doc__)
    print("function Filepacker:",Filepacker.__doc__)
    print("function CreateFile:",CreateFile.__doc__)
    print("function Pack:",Pack.__doc__)
    
    main()

#############################################################################################    
