# Função para adicionar um produto à lista
def adicionar_produto(lista_produtos):
    produto = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    valor_unitario = float(input("Digite o valor unitário: "))
    
    total_produto = quantidade * valor_unitario
    
    novo_produto = {
        "produto": produto,
        "quantidade": quantidade,
        "valor": valor_unitario,
        "total": total_produto
    }
    
    lista_produtos.append(novo_produto)
    print("Produto adicionado com sucesso!")


# Função para visualizar a lista de produtos
def visualizar_lista(lista_produtos):
    print("Lista de produtos:")
    for produto in lista_produtos:
        print(f"Nome: {produto['produto']}, Quantidade: {produto['quantidade']}, Valor Unitário: {produto['valor']}, Total: {produto['total']}")
    
    total_geral = sum(produto['total'] for produto in lista_produtos)
    print(f"Total de todos os produtos: {total_geral}")


# Função para atualizar as informações de um produto
def atualizar_produto(lista_produtos):
    nome_produto = input("Digite o nome do produto que deseja atualizar: ")
    
    for produto in lista_produtos:
        if produto['produto'] == nome_produto:
            produto['produto'] = input("Digite o novo nome do produto: ")
            produto['quantidade'] = int(input("Digite a nova quantidade: "))
            produto['valor'] = float(input("Digite o novo valor unitário: "))
            
            produto['total'] = produto['quantidade'] * produto['valor']
            
            print("Produto atualizado com sucesso!")
            return
    
    print("Produto não encontrado!")


# Função para remover um produto da lista
def remover_produto(lista_produtos):
    nome_produto = input("Digite o nome do produto que deseja remover: ")
    
    for produto in lista_produtos:
        if produto['produto'] == nome_produto:
            lista_produtos.remove(produto)
            print("Produto removido com sucesso!")
            return
    
    print("Produto não encontrado!")


# Função principal
def main():
    lista_produtos = []
    
    while True:
        print("\n--- MENU ---")
        print("1. Adicionar produto")
        print("2. Visualizar lista de produtos")
        print("3. Atualizar produto")
        print("4. Remover produto")
        print("5. Encerrar programa")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_produto(lista_produtos)
        elif opcao == "2":
            visualizar_lista(lista_produtos)
        elif opcao == "3":
            atualizar_produto(lista_produtos)
        elif opcao == "4":
            remover_produto(lista_produtos)
        elif opcao == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()