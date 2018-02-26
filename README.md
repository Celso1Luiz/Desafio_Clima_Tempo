# Desafio_Clima_Tempo - Previsão do Tempo (Temperatura Máxima e Mínima) de Cidades

#Requisitos Básicos
Primeiramente o projeto foi elaborado em python 2.7, ou seja, se a versão do python for diferente 
  talvez será necessario rever algumas sintaxes
Para execução do projeto é necessario o banco de dados SQLITE  em sua maquina.
É preciso que ambos arquivos (Desafio.py e Connection.py) estejam armazenados no mesmo local.
  Obs: Os arquivos estão na aba <Wiki>

#Inicialização
Ao iniciar o programa com o banco de dados ja instalado, será criado uma tabela climatempo, ao mesmo tempo,
  se já existir alguma com o mesmo nome será excluida.
Um menu com 4 opções aparecerá, sendo elas: Cadastrar Cidades - Consultar Cidades - Consultar Gráficos -- Sair.
No primeiro momento não existirá nenhum dado cadastrado na base de dados. Sendo assim necessário cadastrar 
  as cidades para serem vizualizadas no gráfico futuramente.

#Menu
#Cadastrar Cidade -- É solicitado que informe o nome da Cidade e a Sigla do Estado da mesma.
  Obs: Cidades com acentuação gráfica não serão reconhecidas. Para teste utilizar cidades sem acentuação.
       Por exemplo -- Campinas/SP, Resende/RJ etc..
  
#Consultar Cidades -- É realizado uma busca na base de dados onde retorna todas as cidades cadastradas 
  previamente. E caso não possua nehuma, retorna uma mensagem de erro.
  
#Consultar Gráficos -- É solicitado a entrada de DUAS cidades, cadastradas, para demonstrar sua previsão 
  de 15 dias no gráfico. No gráfico o eixo x representa as Datas e o eixo y a Temperatura.
  Obs: O gráfico de maneira automatica ordena as datas no eixo X. Sendo assim quando for final do mês com 
          o começo de outro, as datas do final do mês ficarão no final do gráfico.
       Para melhor vizualização do Gráfico, Maximizar a tela.

#Sair -- O programa é encerrado.
