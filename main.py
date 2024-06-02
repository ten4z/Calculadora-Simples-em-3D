import bge
scl = bge.logic.getSceneList()
cont = bge.logic.getCurrentController()
own = cont.owner
scn = own.scene
obj = scn.objects

mo_btn_on = cont.sensors['mo_btn_on']
mo_btn_off = cont.sensors['mo_btn_off']
mo_btn_0 = cont.sensors['mo_btn_0']
mo_btn_1 = cont.sensors['mo_btn_1']
mo_btn_2 = cont.sensors['mo_btn_2']
mo_btn_3 = cont.sensors['mo_btn_3']
mo_btn_4 = cont.sensors['mo_btn_4']
mo_btn_5 = cont.sensors['mo_btn_5']
mo_btn_6 = cont.sensors['mo_btn_6']
mo_btn_7 = cont.sensors['mo_btn_7']
mo_btn_8 = cont.sensors['mo_btn_8']
mo_btn_9 = cont.sensors['mo_btn_9']
tap = cont.sensors['tap']
mo_btn_pt = cont.sensors['mo_btn_pt']
mo_btn_soma = cont.sensors['mo_btn_soma']
mo_btn_diferenca = cont.sensors['mo_btn_diferenca']
mo_btn_produto = cont.sensors['mo_btn_produto']
mo_btn_igualdade = cont.sensors['mo_btn_igualdade']
mo_btn_razao = cont.sensors['mo_btn_razao']
co_ligar_desligar = cont.actuators['co_ligar_desligar']
mo_btn_mem_mais = cont.sensors['mo_btn_mem_mais']
mo_btn_mem_menos = cont.sensors['mo_btn_mem_menos']
mo_btn_mem_mrc = cont.sensors['mo_btn_mem_mrc']
mo_btn_raiz = cont.sensors['mo_btn_raiz']
mo_btn_porcentagem = cont.sensors['mo_btn_porcentagem']
m_button = cont.sensors['m_button']

