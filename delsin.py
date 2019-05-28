import math, io_util
 
class Delsin:
    rede_obj = {
        'specs_obj': {},
        'area_trabalho': {},
        'malha_horizontal': {},
        'sala_telecom': {},
        'misc': {}
    }


    def calcular_materiais(self):

        print("calculando...")

        area_trabalho = self.rede_obj['area_trabalho']
        specs_obj = self.rede_obj['specs_obj']
        malha_horizontal = self.rede_obj['malha_horizontal']
        sala_telecom = self.rede_obj['sala_telecom']

        area_trabalho['espelhos'] = specs_obj['pts_telecom'] + specs_obj['pts_rede']/2
        area_trabalho['tomadas'] = int(specs_obj['pts_rede'] + (2 * specs_obj['pts_telecom']) + specs_obj['pts_cftv'] + specs_obj['pts_voz'])
        area_trabalho['patch_cords'] = area_trabalho['tomadas']
        area_trabalho['etiquetas'] = area_trabalho['espelhos'] * 3

        malha_horizontal['cabos_utp'] = math.ceil((area_trabalho['tomadas'] * specs_obj['tam_cabos'])/305)
        malha_horizontal['etiquetas'] = 2 * area_trabalho['tomadas']

        sala_telecom['patch_panels'] = math.ceil(area_trabalho['tomadas']/24)
        pcable = []
        pcable.append({'cor': 'azul', 'qtd': specs_obj['pts_rede'] + (2 * specs_obj['pts_telecom'])})
        pcable.append({'cor': 'vermelho', 'qtd': specs_obj['pts_cftv']})
        pcable.append({'cor': 'amarelo', 'qtd': specs_obj['pts_voz']}) 
        sala_telecom['patch_cables'] = pcable
        sala_telecom['etiquetas_pcable'] = 2 * area_trabalho['tomadas']
        sala_telecom['etiquetas_ppanel'] = 24 * sala_telecom['patch_panels']
        sw_redes = math.ceil(specs_obj['pts_rede'] + ((2 * specs_obj['pts_telecom'])/24))
        sw_cftv = math.ceil(specs_obj['pts_cftv']/24)
        sw_voz = math.ceil(specs_obj['pts_voz']/24)
        sala_telecom['switches'] = sw_redes + sw_voz + sw_cftv
        sala_telecom['organizadores_frontais'] = sala_telecom['patch_panels'] + sala_telecom['switches']
        tamanho_total_rack = sala_telecom['switches'] + sala_telecom['patch_panels'] + sala_telecom['organizadores_frontais'] + 4
        
        print(tamanho_total_rack)

        if(not specs_obj['rack_aberto']):
            tamanho_total_rack += 2
        qtd_rack = 1
        if(tamanho_total_rack <=12):
            tamanho_rack = math.ceil(tamanho_total_rack/2) * 2
        elif(tamanho_total_rack>12 and tamanho_total_rack <= 48):
            tamanho_rack = math.ceil(tamanho_total_rack/4) * 4
        else:
            tamanho_rack = tamanho_total_rack
            while(tamanho_rack > 48):
                qtd_rack += 1
                tamanho_rack = tamanho_rack / qtd_rack
            print(qtd_rack)
            print(tamanho_rack)
            tamanho_rack = tamanho_total_rack / qtd_rack
            tamanho_rack = math.ceil(tamanho_total_rack/4) * 4
        sala_telecom['rack'] = {}
        sala_telecom['rack']['tamanho'] = tamanho_rack
        sala_telecom['rack']['qtd'] = qtd_rack

        print(tamanho_rack)
                
        #Miscelânea

    
    def listar_materiais(self):

        print("Listando materiais...")


    def perguntar_especificacoes_da_rede(self):

        specs_obj = self.rede_obj['specs_obj']
        
        print("Digite o número de pontos de telecom da sua rede:")
        specs_obj['pts_telecom'] = int(input())
        io_util.clear()
        print("Digite o número de pontos de rede(simples):")
        specs_obj['pts_rede'] = int(input())
        io_util.clear()
        print("Digite o número de pontos de CFTV IP:")
        specs_obj['pts_cftv'] = int(input())
        io_util.clear()
        print("Digite o número de pontos de voz sobre IP:")
        specs_obj['pts_voz'] = int(input())
        io_util.clear()
        print("Qual será o tamanho dos cabos na malha horizontal?")
        opc = int(input())
        while(int(opc) < 1):
            print("O tamanho dos seus cabos não pode ser menor que 1, por favor digite um tamanho válido.")
            opc = int(input())
        specs_obj['tam_cabos'] = opc
        print("O seu rack estará em um local fechado ou na área de trabalho? (Use 'a' ou 'f')")
        if input() == 'a':
            specs_obj['rack_aberto'] = True
        else:
            specs_obj['rack_aberto'] = False

    def novo(self):
        print("Agora eu vou te ajudar a projetar sua rede. Para isso, preciso que você me responda algumas perguntas. Vamo começar a festa?")
        io_util.pause()
        self.perguntar_especificacoes_da_rede()
        self.calcular_materiais()
        self.listar_materiais()

    def abrir(self):
        self.listar_materiais()
        io_util.pause()

    def salvar(self):
        print('salvar')
        io_util.pause()

    def salvar_como(self):
        print('salvar como...')
        io_util.pause()

    def sair(self):
        print("Saindo...")
        io_util.pause()

    def mostrar_menu(self):
        io_util.clear()
        print("Como posso ajudar?")
        print("1. Novo cálculo de rede")
        print("2. Abrir")
        print("3. Salvar")
        print("4. Salvar como...")
        print("0. Sair")

    def handle_opt(self, opt):
        return self.menu_options.get(opt, lambda a: print("Operação inválida."))

    menu_options = {
        1: novo,
        2: abrir,
        3: salvar,
        4: salvar_como,
        5: calcular_materiais,
        0: sair
    }

    def __init__(self):
        print("Bem vindo ao Network Calculator. Meu nome é Delsin e eu sou uma calculadora de materiais de rede.")
        io_util.pause()
        opt = -1
        while(int(opt) != 0):
            self.mostrar_menu()
            opt = input()
            func = self.handle_opt(int(opt))
            func(self) 


Delsin()