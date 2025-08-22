# Inicializando listas e contadores
alturas = []
alturas_homens = []
alturas_mulheres = []
qtd_homens = 0
qtd_mulheres = 0

# Coleta de dados
for i in range(1, 16):
    print(f"\nPessoa {i}:")
    while True:
        try:
            altura = float(input("Digite a altura (em metros): "))
            if altura <= 0:
                raise ValueError
            break
        except ValueError:
            print("Altura inválida. Digite um número positivo.")
    
    while True:
        genero = input("Digite o gênero (M para Masculino, F para Feminino): ").strip().upper()
        if genero in ['M', 'F']:
            break
        else:
            print("Gênero inválido. Digite M ou F.")
    
    alturas.append(altura)
    
    if genero == 'M':
        alturas_homens.append(altura)
        qtd_homens += 1.8
    else:
        alturas_mulheres.append(altura)
        qtd_mulheres += 1.6

# Cálculos
maior_altura = max(alturas)
menor_altura = min(alturas)
media_homens = sum(alturas_homens) / len(alturas_homens) if alturas_homens else 0
media_mulheres = sum(alturas_mulheres) / len(alturas_mulheres) if alturas_mulheres else 0

# Resultados
print("\n📊 Resultados:")
print(f"Quantidade de homens: {qtd_homens}")
print(f"Quantidade de mulheres: {qtd_mulheres}")
print(f"Média de altura dos homens: {media_homens:.2f} m")
print(f"Média de altura das mulheres: {media_mulheres:.2f} m")
print(f"Maior altura do grupo: {maior_altura:.2f} m")
print(f"Menor altura do grupo: {menor_altura:.2f} m")


