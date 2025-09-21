# Word For Word Lyrics Match Tool
This tool is designed to help you with the matching of word for word lyrics.

For example, if you have a song with the lyrics but no timestamp, 
you can use this tool to match the lyrics word with the song on your own.

---
## How to use
1. Download the tool from the releases page or Build it yourself(See the build instructions below)
2. Open the tool(you can either open it with `python3 main.py` or use the executable file(.exe))
3. Click on the `Open A LRC File` button or use Ctrl+O to open a LRC file OR you can type the lyrics in the text box then click on `Use the Lyrics upon`
4. Check whether the lyrics on the text box are displayed correctly or not. If not, you may need to save and encode the LRC file with UTF-8 on your own editor.
5. Then click `Next Step`. This will lead you to the setting page. Here you should choose the song file(`mp3` `flac` `wav`). Also, you can check other setting.
6. If everything is fine, click `Next Step`, this will lead you to the matching page.
7. On the match page, click the `Start Player` button to play the song.
8. During the song playing, you should click the `Next Char` button(or press `N` key) to log the current timestamp when you hear the current character in the song.
9. After you finish the matching, you will be leaded to the result page. You can save the result to a file.

---
## Build instructions(For WINDOWS)
1. Install Python3
2. ( Optional) Create a virtual environment
3. Install the dependencies with `pip install -r requirements.txt`
4. Install PyInstaller with `pip install pyinstaller`
5. Start building with `pyinstaller main.py`
6. After building, you will find the executable file in the `dist` folder.

---

## Setting
`Audio File`: 

Choose the audio file, which will be played for match.


`Speed`: 

Select the audio playback speed. Set it lower will make the match work easier, 
but It could change the pitch of the song during the playback.

Recommended value: `1` or `0.8` or `0.5`


`Using three decimal places`:

The normal timestamp is like this: `[00:00.00]`

When this function was turned on: `[00:00.000]`

This can slightly improve the accuracy of the match. 
However not every music player application support this feature.
Thus,it is recommended to keep it off.

Recommended value: `False`


`No animation`:

Enable this feature will stop the update function of LCDNumber and ProgressBar in the edit page.
This will optimize the experience on machines with poor performance.

Recommended value: `False`

`Font`:

Some songs might be written in foreign languages.
Thus, sometime the default font of your machine may not be able to display it correctly.
For this situation, you can choose an installed font on your machine.


`Delay`:

Due to the additional time occupied by human reactions and machine calculations,
you may need to adjust the delay time to make the match work better.

Recommended value: >= `-300`