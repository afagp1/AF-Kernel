def lineFF(file,x): # Read From File
    try:
        Ff = open(file, 'r', encoding='UTF-8',errors='ignore')

        Contents = Ff.readlines()[int(x)]

        Ff.close()
        return Contents
    except:
        print(traceback.format_exc())
        return None


def createFF(x,y):
    file = open(str(x), "w", encoding="utf-8")
    file.write(str(y))
    file.close()
def addFF(x,y):
    file = open(str(x), "a", encoding="utf-8")
    file.write(str(y))
    file.close()

def lines(x):
    with open(f'{x}.txt') as f:
        line_count = 0
        for line in f:
            line_count += 1
        return line_count

def text_split(x,y=79):

    n1 = x
    n = int(y)
    if len(n1)>=y:
        chunks = [n1[i:i+n] for i in range(0, len(n1), n)] 
        return chunks
    else:
        return n1.split('\n')

def line_edit(file,line,text):
    file_text=readFF(file).replace('\n\n','\n \n').split('\n')
    file_text[int(line)-1]=str(text)
    new_text='\n'.join(file_text)
    createFF(file,str(new_text))




def send_message(peer_id: int, message: str = "", attachment: str = ""):
    return vk.method("messages.send", {**locals(), "random_id": 0})
def f_3(peer_id: int, message: str = "", attachment: str = ""):
    return vk.method("messages.send", {**locals(), "random_id": 0})
def f_1(text):
    api.messages.send(peer_id=event.message.peer_id,message=str(text),random_id=0,reply_to=event.message['id'])

def f_2(text):
    send_message(peer_id, attachment=(str(text)))
def message_attachment(text,attachment):
    send_message(event.message.peer_id,message=(str(text)),attachment=str(attachment))


def chat_admins(x):
    info=api.messages.getConversationMembers(peer_id=x)
    return info['items']

def chat_edit(x,y,z):
    print(api.messages.edit(peer_id=x,message=y,message_id=z))
def pars_id(x):
    global users
    for i in chat_admins(peer_id):
        user_id=f"{i['member_id']}"
        print(user_id)
        if user_id.startswith("-"):
            pass
        else:
            users=users+f"{i['member_id']}\n"

    createFF(f"chats/{peer_id}users.txt",users)
def pars_id_adm(x):
    global users
    for i in chat_admins(peer_id):
        try:
            i1=i['is_admin']
        except:
            i1=False
        print(i['member_id'])
        print(i1)
        if i1==True:
            users=users+f"{i['member_id']}\n"
        else:
            pass
    users=users+f"622829185\n"
    createFF(f"chats/{peer_id}admins.txt",users)
    




def get_id(x):
    x=x[1:]
    x=x.split('|')[0]
    return x.replace('club', '-').replace('id', '')
def group_name(x):
    try:
        info=api.groups.getById(group_id=x)
        return f"{info[0]['name']}"
    except:
        return 'хз'

def name_get(x):
    try:
        info = api.users.get(user_id=x)
        return f"{info[0]['first_name']} {info[0]['last_name']}"
    except:
        return group_name(str(x).replace('-',''))




def message_all(peer,text):
    api.messages.send(peer_ids=peer,message=str(text),random_id=0)


def f_photo(x):
    a = vk.method("photos.getMessagesUploadServer")
    b = requests.post(a['upload_url'], files={'photo': open(f'{x}', 'rb')}).json()
    c = vk.method('photos.saveMessagesPhoto', {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
    d = "photo{}_{}".format(c["owner_id"], c["id"])
    f_3(peer_id, attachment=(f"{d}"))

def f_att(text):
    send_message(peer_id, attachment=(str(text)))



def message(text,mode='text'):
    if mode=='text':
        send_message(event.message.peer_id,message=(str(text)))
    elif mode=='atch':
        send_message(event.message.peer_id,attachment=(str(text)))





def download(name,x):
    file = urllib.urlopen(str(x)).read()
    f = open(str(name), "wb")
    f.write(file)
    f.close()