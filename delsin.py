import math, io_util
 
class Delsin:
    rede_obj = {
        'specs_obj': {},
        'area_trabalho': {},
        'malha_horizontal': {},
        'sala_telecom': {},
        'misc': {}
    }

    def listar_materiais(self):
        print('listar')

    def calcular_materiais(self):

        #Área de trabalho
        self.rede_obj['area_trabalho']['espelhos'] = self.rede_obj['specs_obj']['pts_telecom']
        self.rede_obj['area_trabalho']['tomadas'] = int(self.rede_obj['specs_obj']['pts_rede'] + self.rede_obj['specs_obj']['pts_cftv'] + self.rede_obj['specs_obj']['pts_voz'])
        self.rede_obj['area_trabalho']['patch_cords'] = self.rede_obj['area_trabalho']['tomadas']
        self.rede_obj['area_trabalho']['etiquetas'] = self.rede_obj['area_trabalho']['tomadas']*2/3

        #Malha horizontal
        self.rede_obj['malha_horizontal']['cabos_utp'] = math.ceil((self.rede_obj['area_trabalho']['tomadas']*self.rede_obj['specs_obj']['tam_cabos'])/305)
        self.rede_obj['malha_horizontal']['etiquetas'] = 2 * self.rede_obj['area_trabalho']['tomadas']

        #Sala de telecom
        self.rede_obj['sala_telecom']['patch_panels'] = self.rede_obj['area_trabalho']['tomadas']
        self.rede_obj['sala_telecom']['patch_panels'] = math.ceil(self.rede_obj['sala_telecom']['patch_panels']/24)
        pc = []
        pc.append({'cor': 'azul', 'qtd': self.rede_obj['specs_obj']['pts_rede']})
        pc.append({'cor': 'vermelho', 'qtd': self.rede_obj['specs_obj']['pts_cftv']})
        pc.append({'cor': 'a', 'qtd': self.rede_obj['specs_obj']['pts_voz']}) 
        self.rede_obj['sala_telecom']['patch_cables'] = pc
        self.rede_obj['sala_telecom']['etiquetas_pc'] = 2 * self.rede_obj['area_trabalho']['tomadas']
        self.rede_obj['sala_telecom']['etiquetas_pp'] = 24 * self.rede_obj['sala_telecom']['patch_panels']
        sw_redes = math.ceil(self.rede_obj['specs_obj']['pts_rede']/24)
        sw_cftv = math.ceil(self.rede_obj['specs_obj']['pts_cftv']/24)
        sw_voz = math.ceil(self.rede_obj['specs_obj']['pts_voz']/24)
        self.rede_obj['sala_telecom']['organizadores_frontais'] = self.rede_obj['sala_telecom']['patch_panels']
        self.rede_obj['sala_telecom']['organizadores_frontais'] += sw_redes + sw_voz + sw_cftv
        self.rede_obj['sala_telecom']['racks'] = {}
        
        
        #Miscelânea


    def perguntar_especificacoes_da_rede(self):
        print("Digite o número de pontos de telecom da sua rede:")
        self.rede_obj['specs_obj']['pts_telecom'] = int(input())
        io_util.clear()
        print("Digite o número de pontos de rede(simples):")
        self.rede_obj['specs_obj']['pts_rede'] = int(input())
        io_util.clear()
        print("Digite o número de pontos de CFTV IP:")
        self.rede_obj['specs_obj']['pts_cftv'] = int(input())
        io_util.clear()
        print("Digite o número de pontos de voz sobre IP:")
        self.rede_obj['specs_obj']['pts_voz'] = int(input())
        io_util.clear()
        print("O seu rack estará em um local fechado ou na área de trabalho?(Use 'a' ou 'f')")
        if input() == 'a': self.rede_obj['specs_obj']['rack_aberto'] = True
        else: self.rede_obj['specs_obj']['rack_aberto'] = False
        print("Qual será o tamanho dos cabos na malha horizontal?")
        self.rede_obj['specs_obj']['tam_cabos'] = int(input())
        io_util.clear()

    def novo(self):
        print("Agora eu vou te ajudar a projetar sua rede. Para isso, preciso que você me responda algumas perguntas. Vamo Começar a festa??")
        io_util.pause()
        self.perguntar_especificacoes_da_rede()
        self.calcular_materiais()
        self.listar_materiais()

    def abrir(self):
        print('abrir')
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