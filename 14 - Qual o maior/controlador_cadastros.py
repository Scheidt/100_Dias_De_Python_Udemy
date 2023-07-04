from cadastro import Cadastro
from tela_cadastros import TelaCadastros
from random import randint
import json

class Controlador_Cadastros():
    def __init__(self) -> None:
        self.__cadastros = []
        self.__tela = TelaCadastros()
        if self.__tela.verificar_rejogabilidade():
            self.__replay = True
        else:
            self.__replay = False

    def menu(self):
        switch = {1: self.listar_cadastros,
                  2: self.listar_cadastros_com_pesquisas,
                  3: self.incluir_opcao,
                  4: self.excluir_produto,
                  5: self.salvar,
                  6: self.carregar,
                  7: self.mudar_rejogabilidade,
                  8: self.jogar}
        while True:
            escolha = self.__tela.listar_opcoes()
            if escolha is None:
                break
            if escolha == 8: # Se a pessoa acertar, ela retorna um True ao main, o que adiciona um ponto ou
                             # um false que indica que ela errou
                return switch[escolha]()
            else:
                switch[escolha]()

    def listar_cadastros(self):
        if len(self.__cadastros) == 0:
            self.__tela.mostra_mensagem("Nenhuma opção foi registrada ainda, por favor, registre uma opção antes de utilizar este comando.")
        else:
            buffer = []
            for cadastro in self.__cadastros:
                buffer.append({'nome': cadastro.nome, 'descricao': cadastro.descricao, 'pais': cadastro.pais})
            self.__tela.mostra_cadastros(buffer)

    def listar_cadastros_com_pesquisas(self):
        if len(self.__cadastros) == 0:
            self.__tela.mostra_mensagem("Nenhuma opção foi registrada ainda, por favor, registre uma opção antes de utilizar este comando. \n")
        else:
            buffer = []
            for cadastro in self.__cadastros:
                buffer.append({'nome': cadastro.nome, 'descricao': cadastro.descricao, 'pais': cadastro.pais, 'pesquisas': cadastro.pesquisas})
            self.__tela.mostra_cadastros(buffer, pesquisasTbm = True)

    def incluir_opcao(self):
        dados = self.__tela.pega_dados_cadastro()
        if dados is None: # Quando a entrada é cancelada na tela
            return None
        else:
            cadastro = self.pega_opcao_por_nome(nome = dados['nome'])
            try:
                if cadastro is None:  #cód de saída
                    return None
                elif isinstance(cadastro, Cadastro):
                    self.__tela.mostra_mensagem("Já foi inscrito uma opção com este nome! Cadastro não feito.")
                else:
                    self.__cadastros.append(Cadastro(dados['nome'],
                                                dados['descricao'],
                                                dados['pais'],
                                                dados['pesquisas']))
            except:
                self.__tela.mostra_mensagem("Não é possível alcançar esse código, eu acho")
                pass
        
    def excluir_produto(self):
        while True:
            opcao = self.pega_opcao_por_nome()
            if opcao is None:
                break
            try:
                self.__cadastros.remove(opcao)
            except:
                self.__tela.mostra_mensagem("Não foi encontrado cadastro com esse nome. Tente novamente, por favor")
            else:
                self.__tela.mostra_mensagem("Cadastro removido com sucesso")
                break

    def pega_opcao_por_nome(self, nome = None): # -> None para cód de retorno, False se n achar e Objeto se achar
        if nome is None:
            nome = self.__tela.pega_nome()
        if nome == '0':
            return None
        for opcao in self.__cadastros:
            if opcao.nome == nome:
                return opcao
        else:
            return False

    def salvar(self):
        elementos_jsonificados = []
        for elemento in self.__cadastros:
            elementos_jsonificados.append(elemento.jsonificado())
        with open('lista_de_cadastros.json', 'w') as file:
            json.dump(elementos_jsonificados, file, indent=4)
        self.__tela.mostra_mensagem("Salvo com sucesso!")

    def carregar(self):
        self.__cadastros = []
        with open('lista_de_cadastros.json', 'r') as file:
            cadastros_jsonificados = json.load(file)
            for cadastro in cadastros_jsonificados:
                self.__cadastros.append(Cadastro(cadastro['nome'],
                                                 cadastro['descricao'],
                                                 cadastro['pais'],
                                                 cadastro['pesquisas']))
        self.__tela.mostra_mensagem("Carregado com sucesso!")

    def jogar(self):
        if len(self.__cadastros) < 2:
            self.__tela.mostra_mensagem(f"Utilizar esta função requer que ao menos dois cadastros sejam feitos. "\
                                         f"Por favor, registre mais {2-len(self.__cadastros)} opções")
        else:
            buffer = []
            rand1 = randint(0, len(self.__cadastros)-1) # Cria um número aleatório
            rand2 = randint(0, len(self.__cadastros)-1) # Cria outro número aleatório
            while rand1 == rand2: # Garante que ambos os números aleatórios são diferentes
                rand2 = randint(0, len(self.__cadastros))
            cadastro1 = self.__cadastros[rand1]
            cadastro2 = self.__cadastros[rand2]
            buffer.append({'nome': cadastro1.nome, 'descricao': cadastro1.descricao, 'pais': cadastro1.pais, 'pesquisas': cadastro1.pesquisas})
            buffer.append({'nome': cadastro2.nome, 'descricao': cadastro2.descricao, 'pais': cadastro2.pais, 'pesquisas': cadastro2.pesquisas})
            resultado = self.__tela.jogar(buffer)
            if resultado is None:
                return
            elif resultado:  # Se a pessoa acertar qual é maior
                print("Você acertou")
                return True
            elif not resultado:
                return False
            
    def mudar_rejogabilidade(self):
        self.__replay = not self.__replay
        if self.__replay:
            self.__tela.mostra_mensagem("Modo de replay: Ligado!")
        else:
            self.__tela.mostra_mensagem("Modo de replay: Desligado!")

    @property
    def replay(self):
        return self.__replay