import socket
from threading import Thread
from tkinter import *
top = Tk()

def accept_incoming_connections():
    while True:
        client, client_address = SERVER.accept()
        clients[client] = client_address
        Thread(target=handle_client, args=(client,)).start()

def handle_client(client):  
    while True:
        try:
            msg = client.recv(BUFSIZ).decode("utf8")
            if msg == "{quit}":
                client.close()
                del clients[client]
                break
            else:
                broadcast(msg)
                msg_list.insert(END, msg)
        except OSError:  
            break

def send(event=None):  
    msg = my_msg.get()
    my_msg.set("")  
    broadcast(msg)
    msg_list.insert(END, "Server: " + msg)

def broadcast(msg, prefix=""):  
    for sock in clients:
        sock.send(bytes(prefix+msg, "utf8"))

def on_closing():
    top.destroy()

top.title("Chat Server")

messages_frame = Frame(top)
my_msg = StringVar()  
my_msg.set("")
scrollbar = Scrollbar(messages_frame)  

msg_list = Listbox(messages_frame, height=25, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)
msg_list.pack(side=LEFT, fill=BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = Button(top, text="Send", command=send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)

clients = {}
addresses = {}

HOST = '10.146.0.143'
PORT = 9242
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    mainloop()  
    ACCEPT_THREAD.join()
    SERVER.close()
