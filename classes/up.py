import ftplib
from io import BytesIO

def whoname(BData):
    if BData == "tzzpxH8vOS9QZ8CPIyAAl95nJYfskzKSbNNpCT1pIBs=":
        BData = "Mamdouh Abdullah Alanazi"
    elif BData == 'i1NMUksRt6fVjciJFI+yKiR2wcX570xHE25hsEepeEo=':
        BData = "Abdullah Eissa Alanazi"
    elif BData == 'fdhsgreertwbfgdhsrew':
        BData = "Moath Abdallah AlFayez"
            
    return BData

def sendtoFTP(filenamesend,buffer):
    FTP_HOST = "192.168.1.8"
    FTP_USER = "ftpuser"
    FTP_PASS = "ftppass"
    ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
    ftp.encoding = "utf-8"


    flo = BytesIO(buffer)
    folderName = 'CTI'
    if folderName in ftp.nlst():
        ftp.storbinary(f'STOR /CTI/{filenamesend}', flo)
    else:
        ftp.mkd("CTI")
        ftp.storbinary(f'STOR /CTI/{filenamesend}', flo)


    # use FTP's STOR command to upload the file
        #ftp.storbinary(f"STOR {filenamesend}", flo)
    
    # list current files & directories
    #ftp.dir()
    ftp.quit()
    
def sendData(filenamesend):
    FTP_HOST = "192.168.1.8"
    FTP_USER = "ftpuser"
    FTP_PASS = "ftppass"
    ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
    ftp.encoding = "utf-8"
    
    file = open(filenamesend,'rb')                  # file to send

    folderName = 'CTI'
    if folderName in ftp.nlst():
        ftp.storbinary(f"STOR {filenamesend}", file)
    else:
        ftp.mkd("CTI")
        ftp.storbinary(f"STOR {filenamesend}", file)


    # use FTP's STOR command to upload the file
        #ftp.storbinary(f"STOR {filenamesend}", flo)
    
    # list current files & directories
    #ftp.dir()
    ftp.quit()
       