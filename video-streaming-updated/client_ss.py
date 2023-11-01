from vidstream import ScreenShareClient
import threading

sender = ScreenShareClient(host='10.146.0.143' , port=9500)
t=threading.Thread(target=sender.start_stream)
t.start()

while input("") != 'q':
    continue

sender.stop_stream()

