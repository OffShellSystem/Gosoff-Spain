#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import tkinter as tk
import webbrowser
from subprocess import call
import subprocess
import os
import subprocess as sub


# Instalación Python3 y Tkinter.

call('sudo apt-get install python3', shell=True)
call('sudo apt-get install python3-tk', shell=True)


def españa():

	botonBienvenido=Frame(root, width=1024, height=1024)
	botonBienvenido.pack(fill=BOTH, expand=YES)
	botonBienvenido.place(x=0, y=0)
	Button(botonBienvenido, image=españa_logo, cursor="spider", justify="center", bd=0, relief="raised", background="black", activebackground='black', font=("URW Chancery L", 15)).pack()

	boton_coruna=Frame(root)
	boton_coruna.pack(fill=BOTH, expand=YES)
	boton_coruna.place(x=150, y=185)
	Button(boton_coruna, image=dedo_logo, command=lambda:[coruna(), botonBienvenido.destroy()], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="orange", activebackground='green').pack()

	boton_lugo=Frame(root)
	boton_lugo.pack(fill=BOTH, expand=YES)
	boton_lugo.place(x=225, y=200)
	Button(boton_lugo, image=dedo_logo, command=lambda:[lugo(), botonBienvenido.destroy()], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="orange", activebackground='green').pack()

	boton_ourense=Frame(root)
	boton_ourense.pack(fill=BOTH, expand=YES)
	boton_ourense.place(x=230, y=235)
	Button(boton_ourense, image=dedo_logo, command=lambda:[ourense(), botonBienvenido.destroy()], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="orange", activebackground='green').pack()

	boton_pontevedra=Frame(root)
	boton_pontevedra.pack(fill=BOTH, expand=YES)
	boton_pontevedra.place(x=180, y=235)
	Button(boton_pontevedra, image=dedo_logo, command=lambda:[pontevedra(), botonBienvenido.destroy()], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="orange", activebackground='green').pack()

	boton_tarragona=Frame(root)
	boton_tarragona.pack(fill=BOTH, expand=YES)
	boton_tarragona.place(x=900, y=300)
	Button(boton_tarragona, image=dedo_logo, command=lambda:[tarragona()], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="orange", activebackground='green').pack()

	boton_madrid=Frame(root)
	boton_madrid.pack(fill=BOTH, expand=YES)
	boton_madrid.place(x=610, y=260)
	Button(boton_madrid, image=dedo_logo, command=lambda:[madrid()], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="orange", activebackground='green').pack()

	boton_andalucia=Frame(root)
	boton_andalucia.pack(fill=BOTH, expand=YES)
	boton_andalucia.place(x=870, y=420)
	Button(boton_andalucia, image=dedo_logo, command=lambda:[andalucia()], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="orange", activebackground='green').pack()

	boton_barcelona=Frame(root)
	boton_barcelona.pack(fill=BOTH, expand=YES)
	boton_barcelona.place(x=829, y=220)
	Button(boton_barcelona, image=dedo_logo, command=lambda:[barcelona()], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="orange", activebackground='green').pack()

	boton_asturias=Frame(root)
	boton_asturias.pack(fill=BOTH, expand=YES)
	boton_asturias.place(x=340, y=180)
	Button(boton_asturias, image=dedo_logo, command=lambda:[asturias()], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="orange", activebackground='green').pack()

	boton_zaragoza=Frame(root)
	boton_zaragoza.pack(fill=BOTH, expand=YES)
	boton_zaragoza.place(x=700, y=220)
	Button(boton_zaragoza, image=dedo_logo, command=lambda:[zaragoza()], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="orange", activebackground='green').pack()


	pass


