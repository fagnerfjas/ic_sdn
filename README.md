# ic_sdn
========
Interface de Controle para Redes Definidas por Software
Version: 0.2 2017

## Instalação

O comando (ic migrate) faz a instalação do diretório ~/.ic_sdn,
e coloca o arquivo i_sdn.db.
Este é o arquivo de banco de dados do SqLite
'''$ ic migrate'''


## Instalação de ambiente de desenvolvimento


### Observação de desenvolvimento
Para a ativação do auto-complet de cada comando, é necessário adicionar uma váriável de ambiente no linux. Exemplo:

Se o comando for 'foo bar'
'''python
eval "$(_FOO_BAR_COMPLETE=source foo-bar)" 
'''
Ou adicionar essa linha no arquivo ~/.bashrc