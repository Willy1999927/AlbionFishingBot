# AlbionFishingBot
2020.Nov.11, Chih-Chiang Huang

Please star this project if you like it (ﾉ>ω<)ﾉ

This is a fully automatic bot that fishes in Albion Online. The functions include cast rod, catch fish, and temporary stop when some other players nearby. Please do not run multiple clients with this bot, the environment in this game will be ruined :(

The method of detecting fish catches is by sound, pyaudio lib. Please adjust the code yourself to fit your audio instrument, volume, and OS. Probably you need to edit the name of the speaker (Stereo or something probably) and the threshold to make this bot work.

If you do not have an ANN model with you, please run the main script without enabled ANN in the branch. It will collect the data when fishing. You can further use these data to train your own model. The ANN involvement would improve the overall performance by filtering out the footsteps from other players and the noise made by the monsters. You can also find my own NN_model from the release. However, the model is fit to my own PC and may not be suitable for you.

Tested on Windows 10. system volume: 30. Game setting: overall volume: 10. sound effect 75. 1920 * 1080, HUD 100% scale.  
Tested on Windows 7.  same configuration.

I can not deal with the speaker instrument problem for you.

# User Guide
F9 for automatically adjust the volume factor. This function is used to balance the volume differences among different computers. The function is still under developed and tested.

F10 for starting the bot. Please stay your mouse at the fishing point before pressing F10.

F11 for adding a fishing point. Please stay your mouse at the fishing point before pressing F11. You can set multiple fishing points to cast rod to multiple directions.

F12 for stoping the bot. Or you can just use Ctrl+C to stop the running process at the command line.

# Hint for packages installation
Python 3.8.6 64 bits version is suggested for future support  
python -m pip install --upgrade pip  
pip install psutil  
pip install numpy  
pip install pywin32  
pip install keyboard  
pip install pyautogui  
pip install pipwin  
pipwin install pyaudio  
pip install pillow  
pip install opencv-python  
pip install keras  
pip install tensorflow  
(pip install pyinstaller) -> This is for making the executable file  
  
You may need to install Microsoft Visual C++ 2015-2019 Redistributable (x64) to use tensorflow  
keras only works for x64 version Python  
tensorflow only works for Python 3.5-3.8 @ 11 NOV 2020
