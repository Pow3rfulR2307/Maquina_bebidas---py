from numpy import array

class Produtos():

    objetos = {}
    def __init__(self, id, nome, valor, estoque):

        self.id = id
        self.nome = nome
        self.valor = valor
        self.estoque = estoque
        Produtos.objetos[self.id] = self

    @classmethod #metodo pode ser operado sem instancias, recebe 'cls' como parametro ao invés de self
    def mostrar_produtos(cls): 
        for produto in cls.objetos.values():
            print(vars(produto)) #vars retorna todos os atributos de um objeto

    @classmethod
    def remover_produto(cls, id_produto):
        if id_produto in cls.objetos:
            del cls.objetos[id_produto] 

    @classmethod
    def editar_produto(cls, id, atributo, novoAtributo):
       produto = cls.objetos.get(id)
       if produto:
           setattr(produto, atributo, novoAtributo)
       else:
           print("Não foi possível encontrar o ID do produto!")

    @classmethod
    def comprar_produto(cls, id, possibilidades):
        produto = cls.objetos.get(id)
        if produto and produto.estoque>=1:
            print(f"Produto {produto.nome} encontrado, valor a pagar R${produto.valor}.")
            
            pagamento = pegar_pagamento()
            
            if pagamento < produto.valor:
                print("Valor insuficiente.")
            
            else:
                valor_troco = pagamento - produto.valor
                for v in possibilidades:
                    if valor_troco > v:
                        quantidade = int(valor_troco/v)
                        print(f">> CONFIRA O TROCO: {quantidade}x{v}")
                        valor_troco -= v*quantidade #tira do valor pago as notas já pagas
                print("Pagamento realizado.")
                produto.estoque-=1
        else:
            print("Produto não encontrado ou sem estoque, por favor tente novamente.")
    
def pegar_id():

    selecao = int(input("---Digite o ID da bebida:---\n"))
    return selecao

def operacao(opcoes, mensagem):

    selecao = None
    while selecao not in opcoes:
        selecao=int(input(mensagem))
    return selecao

def pegar_pagamento():

    pagamento = 0.0
    while pagamento<=0.0:
        pagamento = float(input("Digite o valor a pagar: "))
    return pagamento

if __name__ == "__main__":

    print("PROJETO MÁQUINA\n")
    #array fixo com notas de troco
    possibilidades = array([200,100,50,20,10,5,2,1,0.5,0.25,0.1,0.5,0.01])
    contador = 0
    #CRIANDO 5 PRODUTOS PARA COMEÇAR O PROGRAMA    
    Produtos(contador, "COCA-COLA", 3.75, 2)
    contador+=1
    Produtos(contador, "PEPSI", 3.67, 5)
    contador+=1
    Produtos(contador, "MONSTER", 9.96, 1)
    contador+=1
    Produtos(contador, "CAFÉ", 1.25, 100)
    contador+=1
    Produtos(contador, "REDBULL", 13.99, 2)

    while True:
        
        Produtos.mostrar_produtos()
        modoUser = operacao([1,2,3], ">> Digite 1 para modo administrador, 2 para usuário, 3 para sair: ")
        if modoUser==1:

            tipoOperacao = operacao([1,2,3], "---MODO ADMINISTRDOR---\n1.REMOVER\n2.ADICIONAR\n3.EDITAR\n")
            if tipoOperacao==1:

                removerID= pegar_id()
                Produtos.remover_produto(removerID)
                
            elif tipoOperacao==2:
                
                novoValor = 0.0
                contador+=1

                novoNome=input('Digite o nome do produto: ').upper().strip()
                while novoValor <= 0.0:
                    novoValor=float(input('Digite o valor do produto(minímo 0.1): '))
                novoEstoque=int(input('Digite o estoque do produto: '))

                Produtos(contador, novoNome, novoValor, novoEstoque)

            else:

                idBusca = pegar_id()
                selecaoAtributo = operacao([1,2,3], "1.Nome\n2.Valor\n3.Estoque:\n")
                if selecaoAtributo==1:

                    novoNome = input("Digite o novo nome: ").upper().strip()
                    Produtos.editar_produto(idBusca, "nome", novoNome)

                elif selecaoAtributo==2:
                    
                    novoValor = float(input("Digite o novo valor: "))
                    Produtos.editar_produto(idBusca, "valor", novoValor)

                else:
                    
                    novoEstoque = int(input("Digite o novo estoque: "))
                    Produtos.editar_produto(idBusca, "estoque", novoEstoque)

        elif modoUser == 2:
            print('>> AS BEBIDAS DISPONÍVEIS SÃO:\n')
            Produtos.mostrar_produtos()
            idComprar = pegar_id()

            Produtos.comprar_produto(idComprar, possibilidades)
        
        else:
            break
    print("---Programa Encerrado---")