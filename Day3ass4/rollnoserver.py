'''@author Madhuri'''

import socket 
import os

print('\n-------MSIT Attendance marking - 2019-------\n')
roll_list = [2019501105, 2019501026, 2019501118, 2019501088, 2019501100]
string  = str(roll_list[0])
print('Students in the class: \n')
print(roll_list)
print("\n")

soc = socket.socket()
soc.bind(('127.0.0.1', 8188))
soc.listen(10)
while True:
	conn, addr = soc.accept()
	rollnum = conn.recv(1024).decode()
	checkroll = int(rollnum)
	if checkroll in roll_list:
		roll_list.remove(checkroll)
		print("Attendance Marked for " + rollnum+"\n")
		print("Absentees are "+ str(roll_list)+"\n")
	else:
		print("Roll Number is not found\n")
soc.close()
