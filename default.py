
# -*- coding: utf-8 -*-
import appuifw, key_codes
import e32
import simplejson as json
import urllib
from graphics import *
import time

#print time.strftime("%d %m %H:%M:%S ", time.localtime(1471039700))
#appuifw.app.title = u"vk"  #title name

count_friends = 20
count_history = 20
access_token = "079b3832d92ce4569bd96081c03ea9747bc52f18726cfbc7861d55da8c329c0dd260a1efd477aa24af624"
load_on_of = 0 #1 it get online friends #0 it ger offline frinds
app1=None#win one (friends)
frends_list = []#friends save in it list   
id_list = []#friends id save in it list
id_list1 = []
current_id = ""#it set id's in win one send to history_get
freirnds_l = []
history = []

global old_body
global old_title 
global old_menu 

def get_history(index):#------------------------------------------------------------------------------------------------------------------------------------------------------------
    hustory_list = []
    history = json.loads(urllib.urlopen("https://api.vk.com/method/messages.getHistory?count=%s&user_id=%s&access_token=%s&v=5.33" % (count_history,id_list[index],access_token))
                         .read().decode("utf-8"))
    for item_mes in reversed( history["response"]["items"]):
        layer = ""
        if item_mes["from_id"] == id_list[index]:
            item_mes["from_id"] = freirnds_l[index]
        else:
            item_mes["from_id"] = "Me"
        layer+= "%s : %s \n" % (item_mes["from_id"], item_mes["body"])#save in layer name and online status one's friends
        hustory_list.append(layer)#add in list friend layer
    return hustory_list#--------------------------------------------------------------------------------------------------------------------------------------------------------------



get_chat= []
chats_list=[]
chat_id = []



def get_chat_h(index,chat_list):#--------------------------------------------------------------------------------------------------------------------------------------------------------------
    hustory_chat_list=[]
    ids=chat_id[index]+2000000000
    history_c = json.loads(urllib.urlopen("https://api.vk.com/method/messages.getHistory?count=%s&user_id=%s&access_token=%s&v=5.33" % (count_history,ids,access_token))
                         .read().decode("utf-8"))
   #print history_c
    for item_mes in reversed( history_c["response"]["items"]):
        layer = ""
        if item_mes["from_id"] == 119482119:
            item_mes["from_id"] = "Me"
        else:
            item_mes["from_id"] = "chat"
        layer+= "%s : %s \n" % (item_mes["from_id"], item_mes["body"])#save in layer name and online status one's friends
        hustory_chat_list.append(layer)#add in list friend layer
    return hustory_chat_list#--------------------------------------------------------------------------------------------------------------------------------------------------------------



def get_friends(id_list):#load list friends#--------------------------------------------------------------------------------------------------------------------------------------------------------------
    frends_list = []         
    friends = json.loads(urllib.urlopen("https://api.vk.com/method/friends.get?count=%s&fields=first_name,online&order=hints&access_token=%s&v=5.33" % (count_friends,access_token))
                         .read().decode("utf-8"))#read from vk friends
    
    for item in friends["response"]["items"]:
        layer = ""
        layer+= "%s %s " % (item["first_name"], item["last_name"])#save in layer name and online status one's friends
        frends_list.append(layer)#add in list friend layer
        id_list.append(item["id"])#add in id_list id one's friends   
    return frends_list#--------------------------------------------------------------------------------------------------------------------------------------------------------------

freirnds_l=get_friends(id_list)

def get_chats():#--------------------------------------------------------------------------------------------------------------------------------------------------------------
    chats = json.loads(urllib.urlopen("https://api.vk.com/method/messages.getChat?chat_ids=20,40,41,42,43&fields=first_name,online&order=hints&access_token=%s&v=5.33" % (access_token))
                         .read().decode("utf-8"))
    global chat_id
    for item in chats["response"]:
        layer = ""
        layer+= "%s  " % (item["title"])#save in layer name and online status one's friends
        chat_id.append(item["id"])
        chats_list.append(layer)#add in list friend layer
    #print chats_list
    return chats_list#--------------------------------------------------------------------------------------------------------------------------------------------------------------

get_chat = get_chats()
#print chat_id
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def quit():  
    #print "WANNABE PHOTOEDITOR EXITS"  
    app_lock.signal()
    
    
def handler_L2():
    #print(app2.current())#current index app2
    print "ola"

def back():
    apuifw.app.body = old_body
    appuifw.app.title = old_title
    appuifw.app.menu = old_menu
    appuifw.app.exit_key_handler = quit

def back_chats():
    handle_tab(2)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------    
def settings():
    pass#print ""
    

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def ok():
    appuifw.note(u'Hello World') 
#--------------------------------------------------------------------------------------------------------------------------------------------------------------    
#appuifw.app.body.bind(key_codes.EKeySelect, ok)

    
def exit():#--------------------------------------------------------------------------------------------------------------------------------------------------------------
    #handle_tab(0)
    appuifw.app.body = old_body
    appuifw.app.title = old_title
    appuifw.app.menu = old_menu
    appuifw.app.exit_key_handler = quit
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
index=0

    