class CalculadoraApp():
    desligada = own['desligada']

    def inicio(self):        
        print(self.desligada)        
        print("App iniciado")

    def atualizacao(self):
        self.ligar_calculadora()
        self.desligar_calculadora()
        self.adicicionar_ponto("")
        self.op_soma(None)
        self.op_igualdade(None, None, None, None)

        if mo_btn_on.positive:
            if m_button.positive:                
                self.desligada = False
                own['desligada'] = False                
                self.ligar_calculadora()

        if mo_btn_0.positive:
            if m_button.positive:                   
                self.adicicionar_digito("0")

        if mo_btn_1.positive:
            if m_button.positive:                   
                self.adicicionar_digito("1")

        if mo_btn_2.positive:
            if m_button.positive:                   
                self.adicicionar_digito("2")

        if mo_btn_3.positive:
            if m_button.positive:                   
                self.adicicionar_digito("3")

        if mo_btn_4.positive:
            if m_button.positive:                   
                self.adicicionar_digito("4")

        if mo_btn_5.positive:
            if m_button.positive:                   
                self.adicicionar_digito("5")

        if mo_btn_6.positive:
            if m_button.positive:                   
                self.adicicionar_digito("6")

        if mo_btn_7.positive:
            if m_button.positive:                   
                self.adicicionar_digito("7")

        if mo_btn_8.positive:
            if m_button.positive:                   
                self.adicicionar_digito("8")

        if mo_btn_9.positive:
            if m_button.positive:                   
                self.adicicionar_digito("9")

        if mo_btn_pt.positive:
            if m_button.positive:
                self.adicicionar_ponto(".")

        if mo_btn_soma.positive:
            if m_button.positive:
                self.op_soma(own['num1'])

        if mo_btn_diferenca.positive:
            if m_button.positive:
                self.op_diferenca(own['num1'])

        if mo_btn_produto.positive:
            if m_button.positive:
                own['limpar_visor'] = False
                self.op_produto(own['num1'])

        if mo_btn_razao.positive:
            if m_button.positive:
                own['limpar_visor'] = False
                self.op_razao(own['num1'])

        if mo_btn_igualdade.positive:
            if m_button.positive:
                own['limpar_visor'] = True
                self.op_igualdade(own['num1'], own['num2'], own['operacao1'],  own['operacao2'])

        if mo_btn_mem_mais.positive:
            if m_button.positive:
                own['limpar_visor'] = True
                valor = float(obj['txt_saida']['Text'])
                own['memoria'] += valor
                self.memoria_adicionar(valor)

        if mo_btn_mem_menos.positive:
            if m_button.positive:
                own['limpar_visor'] = True
                valor = float(obj['txt_saida']['Text'])
                own['memoria'] -= valor
                self.memoria_adicionar(valor)
        
        if mo_btn_mem_mrc.positive:
            if m_button.positive:
                #Memória Recuperável Constante | "Memory Recall Constant"
                own['limpar_visor'] = True                
                obj['txt_saida']['Text'] = str(round(own['memoria'], 5 ))[:15]

        if mo_btn_raiz.positive:
            if m_button.positive:                
                try:
                    numero = float(obj['txt_saida']['Text'])
                    if numero >= 0:
                        own['limpar_visor'] = True                        
                        saida = str(round(numero**0.5, 5 ))[:15]        
                        obj['txt_saida']['Text'] = saida
                except:
                    print("Impossível fazer este cálculo")
        if mo_btn_porcentagem.positive:
            if m_button.positive:
                try:
                    own['operacao2'] = "porcentagem"
                    own['num2'] = round(float(obj['txt_saida']['Text'], 5 ))
                    print("v1 = ", own['num1'])
                    print("v2 = ", own['num2'])
                except:
                    print("Impossivel fazer este cálculo")
                
    def adicicionar_ponto(self, ponto):
        if self.desligada == False:
            display = obj['txt_saida']['Text']            
            if len(display) < 8:                                         
                for txt in display:
                    if "." not in display:
                        obj['txt_saida']['Text'] += ponto
                        break

    def op_igualdade(self, v1, v2, op1, op2):
        try:            
            if v1 is not None: 
                if op1 == "soma":
                    if op2 != "porcentagem":
                        own['num2'] = float(obj['txt_saida']['Text'])                        
                        valor = float(own['num1'] + own['num2'])
                        saida = str(round(valor, 5 ))[:15]        
                        obj['txt_saida']['Text'] = saida
                        own['num1'] = 0
                        own['num2'] = 0
                    elif op2 != "" or op2 == "porcentagem":            
                        own['num2'] = float(obj['txt_saida']['Text'])     
                        valor = float(own['num1'] + (own['num1']*own['num2'])/100)                    
                        saida = str(round(valor, 5 ))[:15]               
                        obj['txt_saida']['Text'] = saida
                        own['num1'] = 0
                        own['num2'] = 0
                        own['operacao1'] = ""
                        own['operacao2'] = ""
                elif op1 == "diferenca": 
                    if op2 != "porcentagem":           
                        own['num2'] = float(obj['txt_saida']['Text'])     
                        valor = float(own['num1'] - own['num2'])                    
                        saida = str(round(valor, 5 ))[:15]               
                        obj['txt_saida']['Text'] = saida
                        own['num2'] = 0
                        own['num1'] = 0
                    elif op2 != "" or op2 == "porcentagem":
                        own['num2'] = float(obj['txt_saida']['Text'])     
                        valor = float(own['num1'] - (own['num1']*own['num2'])/100)                    
                        saida = str(round(valor, 5 ))[:15]               
                        obj['txt_saida']['Text'] = saida
                        own['num2'] = 0
                        own['num1'] = 0
                        own['operacao1'] = ""
                        own['operacao2'] = ""
                elif op1 == "produto":  
                    if op2 != "porcentagem":          
                        own['num2'] = float(obj['txt_saida']['Text'])     
                        valor = float(own['num1'] * own['num2'])                    
                        saida = str(round(valor, 5 ))[:15]                
                        obj['txt_saida']['Text'] = saida
                        own['num2'] = 0
                        own['num1'] = 0
                        print("result")
                    elif op2 != "" or op2 == "porcentagem":
                        own['num2'] = float(obj['txt_saida']['Text'])     
                        valor = float((own['num1']*own['num2'])/100)                    
                        saida = str(round(valor, 5 ))[:15]                
                        obj['txt_saida']['Text'] = saida
                        own['num2'] = 0
                        own['num1'] = 0
                        own['operacao1'] = ""
                        own['operacao2'] = ""
                elif op1 == "razao":
                    own['num2'] = float(obj['txt_saida']['Text'])        
                    if op2 != "porcentagem":                             
                        if own['num2'] != 0:                            
                            valor = own['num1'] / own['num2']
                            saida = str(round(valor, 5 ))[:15]               
                            obj['txt_saida']['Text'] = saida
                            own['num2'] = 0
                            own['num1'] = 0
                        else:
                            own['num1'] = 0
                            own['num2'] = 0
                            obj['txt_saida']['Text'] = "Erro"                            
                            print("Impossivel dividir por Zero.")
                    elif op2 != "" or op2 == "porcentagem":                        
                        if own['num2'] != 0:                                                        
                            valor = float(own['num1'] / (own['num1']*own['num2']/100))
                            saida = str(round(valor, 5 ))[:15]               
                            obj['txt_saida']['Text'] = saida
                            own['num2'] = 0
                            own['num1'] = 0
                            own['operacao1'] = ""
                            own['operacao2'] = ""
                        else:
                            own['num1'] = 0
                            own['num2'] = 0
                            own['operacao1'] = ""
                            own['operacao2'] = ""
                            obj['txt_saida']['Text'] = "Erro"                            
                            print("Impossivel dividir por Zero.")
        except:
            print("Operação inválida")

    def op_soma(self, v1):
        try:
            if v1 is not None:
                own['operacao1'] = "soma"
                own['num1'] = float(obj['txt_saida']['Text'])                                   
                obj['txt_saida']['Text'] = ""
        except:
            print("Impossível fazer esta operacao")
    def op_diferenca(self, v1):
        try:
            if v1 is not None:
                own['operacao1'] = "diferenca"
                own['num1'] = float(obj['txt_saida']['Text'])                                       
                obj['txt_saida']['Text'] = ""
        except:
            print("Impossível fazer esta operacao")

    def op_produto(self, v1):
        try:
            if v1 is not None:
                own['operacao1'] = "produto"
                own['num1'] = float(obj['txt_saida']['Text'])                                       
                obj['txt_saida']['Text'] = ""
        except:
            print("Impossível fazer esta operacao")

    def op_razao(self, v1):        
        try:
            if v1 is not None:
                own['operacao1'] = "razao"
                own['num1'] = float(obj['txt_saida']['Text'])                                                     
                obj['txt_saida']['Text'] = ""
        except:
            print("Impossível fazer esta operacao")

    def memoria_adicionar(self, v1):
        if tap.positive:
            own['memoria'] += v1            

    def memoria_subtrair(self, v1):
        if tap.positive:
            own['memoria'] -= v1
            
    def adicicionar_digito(self, digito):
        if self.desligada == False:
            if own['limpar_visor'] == False:
                if len(obj['txt_saida']['Text']) < 9:                    
                    if digito == "0":
                        if obj['txt_saida']['Text'] == "0":          
                            obj['txt_saida']['Text'] = "0"
                        else:
                            obj['txt_saida']['Text'] += "0"
                    else:
                        if (obj['txt_saida']['Text'] == "" or obj['txt_saida']['Text'] == "0"):          
                            obj['txt_saida']['Text'] = digito
                            own['limpar_visor'] = False
                        else:
                            obj['txt_saida']['Text'] += digito
                            own['limpar_visor'] = False
            elif own['limpar_visor'] == True:
                if own['num1'] == own['num2'] == 0:          
                    obj['txt_saida']['Text'] = digito
                    own['limpar_visor'] = False
                else:
                    obj['txt_saida']['Text'] += digito
                    own['limpar_visor'] = False
    
    def ligar_calculadora(self):
        self.desligada = own['desligada']
        if self.desligada == False:  
            if obj['txt_saida']['Text'] == "":          
                if own['num1'] == own['num2'] == 0:            
                    obj['txt_saida']['Text'] = "0"        
        else:
            own['num1'] = 0
            own['num2'] = 0
            own['memoria'] = 0
            own['resultado'] = 0
            own['operacao1'] = ""
            own['operacao2'] = ""
            obj['txt_saida']['Text'] = ""
            
    def desligar_calculadora(self):        
        if mo_btn_off.positive:
            if m_button.positive:
                self.desligada = True
                own['desligada'] = True
                self.ligar_calculadora()
                
def iniciar():
    CalculadoraApp().inicio()
    
def atualizar():
    CalculadoraApp().atualizacao()