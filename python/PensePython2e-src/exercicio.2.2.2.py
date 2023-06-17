#Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias 
#recebem um desconto de 40%. O transporte custa R$ 3,00 para o primeiro 
#exemplar e 75 centavos para cada exemplar adicional. 
#Qual é o custo total de atacado para 60 cópias?

preco_capa = 24.95
desconto_livraria = 0.40
transporte_primeiro_exemplar = 3
transporte_exemplar_adicional = 0.75

qtd_copias = 60

custo = qtd_copias * (preco_capa * desconto_livraria) + (transporte_primeiro_exemplar + (qtd_copias - 1) * transporte_exemplar_adicional)

print("custo: ", custo)