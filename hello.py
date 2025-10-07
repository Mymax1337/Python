#!/usr/bin/env python3

"""Hello WOrld multi linguas.

Dependendo da lingua configurada no ambiente
o pograma exibe a mensagem correspondente.

Como usar:

Tenha a variavel LANG devidamente configurada ex:

Expor LANG=pt_BR

Execucao:

Python3 hello.py

ou

./hello.py
"""
#Dunder significa 2 underlines no comeco e no fim
__version__ = "3.12.3"
__author__ = "Mymax1337"
__license__ ="Unlicense"

import os

current_language = os.getenv("LANG", "pt_BR")[:5]
msg = "Hello, Wold!"

if current_language == "pt_BR":
    msg = "Ola, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao,Mundo!"

    print(msg)
