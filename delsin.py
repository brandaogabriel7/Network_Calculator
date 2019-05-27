import math, io_util
 
class Delsin:
    menu_options = {
        1: novo,
        2: abrir,
        3: salvar,
        4: salvar_como,
        0: sair
    }

    rede_obj = {
        specs_obj: {},
        area_trabalho: {},
        malha_horizontal: {},
        sala_telecom: {},
        misc: {}
    }

    def listar_materiais():
        print('listar')

    def calcular_materiais():

        #Área de trabalho
        rede_obj.area_trabalho['espelhos'] = rede_obj.specs_obj['pts_telecom']
        rede_obj.area_trabalho['tomadas'] = math.int(rede_obj.specs_obj['pts_rede'] + rede_obj.specs_obj['pts_cftv'] + specs_obj['pts_voz'])
        rede_obj.area_trabalho['path_cords'] = area_trabalho['tomadas']
        rede_obj.area_trabalho['etiquetas'] = area_trabalho['tomadas']*2/3

        #Malha horizontal
        rede_obj.malha_horizontal['cabos_utp'] = math.ceil((rede_obj.area_trabalho['tomadas']*rede_obj.specs_obj['tam_cabos'])/305)
        rede_obj.malha_horizontal['etiquetas'] = 2 * rede_obj.area_trabalho['tomadas']

        #Sala de telecom
        rede_obj.sala_telecom['path_panels'] = rede_obj.specs_obj['tomadas']
        rede_obj.sala_telecom['patch_panels'] = math.ceil(rede_obj.sala_telecom['patch_panels']/24)
        pc = []
        pc.append({cor: 'azul', qtd: rede_obj.specs_obj['pts_rede']})
        pc.append({cor: 'vermelho', qtd: rede_obj.specs_obj['pts_cftv']})
        pc.append({cor: 'a', qtd: rede_obj.specs_obj['pts_voz']}) 
        rede_obj.sala_telecom['patch_cables'] = pc
        rede_obj.sala_telecom['etiquetas_pc'] = 2 * rede_obj.area_trabalho['tomadas']
        rede_obj.sala_telecom['etiquetas_pp'] = 24 * rede_obj.sala_telecom['path_panels']
        sw_redes = math.ceil(rede_obj.specs_obj['pts_rede']/24)
        sw_cftv = math.ceil(rede_obj.specs_obj['pts_cftv']/24)
        sw_voz = math.ceil(rede_obj.specs_obj['pts_voz']/24)
        rede_obj.sala_telecom['organizadores_frontais'] = rede_obj.sala_telecom['path_panels']
        rede_obj.sala_telecom['organizadores_frontais'] += sw_redes + sw_voz + sw_cftv
        rede_obj.sala_telecom['racks'] = {}
        if rede_obj.specs_obj['rack_aberto']:
            rede_obj.sala_telecom['organizadores_laterais']
        
        #Miscelânea
        rede_obj.sala_telecom
        rede_obj.sala_telecom
        rede_obj.sala_telecom
        rede_obj.sala_telecom
        rede_obj.sala_telecom



    def perguntar_especificacoes_da_rede():
        print("Digite o número de pontos de telecom da sua rede:")
        specs_obj['pts_telecom'] = input()
        clear()
        print("Digite o número de pontos de rede(simples):")
        specs_obj['pts_rede'] = input()
        clear()
        print("Digite o número de pontos de CFTV IP:")
        specs_obj['pts_cftv'] = input()
        clear()
        print("Digite o número de pontos de voz sobre IP:")
        specs_obj['pts_voz'] = input()
        clear()
        print("O seu rack estará em um local fechado ou na área de trabalho?(Use 'a' ou 'f')")
        if input() == 'a': specs_obj['rack_aberto'] = True
        else: specs_obj['rack_aberto'] = False
        print("Qual será o tamanho dos cabos na malha horizontal?")
        specs_obj['tam_cabos'] = input()
        io_util.clear()

    def novo():
        print("Agora eu vou te ajudar a projetar sua rede. Para isso, preciso que você me responda algumas perguntas. Vamo Começar a festa??")
        io_util.pause()
        perguntar_especificacoes_da_rede()
        calcular_materiais()
        listar_materiais()

    def abrir():
        print('abrir')
        io_util.pause()

    def salvar():
        print('salvar')
        io_util.pause()

    def salvar_como():
        print('salvar como...')
        io_util.pause()

    def sair():
        print("Saindo...")
        io_util.pause()

    def handle_opt(opt):
        return menu_options.get(opt, lambda: print("Operação inválida."))

    def mostrar_menu():
        clear()
        print("Como posso ajudar?")
        print("1. Novo cálculo de rede")
        print("2. Abrir")
        print("3. Salvar")
        print("4. Salvar como...")
        print("0. Sair")

    def __init__():
        print("Bem vindo ao Network Calculator. Meu nome é Delsin e eu uma calculadora de materiais de rede.")
        io_util.pause()
        mostrar_menu()
        opt = -1
        while(opt != 0):
            mostrar_menu()
            opt = input()
            func = handle_opt(opt)
            func()    


Delsin()