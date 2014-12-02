from datetime import date
import datetime

today = datetime.date.today()
someday = datetime.date(2000, 1, 1)
diff = today - someday
DayCount = diff.days +1
DAYS = bin(DayCount)
DC= DAYS[-13:]
print DayCount
print DC
DCLen = len(DC)



MFGID = '000101'
#DATECODE = '01234567890123'
DATECODE = '00000000000001'
FID = '111'
SN = '000000001'

print DATECODE[-(DCLen):]
DATECODE = DATECODE.replace(DATECODE[-(DCLen):],DC)

print DATECODE

a = MFGID + DATECODE + FID + SN

num = 0
for i in range(32):
    num = num+int(a[i])*(2**(31-i))
print num
print hex(num)
VayaSN = hex(num)
VayaSN = VayaSN.upper()
VayaSN = VayaSN[2:10]
print "Generate UID of Today : ",VayaSN
