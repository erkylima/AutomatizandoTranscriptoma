import os

# Verificar qualidade

def verificarResposta(etapa,  nome_etapa):
    while True:
        resposta = input('Concluiu a verificação de qualidade da amostra (s/n)? \n')
        if str(resposta) == 's':
            print("Parabéns! Vamos para a próxima etapa!")
            break
        elif str(resposta) == 'n':
            print("Conclua a {}!".format(nome_etapa))
            etapa()
        else:
            print('Resposta inválida! Tente novamente!')

def verificarQualidadeFastq():
    os.system('fastQC/fastqc')
    verificarResposta( lambda: verificarQualidadeFastq(), 'verificação de qualidade da amostra')

def trimagem(nome_arquivo):
    trim_left = input('Insira o parâmetro trim_left >\n')    
    trim_qual_left = input('Insira o parâmetro trim_qual_left >\n')    
    trim_qual_right = input('Insira o parâmetro trim_qual_right >\n')    
    trim_qual_window = input('Insira o parâmetro trim_qual_window >\n')    
    trim_qual_step = input('Insira o parâmetro trim_qual_step >\n')    
    min_qual_mean = input('Insira o parâmetro min_qual_mean >\n')    
    min_len = input('Insira o parâmetro min_len >\n')    

    os.system('perl prinseq/prinseq-lite.pl -fastq prova/{} -trim_left {} -trim_qual_left {} -trim_qual_right {} -trim_qual_window {} -trim_qual_step {} -min_qual_mean {} -min_len {} -out_format 3 -out_good automaresult/{}_trimmed -out_bad automaresult/{}_bad -log automaresult/{}.log'.format(nome_arquivo, trim_left, trim_qual_left, trim_qual_right,  trim_qual_window, trim_qual_step, min_qual_mean,  min_len, nome_arquivo.split('.')[0], nome_arquivo.split('.')[0], nome_arquivo.split('.')[0]))
    
    return "automaresult/{}_trimmed.fastq".format(nome_arquivo)
    
def prepararMontagens():
    os.system("sudo apt-get install -y libcairo2-dev")
    #os.system("cp -puv prinseq/prinseq-lite.pl /usr/local/bin/prinseq-lite && chmod +x /usr/local/bin/prinseq-lite")
    #os.system("cp -puv prinseq/prinseq-graphs.pl /usr/local/bin/prinseq-graphs && chmod +x /usr/local/bin/prinseq-graphs")
    os.system("sudo apt install -y default-jre")
    os.system("sudo apt-get install -y bwa")
    os.system("sudo apt-get install -y samtools")
    os.system("sudo apt-get install -y valvet")
    os.system("sudo apt-get install -y bcftools")
    
def montagemReferencia(amostra_trimada, arq_referencia):
    nome_trimado = amostra_trimada.split('/')[1].split(".")[0]
    pasta_results = amostra_trimada.split('/')[0]
    os.system("bwa index {}".format(arq_referencia))
    os.system("bwa mem {} {}/{}_trimmed.fastq > {}/{}alinhamento.sam".format(arq_referencia,  pasta_results, nome_trimado,  pasta_results, nome_trimado))
    os.system("samtools view -bS {}/{}alinhamento.sam > {}/{}alinhamento.bam".format(pasta_results, nome_trimado, pasta_results, nome_trimado))
    os.system("samtools sort {}/{}alinhamento.bam -o {}/{}alinhamento_sort.bam".format(pasta_results, nome_trimado, pasta_results, nome_trimado))
    os.system("samtools index {}/{}alinhamento_sort.bam".format(pasta_results,  nome_trimado))

def verificarMontagem():    
    os.system("java -Xmx9g -jar BAMStats/BAMStats-GUI-1.25.jar")
    verificarResposta( lambda: verificarMontagem(), 'verificação de qualidade da montagem')

def montagemDeNovo(nome_amostra, referencia):
    kmer= input("Insira o valor do kmer > \n")
    os.system("velveth kmer_{} {} -short -fastq prova/{}".format(kmer, kmer, nome_amostra))
    contigs= input("Insira o valor minimo de contigs > \n") 
    os.system("quast-5.0.2/quast.py --min-contig {} kmer_{}/contigs.fa -r {}".format(contigs, kmer, referencia))
    
def gerarVCF(nome_amostra, referencia):
    os.system("samtools mpileup -uD -f {} automaresult/{}alinhamento_sort.bam |bcftools view -> {}variants.vcf".format(referencia, nome_amostra.split(".")[0], nome_amostra.split(".")[0]))
    
prepararMontagens()
verificarQualidadeFastq()
amostra= input('Insira o diretório e nome do arquivo a ser trimado que está na pasta prova >\n')  
nomedir_trimado = trimagem(amostra)
verificarQualidadeFastq()
arq_referencia = input("Insira o diretório e nome do arquivo de referência > \n")
montagemReferencia(nomedir_trimado,arq_referencia)
verificarMontagem()
montagemDeNovo(amostra,arq_referencia)
gerarVCF(amostra, arq_referencia)

