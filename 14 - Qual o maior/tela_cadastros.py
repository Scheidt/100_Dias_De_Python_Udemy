

class TelaCadastros():
    def __init__(self) -> None:
        pass

    def listar_opcoes(self):
        string = "--------- OPÇÕES: ---------\n"
        string = string + "1: Listar as opções já inscritas \n"
        string = string + "2: Listar as opções já inscritas (incluindo número de pesquisas) \n"
        string = string + "3: Incluir uma nova opção \n"
        string = string + "4: Excluir uma das opções já inscritas \n"
        string = string + "5: Salvar \n"
        string = string + "6: Carregar \n"
        string = string + "7: Ativar/desativar rejogabilidade \n"
        string = string + "8: Jogar \n"
        string = string + "0: Sair \n"
        string = string + "INSIRA O NÚMERO DA OPÇÃO DESEJADA OU 0 PARA CANCELAR:\n"
        print (string)
        entrada = self.testar_no_intervalo((0, 1, 2, 3, 4, 5, 6, 7, 8))
        return entrada
    
    def pega_dados_cadastro(self):
        self.mostra_mensagem("(Você sempre pode inserir '0' para cancelar a inscrição)")
        nome = input("Entre o termo (nome) do cadastro: ")
        if nome == '0':
            return
        descricao = input(f"Entre a descrição de {nome}: ")
        if descricao == '0':
            return
        pais = input(f"{nome} é um(a) {descricao} de qual país? ")
        if descricao == '0':
            return
        pesquisas = input(f"Quantas pesquisas {nome}, {descricao} de {pais} possui? ")
        if pesquisas == '0':
            return
        pesquisas = self.testar_inteiro(pesquisas)
        if pesquisas is None:
            return
        return {'nome': nome,
                'descricao': descricao,
                'pais': pais,
                'pesquisas': pesquisas}
    
    def mostra_cadastros(self, buffer: list, pesquisasTbm = False):
        bufferString = ''
        if pesquisasTbm:
            for numcadastro in range(len(buffer)):
                bufferString = bufferString + f"CADASTRO {numcadastro + 1}\n"
                bufferString = bufferString + f"NOME {buffer[numcadastro]['nome']}\n"
                bufferString = bufferString + f"DESCRIÇÃO: {buffer[numcadastro]['descricao']}\n"
                bufferString = bufferString + f"PAÍS: {buffer[numcadastro]['pais']}\n"
                bufferString = bufferString + f"PESQUISAS: {buffer[numcadastro]['pesquisas']}\n \n"
            print (bufferString)
        else:
            for numcadastro in range(len(buffer)):
                bufferString = bufferString + f"CADASTRO {numcadastro + 1}\n"
                bufferString = bufferString + f"DESCRIÇÃO: {buffer[numcadastro]['nome']} é um(a)/o(a) {buffer[numcadastro]['descricao']}, localizado(a)/nascido(a) no {buffer[numcadastro]['pais']}\n \n"
            print (bufferString)

    def pega_nome(self):
        entrada = input("Insira o nome do cadastro que deseja alterar: ")
        return entrada
  
    def jogar(self, buffer: list):
        melhor = None
        bufferString = '\n'*5
        if buffer[0]['pesquisas'] > buffer[1]['pesquisas']:
            melhor = 1
        else:
            melhor = 2
        for numcadastro in range(len(buffer)):
            bufferString = bufferString + f"CADASTRO {numcadastro + 1}\n"
            bufferString = bufferString + f"DESCRIÇÃO: {buffer[numcadastro]['nome']} é um(a)/o(a) {buffer[numcadastro]['descricao']}, localizado(a)/nascido(a) no {buffer[numcadastro]['pais']}\n \n"  
        print (bufferString)
        escolha = input("INSIRA O NÚMERO DO CADASTRO QUE VOCÊ ACREDITA TER MAIS PESQUISAS: ")
        escolha = self.testar_inteiro(escolha) # Cancelar é None
        if escolha is None: # Se o usuario decide retornar colocando zero
            return None
        if escolha == melhor:
            self.mostra_mensagem(f"{buffer[melhor-1]['nome']}, o(a) {buffer[melhor-1]['descricao']} de {buffer[melhor-1]['pais']} possui {buffer[melhor-1]['pesquisas']} pesquisas.")
            return True
        else:
            return False
        
    def mostra_mensagem(self, arg: str):
        print(arg)

    def testar_inteiro(self, talvezint):
        while True:
            try:
                int(talvezint)
                if float(int(talvezint)) != float(talvezint):
                    raise ValueError
                if talvezint in (0, '0'):
                    return None
            except ValueError:
                talvezint = input("O valor inserido deve ser um valor numérico inteiro e não pode possuir letras. Por favor, insira novamente:")
            else:
                return int(talvezint)

    def testar_no_intervalo(self, opcoes: tuple):
        entrada = input("Entre a opção desejada: ")
        while True:
            entrada = self.testar_inteiro(entrada)
            if entrada in opcoes or entrada is None:
                return entrada
            else:
                self.mostra_mensagem("A opção escolhida é inválida.")
                entrada = input("Insira uma opção válida: ")

    def verificar_rejogabilidade(self):
        saida = input("Você gostaria de continuar jogando mesmo se perder? [Digite 's' ou 'n'] ").lower()
        while not saida in ('s', 'n'):
            saida = input("As únicas opções são 's' ou 'n'. Por favor, tente novamente. ")
        if saida == 's':
            return True
        else:
            return False
