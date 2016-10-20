import appuifw

import e32

colors = [u"red", u"green", u"blue", u"brown"]  
  
index = appuifw.selection_list(colors)  
if index == 2:  
    print "blue is correct!"  
else:  
    print "Bzz! " + colors[index] + " is not correct"  

  
#def quit():  
#    print "Exit key pressed!"  
#    app_lock.signal()  
  
#appuifw.app.exit_key_handler = quit  
#appuifw.app.title = u"First App!"  
  
#appuifw.note(u"Application is now running","")  
  
#app_lock = e32.Ao_lock()  
#app_lock.wait()  
#print "Application exits"  