def coruna():

	botonBienvenido=Frame(root, width=1024, height=1024)
	botonBienvenido.pack(fill=BOTH, expand=YES)
	botonBienvenido.place(x=0, y=0)
	Button(botonBienvenido, image=coruna_ciudad, cursor="spider", justify="center", bd=0, relief="raised", background="Black", activebackground='black', font=("URW Chancery L", 15)).pack()

	boton_camara1=Frame(root)
	boton_camara1.pack(fill=BOTH, expand=YES)
	boton_camara1.place(x=540, y=240)
	Button(boton_camara1, image=camara_logo, command=lambda:[webbrowser.open_new("http://www.crtvg.es/crtvg/camaras-web/a-coruna-fixa")], cursor="target", justify="center", bd=0, relief="raised", overrelief="flat", background="black", activebackground='black').pack()

	boton_camara2=Frame(root)
	boton_camara2.pack(fill=BOTH, expand=YES)
	boton_camara2.place(x=525, y=480)
	Button(boton_camara2, image=camara_logo, command=lambda:[webbrowser.open_new("http://www.crtvg.es/crtvg/camaras-web/praza-do-obradoiro")], cursor="target", justify="center", bd=0, relief="raised", overrelief="flat", background="black", activebackground='black').pack()

	boton_camara3=Frame(root)
	boton_camara3.pack(fill=BOTH, expand=YES)
	boton_camara3.place(x=520, y=520)
	Button(boton_camara3, image=camara_logo, command=lambda:[webbrowser.open_new("http://www.crtvg.es/crtvg/camaras-web/praza-das-praterias")], cursor="target", justify="center", bd=0, relief="raised", overrelief="flat", background="black", activebackground='black').pack()

	boton_camara4=Frame(root)
	boton_camara4.pack(fill=BOTH, expand=YES)
	boton_camara4.place(x=810, y=110)
	Button(boton_camara4, image=camara_logo, command=lambda:[webbrowser.open_new_tab("http://www.crtvg.es/crtvg/camaras-web/ortigueira")], cursor="target", justify="center", bd=0, relief="raised", overrelief="flat", background="black", activebackground='black').pack()

	boton_camara5=Frame(root)
	boton_camara5.pack(fill=BOTH, expand=YES)
	boton_camara5.place(x=470, y=460)
	Button(boton_camara5, image=camara_logo, command=lambda:[webbrowser.open_new_tab("http://www.crtvg.es/crtvg/camaras-web/monte-pedroso")], cursor="target", justify="center", bd=0, relief="raised", overrelief="flat", background="black", activebackground='black').pack()

	boton_camara6=Frame(root)
	boton_camara6.pack(fill=BOTH, expand=YES)
	boton_camara6.place(x=625, y=180)
	Button(boton_camara6, image=camara_logo, command=lambda:[webbrowser.open_new_tab("http://www.crtvg.es/crtvg/camaras-web/ferrol")], cursor="target", justify="center", bd=0, relief="raised", overrelief="flat", background="black", activebackground='black').pack()

	boton_camara7=Frame(root)
	boton_camara7.pack(fill=BOTH, expand=YES)
	boton_camara7.place(x=160, y=455)
	Button(boton_camara7, image=camara_logo, command=lambda:[webbrowser.open_new_tab("http://www.crtvg.es/crtvg/camaras-web/cabo-fisterra")], cursor="target", justify="center", bd=0, relief="raised", overrelief="flat", background="black", activebackground='black').pack()



	pass

