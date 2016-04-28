for /f "delims=" %%i in (samples-malware-sha256.txt) do (C:\Python27\python vbquery.py  %%i  && timeout 12)
for /f "delims=" %%i in (samples-normal-sha256.txt)  do (C:\Python27\python vbquery.py  %%i  && timeout 12)
pause