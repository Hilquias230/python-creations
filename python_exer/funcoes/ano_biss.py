#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ano_bi (ano):
    if (ano %400 == 0) or (ano %4 == 0 and ano %100 != 0):
        return True
    else:
        return False
    
def dias_mes (ano, m):
    if m == 1 or m == 3 or m == 5 or m == 7:
        return 31
    elif m == 8 or m == 10 or m == 12:
        return 31
    elif m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    elif m == 2:
        if ano_bi(ano):
            return 29
        else:
            return 28
    else:
        return -1

def principal():
    print("Informe as datas")
    ano = int(input("Digite o ano aqui: "))
    mes = int(input("Digite o número do mês: "))

    print(f"Ano bissxeto {ano_bi(ano)}")
    print(f"Dias do mês: {dias_mes(ano, mes)}")

if __name__ == "__main__":
    principal()