def lugo():

	botonBienvenido=Frame(root, width=1024, height=1024)
	botonBienvenido.pack(fill=BOTH, expand=YES)
	botonBienvenido.place(x=0, y=0)
	Button(botonBienvenido, image=mapa_lugo, cursor="spider", justify="center", bd=0, relief="raised", background="Black", activebackground='black', font=("URW Chancery L", 15)).pack()

	boton_camara1=Frame(root)
	boton_camara1.pack(fill=BOTH, expand=YES)
	boton_camara1.place(x=405, y=350)
	Button(boton_camara1, image=camara_logo, command=lambda:[webbrowser.open_new_tab("http://www.crtvg.es/crtvg/camaras-web/lugo-fixa")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara2=Frame(root)
	boton_camara2.pack(fill=BOTH, expand=YES)
	boton_camara2.place(x=645, y=600)
	Button(boton_camara2, image=camara_logo, command=lambda:[webbrowser.open_new_tab("http://www.crtvg.es/crtvg/camaras-web/o-cebreiro")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara3=Frame(root)
	boton_camara3.pack(fill=BOTH, expand=YES)
	boton_camara3.place(x=330, y=480)
	Button(boton_camara3, image=camara_logo, command=lambda:[webbrowser.open_new_tab("http://www.crtvg.es/crtvg/camaras-web/portomarin")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()


	pass

def ourense():

	botonBienvenido=Frame(root, width=1024, height=1024)
	botonBienvenido.pack(fill=BOTH, expand=YES)
	botonBienvenido.place(x=0, y=0)
	Button(botonBienvenido, image=mapa_ourense, cursor="spider", justify="center", bd=0, relief="raised", background="Black", activebackground='black', font=("URW Chancery L", 15)).pack()

	boton_camara1=Frame(root)
	boton_camara1.pack(fill=BOTH, expand=YES)
	boton_camara1.place(x=405, y=220)
	Button(boton_camara1, image=camara_logo, command=lambda:[webbrowser.open_new_tab("http://www.crtvg.es/crtvg/camaras-web/ourense-fixa")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara2=Frame(root)
	boton_camara2.pack(fill=BOTH, expand=YES)
	boton_camara2.place(x=453, y=284)
	Button(boton_camara2, image=camara_logo, command=lambda:[webbrowser.open_new_tab("http://www.crtvg.es/crtvg/camaras-web/ourense-mobil")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara3=Frame(root)
	boton_camara3.pack(fill=BOTH, expand=YES)
	boton_camara3.place(x=350, y=430)
	Button(boton_camara3, image=camara_logo, command=lambda:[webbrowser.open_new_tab("http://www.crtvg.es/crtvg/camaras-web/celanova")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara4=Frame(root)
	boton_camara4.pack(fill=BOTH, expand=YES)
	boton_camara4.place(x=840, y=310)
	Button(boton_camara4, image=camara_logo, command=lambda:[webbrowser.open_new_tab("http://www.crtvg.es/crtvg/camaras-web/cabeza-de-manzaneda-estacion-3")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara5=Frame(root)
	boton_camara5.pack(fill=BOTH, expand=YES)
	boton_camara5.place(x=775, y=280)
	Button(boton_camara5, image=camara_logo, command=lambda:[webbrowser.open_new_tab("http://www.crtvg.es/crtvg/camaras-web/cabeza-de-manzaneda-estacion-2")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara6=Frame(root)
	boton_camara6.pack(fill=BOTH, expand=YES)
	boton_camara6.place(x=800, y=340)
	Button(boton_camara6, image=camara_logo, command=lambda:[webbrowser.open_new_tab("http://www.crtvg.es/crtvg/camaras-web/cabeza-de-manzaneda-estacion-1")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara7=Frame(root)
	boton_camara7.pack(fill=BOTH, expand=YES)
	boton_camara7.place(x=757, y=341)
	Button(boton_camara7, image=camara_logo, command=lambda:[webbrowser.open_new_tab("http://www.crtvg.es/crtvg/camaras-web/cabeza-de-manzaneda")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara8=Frame(root)
	boton_camara8.pack(fill=BOTH, expand=YES)
	boton_camara8.place(x=918, y=190)
	Button(boton_camara8, image=camara_logo, command=lambda:[webbrowser.open_new_tab("http://www.crtvg.es/crtvg/camaras-web/a-rua-2")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()


	pass


def pontevedra():

	botonBienvenido=Frame(root, width=1024, height=1024)
	botonBienvenido.pack(fill=BOTH, expand=YES)
	botonBienvenido.place(x=0, y=0)
	Button(botonBienvenido, image=mapa_pontevedra, cursor="spider", justify="center", bd=0, relief="raised", background="Black", activebackground='black', font=("URW Chancery L", 15)).pack()

	boton_camara1=Frame(root)
	boton_camara1.pack(fill=BOTH, expand=YES)
	boton_camara1.place(x=400, y=600)
	Button(boton_camara1, image=camara_logo, command=lambda:[webbrowser.open_new_tab("http://www.crtvg.es/crtvg/camaras-web/a-guarda")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara2=Frame(root)
	boton_camara2.pack(fill=BOTH, expand=YES)
	boton_camara2.place(x=410, y=450)
	Button(boton_camara2, image=camara_logo, command=lambda:[webbrowser.open_new_tab("http://www.crtvg.es/crtvg/camaras-web/baiona")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara3=Frame(root)
	boton_camara3.pack(fill=BOTH, expand=YES)
	boton_camara3.place(x=1025, y=85)
	Button(boton_camara3, image=camara_logo, command=lambda:[webbrowser.open_new_tab("http://www.crtvg.es/crtvg/camaras-web/concello-lalin")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara4=Frame(root)
	boton_camara4.pack(fill=BOTH, expand=YES)
	boton_camara4.place(x=397, y=170)
	Button(boton_camara4, image=camara_logo, command=lambda:[webbrowser.open_new_tab("http://www.crtvg.es/crtvg/camaras-web/o-grove")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara5=Frame(root)
	boton_camara5.pack(fill=BOTH, expand=YES)
	boton_camara5.place(x=609, y=209)
	Button(boton_camara5, image=camara_logo, command=lambda:[webbrowser.open_new_tab("http://www.crtvg.es/crtvg/camaras-web/pontevedra")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara6=Frame(root)
	boton_camara6.pack(fill=BOTH, expand=YES)
	boton_camara6.place(x=500, y=280)
	Button(boton_camara6, image=camara_logo, command=lambda:[webbrowser.open_new_tab("http://www.crtvg.es/crtvg/camaras-web/portonovo")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara7=Frame(root)
	boton_camara7.pack(fill=BOTH, expand=YES)
	boton_camara7.place(x=490, y=228)
	Button(boton_camara7, image=camara_logo, command=lambda:[webbrowser.open_new_tab("http://www.crtvg.es/crtvg/camaras-web/sanxenxo")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara8=Frame(root)
	boton_camara8.pack(fill=BOTH, expand=YES)
	boton_camara8.place(x=535, y=395)
	Button(boton_camara8, image=camara_logo, command=lambda:[webbrowser.open_new_tab("http://www.crtvg.es/crtvg/camaras-web/vigo-mobil")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()


	pass


def tarragona():

	botonBienvenido=Frame(root, width=1024, height=1024)
	botonBienvenido.pack(fill=BOTH, expand=YES)
	botonBienvenido.place(x=0, y=0)
	Button(botonBienvenido, image=mapa_tarragona, cursor="spider", justify="center", bd=0, relief="raised", background="Black", activebackground='black', font=("URW Chancery L", 15)).pack()

	boton_camara1=Frame(root)
	boton_camara1.pack(fill=BOTH, expand=YES)
	boton_camara1.place(x=540, y=200)
	Button(boton_camara1, image=camara_logo, command=lambda:[webbrowser.open_new_tab("https://www.insecam.org/en/view/831875/")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara2=Frame(root)
	boton_camara2.pack(fill=BOTH, expand=YES)
	boton_camara2.place(x=450, y=400)
	Button(boton_camara2, image=camara_logo, command=lambda:[webbrowser.open_new_tab("https://www.insecam.org/en/view/840795/")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()


	pass


def madrid():

	botonBienvenido=Frame(root, width=1024, height=1024)
	botonBienvenido.pack(fill=BOTH, expand=YES)
	botonBienvenido.place(x=0, y=0)
	Button(botonBienvenido, image=mapa_madrid, cursor="spider", justify="center", bd=0, relief="raised", background="Black", activebackground='black', font=("URW Chancery L", 15)).pack()

	boton_camara1=Frame(root)
	boton_camara1.pack(fill=BOTH, expand=YES)
	boton_camara1.place(x=540, y=200)
	Button(boton_camara1, image=camara_logo, command=lambda:[webbrowser.open_new_tab("https://www.insecam.org/en/view/829071/")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara2=Frame(root)
	boton_camara2.pack(fill=BOTH, expand=YES)
	boton_camara2.place(x=450, y=400)
	Button(boton_camara2, image=camara_logo, command=lambda:[webbrowser.open_new_tab("http://217.217.88.135:91/view/viewer_index.shtml?id=1036")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara3=Frame(root)
	boton_camara3.pack(fill=BOTH, expand=YES)
	boton_camara3.place(x=20, y=40)
	Button(boton_camara3, image=camara_logo, command=lambda:[webbrowser.open_new_tab("http://212.170.201.205/view/viewer_index.shtml?id=637")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara4=Frame(root)
	boton_camara4.pack(fill=BOTH, expand=YES)
	boton_camara4.place(x=300, y=40)
	Button(boton_camara4, image=camara_logo, command=lambda:[webbrowser.open_new_tab("http://37.10.168.209/view/viewer_index.shtml?id=34")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()


	boton_camara5=Frame(root)
	boton_camara5.pack(fill=BOTH, expand=YES)
	boton_camara5.place(x=20, y=450)
	Button(boton_camara5, image=camara_logo, command=lambda:[webbrowser.open_new_tab("http://194.179.40.154:8081/cgi-bin/guestimage.html")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara6=Frame(root)
	boton_camara6.pack(fill=BOTH, expand=YES)
	boton_camara6.place(x=56, y=500)
	Button(boton_camara6, image=camara_logo, command=lambda:[webbrowser.open_new_tab("https://www.insecam.org/en/view/206103/")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara7=Frame(root)
	boton_camara7.pack(fill=BOTH, expand=YES)
	boton_camara7.place(x=800, y=500)
	Button(boton_camara7, image=camara_logo, command=lambda:[webbrowser.open_new_tab("http://195.235.209.122/view/viewer_index.shtml?id=4038")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara8=Frame(root)
	boton_camara8.pack(fill=BOTH, expand=YES)
	boton_camara8.place(x=800, y=500)
	Button(boton_camara8, image=camara_logo, command=lambda:[webbrowser.open_new_tab("http://2.136.59.74:8080/view/viewer_index.shtml?id=290")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara9=Frame(root)
	boton_camara9.pack(fill=BOTH, expand=YES)
	boton_camara9.place(x=700, y=100)
	Button(boton_camara9, image=camara_logo, command=lambda:[webbrowser.open_new_tab("http://185.107.0.37/view/index.shtml")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara10=Frame(root)
	boton_camara10.pack(fill=BOTH, expand=YES)
	boton_camara10.place(x=470, y=310)
	Button(boton_camara10, image=camara_logo, command=lambda:[webbrowser.open_new_tab("https://www.insecam.org/en/view/825581/")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara11=Frame(root)
	boton_camara11.pack(fill=BOTH, expand=YES)
	boton_camara11.place(x=470, y=310)
	Button(boton_camara11, image=camara_logo, command=lambda:[webbrowser.open_new_tab("https://www.insecam.org/en/view/543795/")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()



	pass


def andalucia():

	botonBienvenido=Frame(root, width=1024, height=1024)
	botonBienvenido.pack(fill=BOTH, expand=YES)
	botonBienvenido.place(x=0, y=0)
	Button(botonBienvenido, image=mapa_andalucia, cursor="spider", justify="center", bd=0, relief="raised", background="Black", activebackground='black', font=("URW Chancery L", 15)).pack()

	boton_camara1=Frame(root)
	boton_camara1.pack(fill=BOTH, expand=YES)
	boton_camara1.place(x=460, y=355)
	Button(boton_camara1, image=camara_logo, command=lambda:[webbrowser.open_new_tab("https://www.insecam.org/en/view/816214/")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara2=Frame(root)
	boton_camara2.pack(fill=BOTH, expand=YES)
	boton_camara2.place(x=550, y=500)
	Button(boton_camara2, image=camara_logo, command=lambda:[webbrowser.open_new_tab("https://www.insecam.org/en/view/840559/")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara3=Frame(root)
	boton_camara3.pack(fill=BOTH, expand=YES)
	boton_camara3.place(x=380, y=400)
	Button(boton_camara3, image=camara_logo, command=lambda:[webbrowser.open_new_tab("https://www.insecam.org/en/view/810791/")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara4=Frame(root)
	boton_camara4.pack(fill=BOTH, expand=YES)
	boton_camara4.place(x=654, y=495)
	Button(boton_camara4, image=camara_logo, command=lambda:[webbrowser.open_new_tab("https://www.insecam.org/en/view/239938/")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara5=Frame(root)
	boton_camara5.pack(fill=BOTH, expand=YES)
	boton_camara5.place(x=1040, y=170)
	Button(boton_camara5, image=camara_logo, command=lambda:[webbrowser.open_new_tab("https://www.skylinewebcams.com/it/webcam/espana/comunidad-valenciana/alicante/benidorm-playa-alicante.html")], cursor="heart", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara6=Frame(root)
	boton_camara6.pack(fill=BOTH, expand=YES)
	boton_camara6.place(x=1050, y=30)
	Button(boton_camara6, image=camara_logo, command=lambda:[webbrowser.open_new_tab("http://212.170.100.189/view/view.shtml?id=12220&imagepath=%2Fmjpg%2Fvideo.mjpg%3Fcamera%3D1&size=1")], cursor="heart", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara7=Frame(root)
	boton_camara7.pack(fill=BOTH, expand=YES)
	boton_camara7.place(x=1000, y=190)
	Button(boton_camara7, image=camara_logo, command=lambda:[webbrowser.open_new_tab("https://www.skylinewebcams.com/it/webcam/espana/comunidad-valenciana/alicante/alicante-playa-albir.html")], cursor="heart", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()


	pass


def asturias():

	botonBienvenido=Frame(root, width=1024, height=1024)
	botonBienvenido.pack(fill=BOTH, expand=YES)
	botonBienvenido.place(x=0, y=0)
	Button(botonBienvenido, image=mapa_asturias, cursor="spider", justify="center", bd=0, relief="raised", background="Black", activebackground='black', font=("URW Chancery L", 15)).pack()

	boton_camara1=Frame(root)
	boton_camara1.pack(fill=BOTH, expand=YES)
	boton_camara1.place(x=460, y=355)
	Button(boton_camara1, image=camara_logo, command=lambda:[webbrowser.open_new_tab("https://www.insecam.org/en/view/168451/")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara2=Frame(root)
	boton_camara2.pack(fill=BOTH, expand=YES)
	boton_camara2.place(x=470, y=100)
	Button(boton_camara2, image=camara_logo, command=lambda:[webbrowser.open_new_tab("https://www.insecam.org/en/view/279950/")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()


def barcelona():

	botonBienvenido=Frame(root, width=1024, height=1024)
	botonBienvenido.pack(fill=BOTH, expand=YES)
	botonBienvenido.place(x=0, y=0)
	Button(botonBienvenido, image=mapa_barcelona, cursor="spider", justify="center", bd=0, relief="raised", background="Black", activebackground='black', font=("URW Chancery L", 15)).pack()

	boton_camara1=Frame(root)
	boton_camara1.pack(fill=BOTH, expand=YES)
	boton_camara1.place(x=700, y=355)
	Button(boton_camara1, image=camara_logo, command=lambda:[webbrowser.open_new_tab("https://www.insecam.org/en/view/837447/")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara2=Frame(root)
	boton_camara2.pack(fill=BOTH, expand=YES)
	boton_camara2.place(x=470, y=100)
	Button(boton_camara2, image=camara_logo, command=lambda:[webbrowser.open_new_tab("https://www.insecam.org/en/view/279950/")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara3=Frame(root)
	boton_camara3.pack(fill=BOTH, expand=YES)
	boton_camara3.place(x=510, y=340)
	Button(boton_camara3, image=camara_logo, command=lambda:[webbrowser.open_new_tab("https://www.insecam.org/en/view/807433/")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara4=Frame(root)
	boton_camara4.pack(fill=BOTH, expand=YES)
	boton_camara4.place(x=1070, y=270)
	Button(boton_camara4, image=camara_logo, command=lambda:[webbrowser.open_new_tab("https://www.insecam.org/en/view/484189/")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara5=Frame(root)
	boton_camara5.pack(fill=BOTH, expand=YES)
	boton_camara5.place(x=1030, y=320)
	Button(boton_camara5, image=camara_logo, command=lambda:[webbrowser.open_new_tab("https://www.insecam.org/en/view/242398/")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara6=Frame(root)
	boton_camara6.pack(fill=BOTH, expand=YES)
	boton_camara6.place(x=980, y=400)
	Button(boton_camara6, image=camara_logo, command=lambda:[webbrowser.open_new_tab("https://www.insecam.org/en/view/484189/")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara7=Frame(root)
	boton_camara7.pack(fill=BOTH, expand=YES)
	boton_camara7.place(x=850, y=600)
	Button(boton_camara7, image=camara_logo, command=lambda:[webbrowser.open_new_tab("https://www.insecam.org/en/view/242397/")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara8=Frame(root)
	boton_camara8.pack(fill=BOTH, expand=YES)
	boton_camara8.place(x=645, y=432)
	Button(boton_camara8, image=camara_logo, command=lambda:[webbrowser.open_new_tab("https://www.insecam.org/en/view/435100/")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()

	boton_camara9=Frame(root)
	boton_camara9.pack(fill=BOTH, expand=YES)
	boton_camara9.place(x=940, y=480)
	Button(boton_camara9, image=camara_logo, command=lambda:[webbrowser.open_new_tab("https://www.insecam.org/en/view/832987/")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()


def zaragoza():

	botonBienvenido=Frame(root, width=1024, height=1024)
	botonBienvenido.pack(fill=BOTH, expand=YES)
	botonBienvenido.place(x=0, y=0)
	Button(botonBienvenido, image=mapa_zaragoza, cursor="spider", justify="center", bd=0, relief="raised", background="Black", activebackground='black', font=("URW Chancery L", 15)).pack()

	boton_camara1=Frame(root)
	boton_camara1.pack(fill=BOTH, expand=YES)
	boton_camara1.place(x=460, y=355)
	Button(boton_camara1, image=camara_logo, command=lambda:[webbrowser.open_new_tab("https://www.insecam.org/en/view/837083/")], cursor="target", justify="center", bd=0, relief="flat", overrelief="raised", background="black", activebackground='black').pack()






#Ventana Inicial.

root = Tk()
root.title("··· Gosoff - OffShell System ···")
root.geometry("1124x650+75+50")
root.resizable(width=False, height=False)
root.config(bg='black')

root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='primate.gif'))

#Barra MenuBar.

barramenu=Menu(root, relief=RAISED, cursor="heart", activebackground='darkgreen', foreground='orange', activeforeground='orange', activeborderwidth=1, bg='Black', bd=1)


root.config(menu=barramenu, width=300, height=300, cursor="heart")


archMenu=Menu(barramenu, tearoff=0)
archSpain=Menu(barramenu, tearoff=0)

barramenu.add_cascade(label="Menú", menu=archMenu, font=("URW Chancery L", 14))


archMenu.add_command(label="Mapa España", command=lambda:[españa()], font=("URW Chancery L", 13), background='black', activebackground='darkgreen', foreground='orange', activeforeground='orange')

archMenu.add_command(label="Barcelona", command=lambda:[barcelona()], font=("URW Chancery L", 13), background='black', activebackground='darkgreen', foreground='orange', activeforeground='orange')

archMenu.add_command(label="Madrid", command=lambda:[madrid()], font=("URW Chancery L", 13), background='black', activebackground='darkgreen', foreground='orange', activeforeground='orange')

archMenu.add_command(label="A Coruña", command=lambda:[coruna()], font=("URW Chancery L", 13), background='black', activebackground='darkgreen', foreground='orange', activeforeground='orange')

archMenu.add_command(label="Pontevedra", command=lambda:[pontevedra()], font=("URW Chancery L", 13), background='black', activebackground='darkgreen', foreground='orange', activeforeground='orange')

archMenu.add_command(label="Ourense", command=lambda:[ourense()], font=("URW Chancery L", 13), background='black', activebackground='darkgreen', foreground='orange', activeforeground='orange')

archMenu.add_command(label="Lugo", command=lambda:[lugo()], font=("URW Chancery L", 13), background='black', activebackground='darkgreen', foreground='orange', activeforeground='orange')

archMenu.add_command(label="Asturias", command=lambda:[asturias()], font=("URW Chancery L", 13), background='black', activebackground='darkgreen', foreground='orange', activeforeground='orange')

archMenu.add_command(label="Zaragoza", command=lambda:[zaragoza()], font=("URW Chancery L", 13), background='black', activebackground='darkgreen', foreground='orange', activeforeground='orange')

archMenu.add_command(label="Andalucía", command=lambda:[andalucia()], font=("URW Chancery L", 13), background='black', activebackground='darkgreen', foreground='orange', activeforeground='orange')

archMenu.add_command(label="Tarragona", command=lambda:[tarragona()], font=("URW Chancery L", 13), background='black', activebackground='darkgreen', foreground='orange', activeforeground='orange')





#Imágenes.
mundo_logo=PhotoImage(file="mundo_logo.gif")
españa_logo=PhotoImage(file="españa.gif")
mapa_coruna=PhotoImage(file="mapa_coruna.gif")
mapa_lugo=PhotoImage(file="lugo.gif")
mapa_ourense=PhotoImage(file="ourense.gif")
mapa_pontevedra=PhotoImage(file="pontevedra.gif")
dedo_logo=PhotoImage(file="prismaticos.gif")
coruna1_logo=PhotoImage(file="coruna1.gif")
coruna_ciudad=PhotoImage(file="coruna.gif")
mapa_tarragona=PhotoImage(file="mapa_tarragona.gif")
mapa_madrid=PhotoImage(file="mapa_madrid.gif")
mapa_andalucia=PhotoImage(file="andalucia.gif")
mapa_asturias=PhotoImage(file="asturias.gif")
mapa_barcelona=PhotoImage(file="barcelona.gif")
mapa_zaragoza=PhotoImage(file="zaragoza.gif")
mapa_francia=PhotoImage(file="francia.gif")

camara_logo=PhotoImage(file="camara_logo.gif")


#Imagen de Fondo.
botonBienvenido=Frame(root, width=1024, height=1024)
botonBienvenido.pack(fill=BOTH, expand=YES)
botonBienvenido.place(x=0, y=0)
Button(botonBienvenido, image=mundo_logo, cursor="spider", justify="center", bd=0, relief="raised", background="Black", activebackground='black', font=("URW Chancery L", 15)).pack()



label1=Label(root, text="OffShell System", font=("URW Chancery L", 13), foreground="DarkRed", background="black").place(x=1015, y=618)
label2=Label(root, text="Comunidad", font=("URW Chancery L", 12), foreground="DarkRed", background="black").place(x=1033, y=597)



#salida del bucle y app.

root.mainloop()
