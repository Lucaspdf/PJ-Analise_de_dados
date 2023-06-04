#Analise_de_dados
#Este projeto foi capaz de identificar alguns motivos pelos quais houveram cancelamentos dos cartões de crédito, trazendo solução para esses problemas

#importando bibliotecas 
import pandas as pd 
tabela = pd.read_csv('ClientesBanco.csv', encoding = 'latin-1') 

#apresentando 
display(tabela)

#excluindo valores nulos e apresentandos determinadas informações 
tabela = tabela.drop('CLIENTNUM', axis = 1) 
tabela = tabela.dropna() 
display(tabela.info())

#Apresentando a tabela com algumas descrições e diminuindo o número de casas decimais
display(tabela.describe().round(1))

#Mostando a quantidade de clientes, separados pela categoria de clientes e cancelados
qtd_categoria = tabela["Categoria"].value_counts() display(qtd_categoria) 
qtd_categoria_perc = tabela["Categoria"].value_counts(normalize = True) 
display(qtd_categoria_perc)

#importando nova biblioteca para criar um gráfico com o método histogram extraindo da tabela a coluna idade como eixo x e as cores do gráfico como categoria 
#criamos um laço for para que cada coluna na tabela fosse separada para a classificação de categoria(cliente/cancelado). Obtendo-se o numero de cancelamentos pode-se fazer uma análise sobre os possíveis motivos 
import plotly.express as px 
for coluna in tabela: 
    grafico = px.histogram(tabela, x = coluna, color = "Categoria") 
    grafico.show()

#Aqui estão algumas observações feitas através dos gráficos obtidos

#adultos de 35 hà 60 anos são os que mais ultilizam os nossos serviços
#cartão blue é de longe o mais utilizado com 7616 usuários ativos ficando em segundo lugar silver com 473 usuários
#A inatividade causa o cancelamento, entâo é preciso incentivar o uso do cartâo com promoções e presentes
#Há algum problema com as ligações pois os clientes estão cancelando após elas, estão ligando e o problema muito provavelmente não esta sendo resolvido.
#Quanto maiores as transações menores as chances de cancelamento, então o objetivo é incentivar transações altas
#Quanto maior a quantidade de tranzações menor a chance de cancelamento, no entanto o objetivo é incentivar o uso do cartão