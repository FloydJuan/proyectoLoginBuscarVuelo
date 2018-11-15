from flask import Flask, request, g, redirect, url_for, render_template, flash, session
import flask
import sys
from flask import json
import os

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = set(['txt','mp3'])

# Inicializacion de variables
app = Flask(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app.secret_key = 'random string'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
filename = ""

#@app.route("/", methods=["GET","POST"])

@app.route('/iniciarsesion.html',methods=["GET","POST"])
def inicio():
    res='iniciarsesion.html'
    if(request.method=='POST'):
        usr= request.form['usuario']
        con= request.form['password']
        arc=open('usuarios.txt')
        lineas=arc.readlines()
        Dic={}
        for i in lineas:
            lista=i.strip().split("/")
            Dic[lista[0]]=lista[1]
        arc.close()
        if(usr in Dic):
            if(Dic[usr]==con):
                res='vuela.html'
            
        
    entries={}
    entries["numero"]=0
    return render_template(res,entries=entries)
#print(inicio("Sebastian","4536"))

#@app.route('/registro.html',methods=["GET","POST"])
def reg():
    print(4)
    return render_template('registro.html',entries={})
@app.route('/registro.html',methods=["GET","POST"])
def registrar():
    print(request.method)
    if(request.method=='POST'):
        usr= request.form['nombre']
        con= request.form['password']
        arc=open("usuarios.txt")
        lineas=arc.readlines()
        dic={}
        for i in lineas:
            lista=i.strip().split("/")
            dic[lista[0]]=lista[1]
        dic[usr]=con
        arc.close()
        arc=open("usuarios.txt","w")
        for i in dic:
            arc.write(i+"/"+dic[i]+"\n")
        arc.close()
    return render_template('registro.html',entries={})
@app.route('/',methods=["GET","POST"])
def paginaWeb():
    return render_template('paginaWeb.html')
@app.route('/paginaWeb.html',methods=["GET","POST"])
def paginaWeb2():
    return render_template('paginaWeb.html')

@app.route('/vuela.html',methods=["GET","POST"])
def volar():
    return render_template('vuela.html')

def leerArchivo():
    """
    """
    archivo=open('datosvuelos.txt','r')
    for i in range(14):
        archivo.readline()
    aeropuertos=[]
    for i in range(15,37):
        linea=archivo.readline()
        aeropuertos.append(linea)
    for i in range (38,61):
        archivo.readline()
    vuelos=[]
    for i in range(62,500):
        linea=archivo.readline()
        vuelos.append(linea)
    archivo.close()
    return vuelos

@app.route('/vuela',methods=['GET','POST'])
def imprimirVuelos():
    vuelos=leerArchivo()
    entries={"vuelos":[]}
    if (request.method=='POST'):
        origen=request.form['vuelo']
        regreso=request.form['regreso']
        aerolinea=request.form['aerolinea']    
        for linea in vuelos:
            tmp=linea.split()
            if(tmp[2]==origen and tmp[4]==regreso and tmp[0]==aerolinea):
                entries["vuelos"].append(linea)
        entries["numero"]=len(entries["vuelos"])
    return render_template('vuela.html', entries=entries)
if __name__ == '__main__':
    app.run()
    
        
