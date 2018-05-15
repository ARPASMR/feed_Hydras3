# Feed_Hydras3
Programma di alimentazione di Hydras3

# Scopo
Lo script in Python 3 esegue la copia dall ftp di arpalombardia nella cartella
di lavoro di Hydras3 dei file con estensione .mis come trasmessi direttamente
dalle stazioni Corrtek

# Funzionamento
Lo script viene lanciato dal PC Hydras3 (ARPA-024042) previa modifica di:
1. directory di atterraggio dei file_remote
2. inserimento della password FTP per l'accesso
Lo script può essere inserito in un ciclo tipo crontab