def write():#---------------------------------------------------------------------------write to user-----------------------------------------------------------------------------------
    my_message = appuifw.query(u"type a message:", "text")
    #print my_message
    #global my_message
    if( my_message != None):
   
        user_id = id_list[index]
        my_message.encode("utf-8")
        text=json.loads(urllib.urlopen("https://api.vk.com/method/messages.send?user_id=%s&message=%s&access_token=%s&v=5.33" % (user_id,my_message,access_token))
                        .read().decode("utf-8"))#read from vk friends
        text = u"Me : "+ my_message.decode("utf-8")
        
        history.append(text)
        ind = appuifw.Listbox(history, handler_his)
        appuifw.app.body = ind
        appuifw.app.menu = [ (u"back",back),(u"settings",settings),(u"exit",quit)]#left soft
    else:
        pass
#--------------------------------------------------------------------------------------------------------------------------------------------------------------

        

    
def wtite_chats():#--------------------------------------------------------------------write to chat------------------------------------------------------------------------------------------
    #print index
    my_message = appuifw.query(u"type a message:", "text").encode("utf-8")
    2000000000
    user_id =chat_id[index]
    user_id += 2000000000
    text=json.loads(urllib.urlopen("https://api.vk.com/method/messages.send?peer_id=%s&message=%s&access_token=%s&v=5.53" % (user_id,my_message,access_token))
                         .read().decode("utf-8"))#read from vk friends
    print text
    text = u"Me : "+ my_message.decode("utf-8")
    
    history_chat.append(text)
    ind = appuifw.Listbox(history_chat, handler_his)
    appuifw.app.body = ind
    appuifw.app.body.RefreshItem
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------
    

def messsage_win(index):#---------------------------------------------------------------history with user-----------------------------------------------------------------------------------------------
    appuifw.app.exit_key_handler = exit
    appuifw.app.title = u"message"
    global history
    history = get_history(index)

    def handler_his():
        global index_history_message
        index_history_message = ind.current()
        appuifw.note(history[index_history_message])

    
    ind = appuifw.Listbox(history, handler_his)
   
    appuifw.app.body =ind 
    appuifw.app.menu = [ (u"write",write),(u"back",back),(u"settings",settings),(u"exit",quit)]#left soft
  #--------------------------------------------------------------------------------------------------------------------------------------------------------------

    
def get_chat_history(index):#-----------------------------------------------------------history with chat---------------------------------------------------------------------------------------------------
    
    appuifw.app.exit_key_handler = exit
    appuifw.app.title = u"message chat"
    def handler_his():
        global index_history_message_chat
        index_history_message_chat = ind.current()
        appuifw.note(history_chat[index_history_message_chat])
    
    history_chat = get_chat_h(index,chats_list)
    ind = appuifw.Listbox(history_chat, handler_his)
    appuifw.app.body = ind
    appuifw.app.menu = [ (u"write",wtite_chats),(u"back",back),(u"settings",settings),(u"exit",quit)]#left soft
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------


    #--------------------------------------------------------------------------------------------------------------------------------------------------------------
def ref_app1():#refreshing friends win
    
    def handler():#
       # print id_list\
        global index
        index = app1.current()#--
        current_id = id_list[index]#-getting current id select from friends win and send history_get
        messsage_win(index)
        #print current_id
        #print index
        
    app1 = appuifw.Listbox(freirnds_l,handler)   
    
    return  app1
#--------------------------------------------------------------------------------------------------------------------------------------------------------------

L2 = [u"Stefan", u"Holger", u"Emil", u"Ludger"]
app2 = appuifw.Listbox(L2, handler_L2)#add win2
app3 = appuifw.Listbox(L2, handler_L2)




def handler_L3():#--------------------------------------------------------------------------------------------------------------------------------------------------------------
     
     def handler3():#
       # print id_list\
        global index
        index = app3.current()#--
        #current_id = id_list[index]#-getting current id select from friends win and send history_get
        get_chat_history(index)
        #print current_id
        #print index
        
     app3 = appuifw.Listbox(get_chat,handler3) 
    
     return  app3#--------------------------------------------------------------------------------------------------------------------------------------------------------------



    

#appuifw.app.body = ind
def handle_tab(tab_index):#switch beetwin windows#--------------------------------------------------------------------------------------------------------------------------------------------------------------
    global lb
    global old_body
    global old_title 
    global old_menu 
        
    if tab_index == 0:#win1
        appuifw.app.title = u"friends" 
        appuifw.app.menu = [(u"settings",settings),(u"exit",quit)]
        appuifw.app.set_tabs([u"Friends", u"online", u"chats"],handle_tab)#select win
        appuifw.app.exit_key_handler = quit
        app_l = ref_app1()#refresh friends list
        appuifw.app.body = app_l # write in frinds(win1) friends list

        
        old_body = appuifw.app.body
        old_title = appuifw.app.title
        old_menu = appuifw.app.menu
    if tab_index == 1:
        appuifw.app.title = u"online" 
        appuifw.app.body = app2 # switch to application 2
        
    if tab_index == 2:
        appuifw.app.menu = [(u"settings",settings),(u"exit",quit)]
        app3 =  handler_L3()
        appuifw.app.body = app3
        appuifw.app.title = u"chats"
        old_body = appuifw.app.body
        old_title = appuifw.app.title
        old_menu = appuifw.app.menu
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#appuifw.EKeyRightArrow = handle_tab(0)



handle_tab(0)#win1 defind
app_lock = e32.Ao_lock()

# create the tabs with its names in unicode as a list, include the tab handler
appuifw.app.screen = "normal"

app_lock.wait()

  
