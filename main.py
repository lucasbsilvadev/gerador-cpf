import random

def gerar_digitos_aleatorios():

    digitos = [ random.randint(0, 9) for _ in range(8)] 
    return digitos

# cada digito tem q ser um n separado pra ser usado em operação depois
# decidir tipo de armazenamento dos digitos


def escolhe_id_regiao():
    # dicionario de regiao 
    regioes = {
        0: "Rio Grande do Sul (RS)",
        1: "Distrito Federal (DF), Goiás (GO), Mato Grosso (MT), Mato Grosso do Sul (MS) e Tocantins (TO)",
        2: "Acre (AC), Amazonas (AM), Amapá (AP), Pará (PA), Rondônia (RO) e Roraima (RR)",
        3: "Ceará (CE), Maranhão (MA) e Piauí (PI)",
        4: "Alagoas (AL), Paraíba (PB), Pernambuco (PE) e Rio Grande do Norte (RN)",
        5: "Bahia (BA) e Sergipe (SE)",
        6: "Minas Gerais (MG)",
        7: "Espírito Santo (ES) e Rio de Janeiro (RJ)",
        8: "São Paulo (SP)",
        9: "Paraná (PR) e Santa Catarina (SC)"
    }

    id_regiao = random.randint(0, 9)
    nome_regiao = regioes[id_regiao]

    print(f"Região selecionada: {nome_regiao}")
    return id_regiao

def calcular_d1(digitos, id_regiao):
    s1 = (digitos[0] * 10 +
          digitos[1] * 9 +
          digitos[2] * 8 +
          digitos[3] * 7 +
          digitos[4] * 6 +
          digitos[5] * 5 +
          digitos[6] * 4 +
          digitos[7] * 3 +
          id_regiao)

    resto = s1 % 11

    if resto == 0 or resto == 1:
        return 0
    else:
        return 11 - resto

def calcular_d2(digitos, id_regiao, d1):
    s2 =  (digitos[0] * 11 +
          digitos[1] * 10 +
          digitos[2] * 9 +
          digitos[3] * 8 +
          digitos[4] * 7 +
          digitos[5] * 6 +
          digitos[6] * 5 +
          digitos[7] * 4 +
          id_regiao +
          d1) 

    resto = s2 % 11

    if resto == 0 or resto == 1:
        return 0
    else:
        return 11 - resto

def montar_cpf(digitos, id_regiao, d1, d2):

    cpf = (str(digitos[0]) + str(digitos[1]) + str(digitos[2]) + "." +
    str(digitos[3]) + str(digitos[4]) + str(digitos[5]) + "." +
    str(digitos[6]) + str(digitos[7]) + str(id_regiao) + "-" +
    str(d1) + str(d2))
    return cpf

def main():
    print("=== GERADOR DE CPF ===\n")
    
    digitos = gerar_digitos_aleatorios()
    print("Dígitos gerados:", digitos)
    
    id_regiao = escolhe_id_regiao()
    
    d1 = calcular_d1(digitos, id_regiao)
    print("D1 calculado:", d1)
    
    d2 = calcular_d2(digitos, id_regiao, d1)
    print("D2 calculado:", d2)
    
    cpf = montar_cpf(digitos, id_regiao, d1, d2)
    print(f"\nCPF gerado: {cpf}")

if __name__ == "__main__":
    main()

