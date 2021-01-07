"""hexipro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from players.views import allocate




import socket    




HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PLAYER1_PORT = 65441        # Port to listen on (non-privileged ports are > 1023)
PLAYER2_PORT = 65442        # Port to listen on (non-privileged ports are > 1023)

class Server:
    connection1 = 0
    connection2 = 0

    def parse1(data):
        parts = data.split()
        if (parts[0] == "allocate"):
            messages = allocate(parts[1], int(parts[2]), int(parts[3]))
            for message in messages:
                send_message(message)
        elif (parts[0] == "move"):
            messages = move(parts[1], int(parts[2]), int(parts[3]), int(parts[4]), int(parts[5]))
            for message in messages:
                send_message(message)
            


    def send_message(message):
        with connection1:
            connection1.sendmsg(message)
        with connection2:
            connection2.sendmsg(message)


    def connect1(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PLAYER1_PORT))
            s.listen()
            self.connection1, address = s.accept()
            while True:
                data = self.connection1.recv(1024)
                self.parse1(data)

    def parse2(data):
        parts = data.split()
        if (parts[0] == "allocate"):
            messages = allocate(parts[1], int(parts[2]), int(parts[3]))
            for message in messages:
                send_message(message)
        elif (parts[0] == "move"):
            messages = move(parts[1], int(parts[2]), int(parts[3]), int(parts[4]), int(parts[5]))
            for message in messages:
                send_message(message)


    def connect2(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PLAYER2_PORT))
            s.listen()
            self.connection2, address = s.accept()
            while True:
                data = self.connection2.recv(1024)
                self.parse2(data)

                
            
            

server = Server()
server.connect1()
server.connect2()
            
