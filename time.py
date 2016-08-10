#!/usr/bin/python
import time
import datetime

#07/04/2016 08:50:10 (1460037010)
s = "12/04/2016 12:50:14"
print time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y %H:%M:%S").timetuple())

etmig=1
etmigdate=1
elapsedformated=1
elapsed=1
mignumber=1
gpfsData="aqui"
print 'echo \"End date   = '+str(etmigdate)+' secs('+str(etmig)+'\)\nElapsed time = '+str(elapsedformated)+'secs ('+str(elapsed)+')\n----- Mig #'+str(mignumber)+'\-----\n\">>'+gpfsData+'migrations.log'
s.sendline('echo \"End date   = '+str(etmigdate)+' secs('+str(etmig)+')\nElapsed time = '+elapsedformated+' secs ('+str(elapsed)+')\n----- Mig #'+str(mignumber)+'-----\n\">>'+Config.gpfsData+'migrations.log')
