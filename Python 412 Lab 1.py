print('How many total requests were made in the time period represented by the log?')

logfile="http_access_log.txt"
linescount=0
with open (logfile,'r') as files:
    for i in files:
        linescount=linescount+1
print(linescount)

