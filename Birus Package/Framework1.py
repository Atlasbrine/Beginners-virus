import os , shutil
i = int (0)
t = int (1)
while i == 0:
	path = os.path.join(r'C:\Users',os.getlogin(),'Desktop', f'{t}.gif')
	path2 = os.path.join(r'C:\Users',os.getlogin(),'Desktop', f'{t}.mp4')	
	t+=1
	shutil.copy ('henrystickmin.gif',path)
	shutil.copy ('chungus.mp4',path2)