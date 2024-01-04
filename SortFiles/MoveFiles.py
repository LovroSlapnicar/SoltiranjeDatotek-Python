import os
import shutil

path = "C:\\Users\\Lovro\\Downloads"
Folder = os.scandir(path)
Folders = {"Slike":[ ".png", ".bmp", ".webp", ".jpeg", ".gif", ".jpg", ".ico"],"Dokumenti":[".txt",".pdf",".docx",".xml",".vsdx",".pptx",".xlsx",".doc"],"Executables":[".exe",".bat",".msi"],"Zipped":[".7zip",".iso",".zip",".rar"],"torrenti":[".torrent"],"Video":[".mp4",".avi",".wmv",".flv",".webm",".avchd",".mov"],"Zvok":[".mp3",".aac",".flac",".alac",".wav",".aiff",".dsd"],"3D modeli":[".glb",".blend"],"Projekti":[".csproj",".py",".prproj",".json",".html"],"Random":[".jar",".otf",".ttf",".vdi",".whl",".qmod",".wld",".bplist",".dll"]}

def FolderMaker():
    for FolderName in Folders:
        if os.path.exists(path+"\\"+str(FolderName))==False:
            os.mkdir(path+"\\"+str(FolderName))
            print("Created Folder "+str(FolderName)+"!")
FolderMaker()

def FileMover():
    for file in Folder:
        for FolderName in Folders:
            for dat in Folders[FolderName]:
                if dat in file.name:
                    shutil.move("C:\\Users\\Lovro\\Downloads\\"+str(file.name),"C:\\Users\\Lovro\\Downloads\\"+str(FolderName)+"\\"+str(file.name))
FileMover()

#Made by Lovro Slapničar 03.01.2024 