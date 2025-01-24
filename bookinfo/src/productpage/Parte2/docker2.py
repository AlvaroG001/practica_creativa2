#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import os
import logging
from os import close
import sys
import json
import time

from subprocess import call
os.system('git clone https://github.com/carlossalval99/practica_creativa2.git')
variable = os.environ.get('GROUP_NUMBER')      
fin = open("/usr/src/app/practica_creativa2/bookinfo/src/productpage/templates/index.html", 'r') # in file
fout = open("/usr/src/app/practica_creativa2/bookinfo/src/productpage/templates/index2.html", 'w') # out file
for line in fin:
  if "{% block title %}Simple Bookstore App{% endblock %}" in line :
   fout.write("{% block title %}"+"Simple Bookstore App {}".format(variable) + "{% endblock %}")
  else:
   fout.write(line)
fin.close()
fout.close()

call(["cp","/usr/src/app/practica_creativa2/bookinfo/src/productpage/templates/index2.html","/usr/src/app/practica_creativa2/bookinfo/src/productpage/templates/index.html"])
call(["rm","/usr/src/app/practica_creativa2/bookinfo/src/productpage/templates/index2.html"])

fin = open("/usr/src/app/practica_creativa2/bookinfo/src/productpage/templates/productpage.html", 'r') # in file
fout = open("/usr/src/app/practica_creativa2/bookinfo/src/productpage/templates/productpage2.html", 'w') # out file
for line in fin:
  if "{% block title %}Simple Bookstore App{% endblock %}" in line :
   fout.write("{% block title %}"+"Simple Bookstore App {}".format(variable) + "{% endblock %}")
  else:
   fout.write(line)
fin.close()
fout.close()

call(["cp","/usr/src/app/practica_creativa2/bookinfo/src/productpage/templates/productpage2.html","/usr/src/app/practica_creativa2/bookinfo/src/productpage/templates/productpage.html"])
call(["rm","/usr/src/app/practica_creativa2/bookinfo/src/productpage/templates/productpage2.html"])


os.system('pip3 install -r /usr/src/app/practica_creativa2/bookinfo/src/productpage/requirements.txt')
os.system(' python3 /usr/src/app/practica_creativa2/bookinfo/src/productpage/productpage_monolith.py 9080')






#a=open("practica_creativa2/bookinfo/src/productpage/templates/productpage.html", "r+")
#aux=open("practica_creativa2/bookinfo/src/productpage/templates/auxiliar.html", "w+")
#for line in a:
#    if ("{} block title {}Simple Bookstore App{} endblock {}".format('{%', '%}', '{%', '%}')) in line:
#        print("Encontrada")
#        aux.write("{} block title {}Simple Bookstore App{} {} endblock {}".format('{%', '%}', os.environ.get('GROUP_NUMBER'), '{%', '%}'))
#    else:
#        aux.write(line)
#a.close()
#aux.close()

#a=open("practica_creativa2/bookinfo/src/productpage/templates/productpage.html", "r+")
#aux=open("practica_creativa2/bookinfo/src/productpage/templates/auxiliar.html", "w+")
#for line in aux:
#    a.write(line)
#a.close()
#aux.close()


#variable = os.environ.get('GROUP_NUMBER')
#fin = open("practica_creativa2/bookinfo/src/productpage/templates/productpage.html", 'r') # in file
#fout = open("productpage2.html", 'w') # out file
#for line in fin:
   # if "{} block title {}Simple Bookstore App{} endblock {}".format('{%', '%}', '{%', '%}') in line:
   #     fout.write("{} block title {}Simple Bookstore App"+ variable +"{} endblock {}".format('{%', '%}', '{%', '%}'))
   # else :
   #     fout.write(line)
#fin.close()
#fout.close()

#call(["mv","productpage2.html","practica_creativa2/bookinfo/src/productpage/templates/productpage.html"])