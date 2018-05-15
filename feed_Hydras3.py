# Feed_Hydras3
# il programma esegue l'alimentazione della cartella di Hydras3 con i file .mis
# scaricati direttamente dall'ftp di ARPA
#1. inizializzazione
import os
import pandas
from ftplib import FTP
import shutil
ftp_server='ftp.arpalombardia.it'
userid='portata'
pwd='' #mettere la passwd giusta
#2. inizializzazione ftp e directory di lavoro
ftp=FTP(host=ftp_server, user=userid, passwd=pwd)
ftp.cwd('/portata/Hydras3')
file_remote=ftp.nlst('.')
os.chdir('c://Users//mmussin//Downloads') # cambiare la directory in modo opportuno
#3. ciclo di
for f in file_remote:
    localfile=open(f,'wb')
    ftp.retrbinary('RETR '+f,localfile.write, 1024)
    localfile.close()
    #ftp.delete(f)
ftp.quit()
