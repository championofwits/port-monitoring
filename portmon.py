import socket


host = ''    #which host to accept '' => all host    
wport = 2222 #port on which service is shifted
whost = '172.20.25.69'   #IP of your PC
port = 80   #port on which we want to monitor activity

def connection1(host,port):          #port recieving socket              this program <----------> client             
    t1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    t1.bind((host,port))
    t1.listen(100)
    conn,addr = t1.accept()
    return conn,addr

def connection2(whost,wport):       #socket to talk to original service      service(apache ,mongoDB,SSH,firefox ...) <------->this program
    t2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    t2.connect((whost,wport))
    return t2
while True :
    conn,addr = connection1(host,port)   #setup with client
    with conn: 
        t2 =  connection2(whost,wport)  #setup with service
        with t2:
            while True :
                data = conn.recv(8290304)    
                print(data)
                if not data:
                    print('delayy1')
                    break
                print("browser")
                t2.sendall(data)
                returnn = t2.recv(8290304)
                if not returnn:
                    print('delayy2')
                    break
                print("server")
                conn.sendall(returnn)

            
'''
what client believes    service(port 80) <----------> client

what is done       service(port 2222)  <----------> this program(port 80) <---------> client

Tested with XAMPP and browser:
set apache service port to 2222
run your site on xampp
go to your browser :
enter local host and run you will see browser request and server response
to bypass this if you go to localhost:2222 you will directly access page without monitoring but by default browsers send request to port 80

'''


