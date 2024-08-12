from cliente import Cliente
from fornecedor import Fornecedor
from mercado import Mercado
from produto import Produto
from transacao import Transacao

def instanciar_clientes():
    cliente1 = Cliente("João", "(55)3054-5478", "Rua dos Arbustos, nº 1101")
    cliente2 = Cliente("Maria", "(55)3054-5478", "Rua Santo Espedido, nº 1010")
    cliente3 = Cliente("José", "(55)3054-5478", "Rua Ada Lovelace, nº 111")
    
    return cliente1, cliente2, cliente3

def instanciar_produtos():
    produto1 = Produto("Arroz", "Alimento", 10)
    produto2 = Produto("Feijão", "Alimento", 5)
    produto3 = Produto("Macarrão", "Alimento", 15)
    
    return produto1, produto2, produto3

def instanciar_fornecedores():
    fornecedor1 = Fornecedor("Arroz da Fazenda")
    fornecedor2 = Fornecedor("Feijão da cantina")
    fornecedor3 = Fornecedor("Itália massas") 

    return fornecedor1, fornecedor2, fornecedor3

def instanciar_mercado():
    cliente1, cliente2, cliente3 = instanciar_clientes()
    produto1, produto2, produto3 = instanciar_produtos()

    transacao1 = Transacao(cliente1, produto1, 2)
    transacao2 = Transacao(cliente2, produto2, 3)
    transacao3 = Transacao(cliente3, produto3, 1)
    
    mercado = Mercado("Mercearia da Esquina")
    
    mercado.adicionar_cliente(cliente1)
    mercado.adicionar_cliente(cliente2)
    mercado.adicionar_cliente(cliente3)
    
    mercado.adicionar_transacao(transacao1)
    mercado.adicionar_transacao(transacao2)
    mercado.adicionar_transacao(transacao3)
    
    return mercado

def main():
    mercado = instanciar_mercado()
    print("\nCLIENTES:\n")
    print(mercado.listar_clientes())
    print("\nTRANSAÇÕES:\n")
    print(mercado.listar_transacoes())

main()