# AlbionFishingBot
2020.Nov.11, Chih-Chiang Huang

Please star this project if you like it (ﾉ>ω<)ﾉ

This is a fully automatic bot that fishes in Albion Online. The functions include cast rod, catch fish, and temperary stop when some other players nearby. Please do not run multiple clients with this bot, the environment in this game will be ruined :(

The method of detecting fish catches is by sound, pyaudio lib. Please adjust the code yourself to fit your audio instrument, volume, and OS. Probably you need to edit the name of the speaker (Stereo or something probably) and the threshold to make this bot work.

Tested on Windows 10. system volume: 30. Game setting: overall volume: 10. sound effect 75. 1920 * 1080, HUD 100% scale.  
Tested on Windows 7.  same configuration.

I can not deal with the speaker instrument problem for you.


# Hint for packages installation
Python 3.8.6 64 bits version is suggested for future support  
python -m pip install --upgrade pip  
pip install psutil  
pip install numpy  
pip install pywin32  
pip install keyboard  
pip install pipwin  
pipwin install pyaudio  
pip install pillow  
pip install opencv-python  
pip install keras         -> This only works for x64 version Python  
pip install tensorflow    -> This only works for Python 3.5-3.8 @ 11 NOV 2020  
(pip install pyinstaller) -> This is for making the execuable file
