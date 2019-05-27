from os import system, name
import math

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def apresentar():
    print("Bem vindo ao Network Calculator. Meu nome é Delsin e eu vou te ajudar a projetar sua rede, fazendo os cálculos de materiais.")

def abrir():
    print('abrir')

def salvar():
    print('salvar')
    input()

def salvar_como():
    print('salvar como...')
    input()

def sair():
    print('Saindo...')


def mostrar_menu():
    clear()
    print("O que deseja fazer?")
    print("1. Novo cálculo de rede")
    print("2. Abrir")
    print("3. Salvar")
    print("4. Salvar como...")
    print("0. Sair")

def perguntar_especificacoes_da_rede():
    rede_obj = {}
    print("Digite o número de pontos de telecom da sua rede:")
    rede_obj[pts_telecom] = input()
    clear()
    print("Digite o número de pontos de rede(simples):")
    rede_obj[pts_rede] = input()
    clear()
    print("Digite o número de pontos de CFTV IP:")
    rede_obj[pts_cftv] = input()
    clear()
    print("Digite o número de pontos de voz sobre IP:")
    rede_obj[pts_voz] = input()
    clear()
    print("O seu rack estará em um local fechado ou na área de trabalho?(Use 'a' ou 'f')")
    if input() == 'a': rede_obj[rack_aberto] = True
    else: rede_obj[rack_aberto] = False
    print("Qual será o tamanho dos cabos na malha horizontal?")
    rede_obj[tam_cabos] = input()
    return rede_obj

def calcular_materiais():
    print('calcular')

def listar_materiais(pts_obj):
    print('listar')