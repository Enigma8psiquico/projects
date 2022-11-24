#!/usr/bin/env python
""" encriptador de textos """
# Nota:
# ~ Este programa solo se inicia desde la terminal del windows
# ~ La funcion de encriptar palabras tovia no esta disponible 
# ~ Pero si esta disponible la de convertir archivos de texto

#!/usr/bin/env python
from datetime import datetime 
import os 
import sys

class App(object):
    global nombre 
    date = datetime.now()
    nombre = date.strftime("%d %B - %H:%M")
    nombre = str(f"{nombre}.txt")
    def __init__(self):
        os.system(" @title Encripton v1.0 ᓚᘏᗢ ")
        self.matrisPortada()

    def matrisPortada(self):
        self.matris = [[0,0,0,0,0,0,0,0,0],
                       [0,0,2,0,0,0,0,0,0]]

        for x in self.matris:
            for y in self.matris:
                pass

        self.funcion2()

    def funcion2(self):
        os.system("cls")
        print("""
Ingresa la opcion del programa 
0) archivo de texto
1) texto 
        """)
        self.opcion = input(">>> ")

        if self.opcion == "0":
            self.archivo()
        if self.opcion == "exit()":
            os.system("pause > null | set/p = pulsa enter para salir ...")
        else:
            App()

    def archivo(self):
        # listo 
        self.archivoTo = input("ingresa el nombre del archivo: ")
        try:
            if os.system(f"if exist {self.archivoTo} (echo si se encontro)") != OSError:
                print("cargando arCHIVO...")    
                self.archivoToEncriptar = open(f"{self.archivoTo}","r")
                self.conversion(self.archivoToEncriptar)
        except:
            if os.system(f"if not exist {self.archivoTo} (echo no se encontro)") is not OSError:
                os.system("pause > null | set/p = archivo not found")
        
    def conversion(self, archivo): 
        # funcion de conversion 
        self.texto = str(archivo.readlines()) # el texto se almacena en una variable 
        self.newtexto = self.convert(self.texto)# convierte 
        self.newArchivo(self.newtexto)
        

    def convert(self,texto):
        texto = (
        texto.replace("a","ç´-gg5tg+*si^vb+-.+ed46-)(=/&%/&/&%/&4ce45")
        .replace("b","tvfrv+´.+ç´ñ.+`.ñ+9tP(=)?/(?=rr`v%TUWe")
        .replace("c","oi23·$v$%YQW·dce ed345768e3f3-··$rf4rf")
        .replace("d","23de·F$·EF·$RF4%/&U/&(=?0'7¡0/=?&%(/8(&%/$6)")
        .replace("f","2E3f3ee4fr$456$%Ty&&/&())=)?^+`ñ+ñ=HY%y5")
        .replace("g","dw2e·dF·EF·efef3´ñ.+`..+`.+`ñ+`la+.`+%%")
        .replace("h","E·DE%6H/7k%&HRI//((I8i)7/U7&%4r$4Y&/U")
        .replace("i","8)(HJ/&/&/&%&%I´+`ñ)(=?=?(¿)//%7+`ñ`k`p´ñ")
        .replace("j","r3+´-+--v+r`+`-+`.ñ+`.v)(=&(&&=&/%HTr.+`v")
        .replace("k","+`-+c`d+è.vç´ñ.`+-´+-ç-.´%()OI/UKYñ.ç´-`+")
        .replace("l","+`ñwcde`vpreplve`pv-.´ç.--..´ñ.+`+`ñ")
        .replace("m","e.v`p,ewew`dcàqdce¨-ç´-ç_ç´`p¡`¡'¡'-.-:+ç-&")
        .replace("n","`pl.`p.ve`prv`.r`gpvk%&/()709=(=??=&%&_&%&")
        .replace("o","`4%TH&YH&JH7ç+objec++`-+`foi3et+-tñ+`r`")
        .replace("p","pokpcde%&`%T$Gr+4`ñ+ñ5´-$&%/çñ+ç´./&TH67&%")
        .replace("q","p.`65%&p%_&%/$·$R·$·ªª!!!Dç5/&($/E%&·W·$%&%/()&/=REHGR)")
        .replace("r","+ñ334·+`ñf4f45g`67&/I&()4ñ5+`4r`plfe")
        .replace("s","p`lrp,lpo4rkvg4ñ+`ñ-d+2`ñ3%/54`ñ+`45$%&")
        .replace("t","`plec3%$T$%tl5g5`pol`p34(/O(=)95+´`f+3`4f")
        .replace("u","`p3de,`p4f,43`pl'0lo'0320837r7g4634´ñ.`p+`ll`p")
        .replace("v","po3e´4ñ.t`plg5`pl`gp5,5//(O/%)$%/85.+$%&-")
        .replace("w","de`p,l3eet`p4rv4p·$T%W,vi5&/()(/%`po,ptor,")
        .replace("y","po2k3pod,e443t!$%!·$%UEERWFT$G$4.,ñl45g`4,g3")
        .replace("x","po,3epdo,39fw09jf3094/(()5$QER$%&&(/&(/·)")
        .replace("z","o2p,wcp,wpo%$VCSA%&%($%Y46yW··&$%·$%$·(%&/%&·%"))
        return texto

    def newArchivo(self, texto):
        self.archivo = open("dede.mb","w")
        self.archivo.write(texto)
        self.archivo.close()



App()
