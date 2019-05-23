from os import system, name
import math

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def listar_materiais(pts_obj):
    print('Lista de materiais')
    print('1. Tomadas fêmea\t-\t', pts_rede)
    print('2. Patch Cords\t-\t', pts_rede)
    print('3. Espelhos\t-\t', pts_telecom)
    print('4. Cabos da malha horizontal\t-\t', math.ceil(pts_rede*tam_cabos/305))
    print('5. Etiquetas)
    print('\tÁrea de trabalho\t-\t', 3*pts_telecom)
    print('\tMalha horizontal\t-\t', 4*pts_telecom)
    print('6. Patch Panels\t-\t', int((pts_rede+pts_cftv+pts_voz)/24))
    print('7. Patch Cable')
    print('\tDados\t-\tAzul de 3m: ', pts_rede)
    print('\tCFTV\t-\tVermelho de 3m: ', pts_cftv)
    print('\tVoz\t-\tAmarelo de 3m: ', pts_voz)
    print('8. Organizadores de cabo frontal\t-\t')
    print('9. Etiquetas para Patch Panel\t-\t', pts_rede + pts_cftv + pts_voz)
    print('10. Tipo e tamanho do rack\t-\t')
    print('11. Acessórios para o rack\t-\t', )
    print('12. Acessórios para o acabamento\t-\t')



print("Bem vindo ao Network Calculator. Meu nome é Delsin e eu vou te ajudar a projetar sua rede, fazendo os cálculos de materiais.")
print("Digite o número de pontos de telecom da sua rede:")
pts_telecom = input()
clear()
print("Digite o número de pontos de rede(simples):")
pts_rede = input()
clear()
print("Digite o número de pontos de CFTV IP:")
pts_cftv = input()
clear()
print("Digite o número de pontos de voz sobre IP:")
pts_voz = input()
clear()
print("O seu rack estará em um local fechado ou na área de trabalho?(Use 'a' ou 'f')")
if input() == 'a': rack_aberto = True
else: rack_aberto = False
print("Qual será o tamanho dos cabos na malha horizontal?")
tam_cabos = input()
pts_obj = {pts_cftv, pts_telecom, pts_rede, pts_voz, tam_cabos, rack_aberto}
listar_materiais(pts_obj)

