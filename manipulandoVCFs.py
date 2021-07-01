arq_vcf = input('Insira o nome do arquivo VCF a ser manipulado > \n')

def quantidadeVariantes(arq_vcf, base, qnt_linhas):
    vcf = open(arq_vcf)
    count = 0
    for i, linha in enumerate(vcf):
        if "#" in linha:
            continue
        
        if i ==qnt_linhas:            
            break
            
        rec=linha.split("\t")
        if rec[3] == base:
            count+=1
    if base == "A":
        nome_base ="adininas" 
    elif base == "T":
        nome_base="timinas"
    elif base == "G":
        nome_base="guaninas"
    elif base == "C":
        nome_base="citosinas"
        
    print("Foram encontrados {} variantes de {} nas primeiras {} linhas desse VCF".format(count, nome_base, qnt_linhas))
    print("=========================")
quantidadeVariantes(arq_vcf, "A",  1000)
quantidadeVariantes(arq_vcf, "T",  5000)
quantidadeVariantes(arq_vcf, "G",  2000)
quantidadeVariantes(arq_vcf, "C",  3000)
