# from asyncore import write #this one came automatically
import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root ,dirs ,files in os.walk(file_from):
            for filename in files:
                    #construct the full local path
                local_path = os.path.join(root, filename)

                    #Construct the full dropbox path
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to ,relative_path)
                    #upload the file
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))
def main():
    # To access dropbox to upload files
    access_token = 'sl.BNvV28fdnPS1dNkGEmL9mzGxdTzZCJaZ_qC4m9TZqDfCYMsOhkeTTnjZBOy0rOTxnvrEc2LdXLpIKM-airWREF_WTZdtr1CyQ3RJWsJQvYuoLz7tpSIqWGix4I6L_YHTLdTFDf4'
    # Transferring file through access token
    transferData = TransferData(access_token)

    # This is the full path to upload on dropbox
    file_from = input("Enter full File path which has to be uploaded: ")
    file_to = input("Enter the full path to upload on dropbox: ") 

    #transfer file by taking path through file_from then uploading to dropbox through file_to.
    transferData.upload_file(file_from,file_to)
    print("File has been moved!")

main()