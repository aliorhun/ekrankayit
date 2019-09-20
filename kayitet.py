import subprocess
import sys
import ftplib
import datetime
import time

ftpservername="10.154.25.159"
ftpusername="elma"
ftppassword="elma"

# cython3 --embed -o kayitet.c kayitet.py 
# gcc -v -Os -I /usr/include/python3.7m/ -L /usr/lib/x86_64-linux-gnu/  -o kayitet kayitet.c  -lpython3.7m  -lpthread -lm -lutil -ldl

def record():
	datetime_object = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H:%M:%S')
	cmd="recordmydesktop --no-sound -o "+str(datetime_object)+".ogv > /dev/null 2>&1 &"
	subprocess.check_output(cmd, shell=True)
	return("Kayıt Başladı")

def searchProgram():
	cmd="ps aux | grep recordmydesktop | awk {'print $2'} | head -1"
	lines=subprocess.check_output(cmd, shell=True)
	return(lines)

def searchFileName():
	cmd="ps aux | grep recordmydesktop | awk '{split($0, a, \"-o\"); print a[2]}' | head -1"
	filename1=subprocess.check_output(cmd, shell=True)
	filename1=filename1.decode("utf-8").strip()
	return(filename1)

def sendFTP(filenamevideo):
	session = ftplib.FTP(ftpservername,ftpusername,ftppassword)
	file = open(filenamevideo,'rb') 
	session.storbinary('STOR '+filenamevideo, file) 
	file.close()
	session.quit()

def stop():
	#programpids=searchPrograms()
	#for i in range(0,len(programpids)):
	filename=searchFileName()
	pid=searchProgram()
	cmd="killall -s SIGINT recordmydesktop"
	cmd2="tail --pid="+str(pid.decode("utf-8").strip())+" -f /dev/null"
	cmd=subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
	cmd.communicate()
	
	cmd2=subprocess.Popen(cmd2, stdout=subprocess.PIPE, shell=True)
	cmd2.communicate()
	sendFTP(filename)
	print("durduruldu")
	return(True)

if __name__ == "__main__":
	if (sys.argv[1]=="record"):
		print(record())
	elif(sys.argv[1]=="stop"):
		stop()
