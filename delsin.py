import math, io_util
import JSONFileHandler as jfh
 
class Delsin:
    
    rede_obj = {
        'specs_obj': {},
        'area_trabalho': {},
        'malha_horizontal': {},
        'sala_telecom': {},
        'misc': {}
    }

    curr_filename = None

    area_trabalho = {}
    specs_obj = {}
    malha_horizontal = {}
    sala_telecom = {}
    misc = {}
         

    def perguntar_especificacoes_da_rede(self):

        self.area_trabalho = self.rede_obj['area_trabalho']
        self.specs_obj = self.rede_obj['specs_obj']
        self.malha_horizontal = self.rede_obj['malha_horizontal']
        self.sala_telecom = self.rede_obj['sala_telecom']
        
        print("Digite o número de pontos de telecom da sua rede:")
        self.specs_obj['pts_telecom'] = int(input())
        io_util.clear()
        print("Digite o número de pontos de rede(simples):")
        self.specs_obj['pts_rede'] = int(input())
        io_util.clear()
        print("Digite o número de pontos de CFTV IP:")
        self.specs_obj['pts_cftv'] = int(input())
        io_util.clear()
        print("Digite o número de pontos de voz sobre IP:")
        self.specs_obj['pts_voz'] = int(input())
        io_util.clear()
        print("Qual será o tamanho dos cabos na malha horizontal?")
        opc = int(input())
        io_util.clear()
        while(int(opc) < 1):
            print("O tamanho dos seus cabos não pode ser menor que 1, por favor digite um tamanho válido.")
            opc = int(input())
        self.specs_obj['tam_cabos'] = opc
        print("O seu rack estará em um local fechado ou na área de trabalho? (Use 'f' ou 'a')")
        if input() == 'a':
            self.specs_obj['rack_aberto'] = False
        else:
            self.specs_obj['rack_aberto'] = True
        io_util.clear()


    def calcular_materiais(self):

        print("Calculando...")

        self.area_trabalho['espelhos_duplos'] = self.specs_obj['pts_telecom']
        self.area_trabalho['espelhos_simples'] = self.specs_obj['pts_rede']
        self.area_trabalho['tomadas'] = int(self.specs_obj['pts_rede'] + (2 * self.specs_obj['pts_telecom']))
        self.area_trabalho['patch_cords'] = self.area_trabalho['tomadas']
        self.area_trabalho['etiquetas'] = self.area_trabalho['tomadas'] + self.area_trabalho['espelhos_simples'] + self.area_trabalho['espelhos_duplos']

        self.malha_horizontal['cabos_utp'] = math.ceil((self.area_trabalho['tomadas'] * self.specs_obj['tam_cabos'])/305)
        self.malha_horizontal['etiquetas'] = 2 * self.area_trabalho['tomadas']

        self.sala_telecom['switches'] = math.ceil((self.specs_obj['pts_rede'] + (2 * self.specs_obj['pts_telecom']))/24)
        self.sala_telecom['patch_panels'] = self.sala_telecom['switches']
        pcable = []
        pcable.append({'cor': 'azul', 'qtd': (self.specs_obj['pts_rede'] + (2 * self.specs_obj['pts_telecom']) - self.specs_obj['pts_cftv'] - self.specs_obj['pts_voz'])})
        pcable.append({'cor': 'vermelho', 'qtd': self.specs_obj['pts_cftv']})
        pcable.append({'cor': 'amarelo', 'qtd': self.specs_obj['pts_voz']}) 
        self.sala_telecom['patch_cables'] = pcable
        self.sala_telecom['etiquetas_pcable'] = 2 * self.area_trabalho['tomadas']
        self.sala_telecom['etiquetas_ppanel'] = 24 * (self.sala_telecom['patch_panels'])
        self.sala_telecom['organizadores_frontais'] = self.sala_telecom['patch_panels'] + self.sala_telecom['switches']
        tamanho_total_rack = int(self.sala_telecom['switches'] + self.sala_telecom['patch_panels'] + self.sala_telecom['organizadores_frontais'])
        tamanho_unit_rack = tamanho_total_rack 
        qtd_rack = 1
        if(self.specs_obj['rack_aberto']):
            qtd_exaust = 0
            exaustor = 0
        else:
            qtd_exaust = 1
            exaustor = 2
        
        while(((tamanho_unit_rack + exaustor + 4) * 3/2) > 48):
            qtd_rack += 1
            print("while")
            if(not self.specs_obj['rack_aberto']):
                qtd_exaust = qtd_rack
            tamanho_unit_rack = tamanho_total_rack / qtd_rack
        tamanho_unit_rack = (tamanho_unit_rack + exaustor + 4) * 3/2
        if(tamanho_unit_rack <= 12):
            tamanho_unit_rack = math.ceil((tamanho_total_rack+4)/2) * 2
        elif(tamanho_unit_rack > 12 and tamanho_unit_rack <= 48):
            tamanho_unit_rack = math.ceil((tamanho_total_rack+4)/4) * 4
        else:
            tamanho_unit_rack = math.ceil(tamanho_unit_rack/4) * 4
        self.sala_telecom['rack'] = {}
        self.sala_telecom['rack']['tamanho'] = tamanho_unit_rack
        self.sala_telecom['rack']['qtd'] = qtd_rack        
                
        self.misc['porca_gaiola'] = 4 * self.sala_telecom['rack']['tamanho'] * self.sala_telecom['rack']['qtd']
        self.misc['abrc_plastica'] = self.sala_telecom['rack']['qtd']
        self.misc['abrc_velcro'] = 3 * self.sala_telecom['rack']['qtd']
        self.misc['filtro_linha'] = self.sala_telecom['switches'] + 2 * self.sala_telecom['rack']['qtd']
        self.misc['kit_rodizio'] = self.sala_telecom['rack']['qtd']

        io_util.pause()

    
    def listar_materiais(self):

        io_util.clear()

        print("Listando materiais...")

        print("Área de trabalho:")
        print(" - Tomadas fêmea RJ-45 (cat 6): ", self.area_trabalho['tomadas'])
        print("\tTomadas fêmea de dados: ", ((2*self.specs_obj['pts_telecom']) + self.specs_obj['pts_rede']) - self.specs_obj['pts_cftv'] - self.specs_obj['pts_voz'])
        print("\tTomadas fêmea de CFTV: ", self.specs_obj['pts_cftv'])
        print("\tTomadas fêmea de voz sobre IP: ", self.specs_obj['pts_voz'])
        print(" - Patch Cord (cat 6, 3 metros por cabo): ", self.area_trabalho['patch_cords'])
        print(" - Espelhos simples: ", self.area_trabalho['espelhos_simples'])
        print(" - Espelhos duplos: ", self.area_trabalho['espelhos_duplos'])
        print(" - Etiquetas: ", self.area_trabalho['etiquetas'])

        print("Malha horizontal:")
        print(" - Cabos UTP (caixa de 305m): ", self.malha_horizontal['cabos_utp'])
        print(" - Etiquetas: ", self.malha_horizontal['etiquetas'])

        print("Sala de Telecomunicações:")
        print(" - Patch Panels: ", self.sala_telecom['patch_panels'])
        print("\tEtiquetas: ", self.sala_telecom['etiquetas_ppanel'])
        print(" - Patch Cables:")
        print("\tEtiquetas: ", self.sala_telecom['etiquetas_pcable'])
        print("\tDados: ", self.sala_telecom['patch_cables'][0]['qtd'], " - cor: ", self.sala_telecom['patch_cables'][0]['cor'])
        print("\tCFTV: ", self.sala_telecom['patch_cables'][1]['qtd'], " - cor: ", self.sala_telecom['patch_cables'][1]['cor'])
        print("\tVoz: ", self.sala_telecom['patch_cables'][2]['qtd'], " - cor: ", self.sala_telecom['patch_cables'][2]['cor'])
        print(" - Organizadores frontais: ", self.sala_telecom['organizadores_frontais'])
        if(self.specs_obj['rack_aberto']):
            print(" - Organizadores laterais: ", (2 * self.sala_telecom['rack']['tamanho'] * self.sala_telecom['rack']['qtd']))
        print(" - Rack: ")
        print("\tTamanho: ", self.sala_telecom['rack']['tamanho'], "U")
        print("\tQuantidade: ", self.sala_telecom['rack']['qtd'])

        print("Miscelânea:")
        if(not self.specs_obj['rack_aberto']):
            print(" - Kit rodízio: ", self.misc['kit_rodizio'])
        print(" - Porca gaiola: ", self.misc['porca_gaiola'])
        print(" - Abraçadeiras plásticas (pacote de 100 unidades): ", self.misc['abrc_plastica'])
        print(" - Abraçadeiras de velcro (em metros): ", self.misc['abrc_velcro'])
        print(" - Filtro de linha: ", self.misc['filtro_linha'])

        
        io_util.pause()
   

    def novo(self):
        print("Agora eu vou te ajudar a projetar sua rede. Para isso, preciso que você me responda algumas perguntas. Vamo começar a festa?")
        io_util.pause()
        self.perguntar_especificacoes_da_rede()
        self.calcular_materiais()
        self.listar_materiais()

    def abrir(self):
        print('Digite o nome do arquivo que deseja abrir:')
        self.curr_filename = input()
        self.rede_obj = jfh.read_json(self.curr_filename)
        self.listar_materiais()
        io_util.pause()

    def salvar(self):
        if self.curr_filename != None:
            jfh.save_json(self.curr_filename, self.rede_obj)
        else:
            self.salvar_como()

    def salvar_como(self):
        print("Digite o nome que deseja salvar seu arquivo:")
        self.curr_filename = input()
        jfh.save_json(self.curr_filename, self.rede_obj)

    def sair(self):
        print("Saindo...")
        io_util.pause()

    def mostrar_menu(self):
        io_util.clear()
        print("Como posso ajudar?")
        print("1. Novo cálculo de rede")
        print("2. Listar materiais")
        print("3. Abrir")
        print("4. Salvar")
        print("5. Salvar como...")
        print("0. Sair")

    def handle_opt(self, opt):
        return self.menu_options.get(opt, lambda a: print("Operação inválida."))

    menu_options = {
        1: novo,
        2: listar_materiais,
        3: abrir,
        4: salvar,
        5: salvar_como,
        0: sair
    }

    def __init__(self):
        print("Bem vindo ao Network Calculator. Meu nome é Delsin e eu sou uma calculadora de materiais de rede.")
        io_util.pause()
        opt = -1
        while(int(opt) != 0):
            self.mostrar_menu()
            opt = input()
            io_util.clear()
            func = self.handle_opt(int(opt))
            func(self) 


Delsin()