from vidstream  import StreamingServer
import threading 

receiver = StreamingServer(host='10.146.0.143' , port=9500)

t=threading.Thread(target=receiver.start_server)
t.start()

while input("") != 'q':
    continue

receiver.stop_server()