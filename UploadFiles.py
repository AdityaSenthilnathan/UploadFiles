import sys
import os
import dropbox
from dropbox.files import WriteMode


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    
    def uploadFiles(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        
        for root, dirs, files in os.walk(file_from):
            files.pop(0)
            for file in files:
                local_path = os.path.join(root, file)
                print(local_path + " local path")
                fullPath = os.path.join(root, file)
                #print(file_from + "    file from name    " + file)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                #print(relative_path + "-- relative path")
                print(dropbox_path + "-- dropbox path")
                print(fullPath +"-- fullpath")
                with open(fullPath, 'rb') as f:
                  # dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))
                  print(f.read())
                  dbx.files_upload(f.read(),dropbox_path, mute=True)
                    
            
transferData = TransferData("sl.A_kf6FbzHjQG4j3cZSpPqRTfupNUl4ENs5ZNamT9VvZmt7irf6W6Pg00ZxpPqOru4RzECjkdKuepmGgr0uL98qPKI7VEooz88m37LN9yyj0mnOYhaogGVcqdL9wJDTIz0gcP5Ow")
transferData.uploadFiles("/Users/Aditya/Documents/Folder1", "/Folder1")