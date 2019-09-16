# import socketserver


import socket
import sys, os
import re
from _thread import *
from collections import namedtuple
import threading
project_dir ='/GeoServer'

sys.path.append(project_dir)

#os.environ['DJANGO_SETTINGS_MODULE']='settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GeoServer.settings")

import django
from django.utils import timezone

django.setup()
from api.models import Geo, movement

# **,imei:359586018966098,B
startups = [("359586018966098", "**,imei:864895033178706,C,20s")]
HOST = '0.0.0.0'  # Symbolic name meaning all available interfaces
PORT = 8888  # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
Pos = namedtuple('Pos', 'imei, lat, lon, spd, bearing, acc, idx')
print('Socket created')

# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print('Socket bind complete')

# Start listening on socket
s.listen(255)
print('Socket now listening')


def log(msg):
    with open('log.txt', 'a+') as output_file:
        output_file.write('{0}\n'.format(msg))


# Function for handling connections. This will be used to create threads
def clientthread(conn):
    # Sending message to connected client
    imei=''
    # infinite loop so that function do not terminate and thread do not end.
    while True:

        # Receiving from client
        try:
            data = conn.recv(1024)
        except socket.error:
            break
        else:
            if not data:
                break
            try:
                print((data).decode())
                log((data).decode())
            except:
                print('Не удалось прочитать data')
                log('Не удалось прочитать data')
                break

            if str(data).find("##") > -1:
                print("Отправляем Load на клиент")
                #conn.send(("LOAD").encode('utf-8'))
                if (data.decode())[0:7] == "##,imei":  # FIRST CONTACT
                    imei_re = re.compile("##,imei:(\d+),A;")
                    m = imei_re.match(data.decode())
                    if m:
                        imei = m.group(1)
                        print('Imei: '+imei)
                        if (Geo.objects.filter(ID_obj=imei).exists()):
                            print('Этот ID нашелся в системе')
                            conn.send(("LOAD").encode('utf-8'))
                        else:
                            print('ID в системе не зарегистрирован!!!')
                            break


            #Собираем координаты
            elif (data.decode())[0:4] == "imei":
                spd=0
                data2 = data.decode()[:-1]  # remove ;
                parts = data2.split(',')
                if len(parts) > 11:
                    #self.last = time.time()
                    #self.counter = self.counts
                    #os.utime(self.lastfile, None)  # mark OK
                    # print parts[7],parts[8],parts[9],parts[10]
                    #
                    # parse messages "help me", "et", etc?
                    # imei:35971004071XXXX,et,1304041745,,F,164528.000,A,5150.6452,N,00551.9452,E,0.00,0;
                    # imei:35971004071XXXX,help me,1304041743,,F,164345.000,A,5150.6452,N,00551.9452,E,0.00,0;
                    # imei:35971004071XXXX,tracker,1304041747,,F,164726.000,A,5150.6452,N,00551.9452,E,0.00,0;
                    if parts[8] != "":
                        # 5620.2932 = ddmm.mmmm
                        #
                        ddmmmmmm = float(parts[7])
                        degs = int(ddmmmmmm / 100)
                        mins = ddmmmmmm - (degs * 100)
                        lat = degs + mins / 60
                        if parts[8] == "S":
                            lat = -lat
                        lat = round(lat, 5)

                        ddmmmmmm = float(parts[9])
                        degs = int(ddmmmmmm / 100)
                        mins = ddmmmmmm - (degs * 100)
                        lon = degs + mins / 60
                        # добавляем запись координат для объекта в БД
                        print(str(imei))
                        if (movement.objects.filter(ID_obj=Geo.objects.get(ID_obj=imei)).exists()):
                            print('Сохраняем координаты')
                            mov = movement.objects.get(ID_obj=Geo.objects.get(ID_obj=imei))
                            mov.Latitude = str(lat)
                            mov.Longitude = str(lon)
                            mov.save()
                        if parts[10] == "W":
                            lon = -lon
                        lon = round(lon, 5)

                        #
                        if parts[11] != "":
                            spd = float(parts[11]) * 0.44704  # mi/h,to km/h,to m/s

                        bearing = -1
                        if parts[12] != "":
                            bearing = parts[12]
                        #
                        # 'imei, lat, lon, spd, bearing, acc
                        acc=''
                        posidx=''
                        #pos = Pos(imei, lat, lon, spd, bearing, acc, posidx)
                        msg = parts[1]
                        if msg != "tracker":  # could be SOS, battery low, etc.
                            #self.on_msg(msg)
                            print('Could be SOS, battery low, etc')
                            log('Could be SOS, battery low, etc')
                        print('Получены координаты от устройства: '+imei+' '+str(lat)+' '+ str(lon)+ ' Скорость '+str(spd))
                        log('Получены координаты от устройства: '+imei+' '+str(lat)+' '+ str(lon)+ ' Скорость '+str(spd))



            if len(data) == 16:
                print("Отправляем imai на клиент")
                print('строка запроса:**,imei:'+ imei+',C,30s')
                conn.send(("**,imei:"+ imei+",C,30s").encode('utf-8'))
                # conn.send(("ON").encode('utf-8'))

    # came out of loop
    conn.close()
    print('Соединение завершено для imei: '+str(imei))


# now keep talking with the client
while 1:
    # wait to accept a connection - blocking call
    try:
        conn, addr = s.accept()
    except socket.error:  # данных нет
        break
    else:
        print('Connected with ' + addr[0] + ':' + str(addr[1]))

        # start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
        start_new_thread(clientthread, (conn,))
        # t = threading.Thread(clientthread(conn))
        # t.setDaemon(True)  # don't hang on exit
        # t.start()

s.close()