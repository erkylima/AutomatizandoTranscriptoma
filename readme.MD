# Script de transcriptoma
Os transcriptomas são conjuntos completos de transcritos, ou seja, RNAs mensageiros, RNA Ribossômicos, RNA transportadores e os microRNAs de determinados organismos, órgãos, tecidos ou linhagens celulares.  

## Automatizando etapas com Python
Para obtermos os VCFs que desejamos precisamos definir um roteiro de operação com todas as etapas necessárias para atingirmos o nosso objetivo. Portanto, o roteiro definido é o seguinte:

1.	Verificar a qualidade
2.	Trimar
3.	Verificar qualidade novamente
4.	Fazer montagem com referência
5.	Verificar qualidade novamente
6.	Fazer montagem de novo (recebe arquivo bam)
7.	Gerar os VCFs
8.	Processar os VCFs
 
Esse roteiro foi automatizado no script do arquivo transcriptoma.py

### Instalando Python 2.7
Antes de executar os arquivos Python voce precisa ter o git instalado na sua maquina e digitar os seguintes comandos no terminal do ubuntu

sudo apt-get install -y python

sudo apt-get install -y pip


### Executando o Script
Para executar todas as etapas de peço que faça a clonagem do repositório do GitHub abaixo e execute o arquivo transcriptomas.py e siga os passos descritos no shell ao executar o script em python.

Vale a pena lembrar que pode ser necessario ter uma IDE Python para executar o script. Por esse motivo eu recomento a IDE eric digitando o comando abaixo:

sudo apt-get install -y eric

eric --no-sandbox
