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


urlpatterns = [
    path('allocate/', game.allocate),
    path('attack/', game.attack),
]


import socket    




HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PLAYER1_PORT = 65441        # Port to listen on (non-privileged ports are > 1023)
PLAYER2_PORT = 65442        # Port to listen on (non-privileged ports are > 1023)

var connection
var address

def parse1(data):
    print(data)
    parts = data.split()
    if (parts[0] == "allocate"):
        allocate(parts[1], int(parts[2], int(parts[3])))
    elif (parts[0] == "move"):


def send_message1(message):
    with conn:
        conn.sendmsg(message)


def connect1():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PLAYER1_PORT))
        s.listen()
        connection, address = s.accept()
        while True:
            data = connection.recv(1024)
            parse1(data)

def parse2(data) {
    print(data)
    parts = data.split()
    if (parts[0] == "allocate"):
        allocate(parts[1], int(parts[2], int(parts[3])))

def send_message2(message):
    with conn:
        conn.sendmsg(message)


def connect2():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PLAYER2_PORT))
        s.listen()
        connection, address = s.accept()
        while True:
            data = connection.recv(1024)
            parse1(data)

            
            
            

__init__():
    connect1()
    connect2()

            
