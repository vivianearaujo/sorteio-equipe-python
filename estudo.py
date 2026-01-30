import random

# 1. Configuração oficial My Acessórios
equipe = ["Viviane", "Rayla", "Jane", "Kawany", "Núbia"]
pecas = ["Mix Verão", "Prata", "Dourado", "Longo Dourado", "Mix de Banho"]

def realizar_sorteio():
    print("✨ CONFIGURAÇÃO DO SORTEIO - MY ACESSÓRIOS ✨")
    print("Informe o que cada uma usou na semana passada:")
    print(f"Opções: {', '.join(pecas)}\n")

    historico_manual = {}
    for nome in equipe:
        while True:
            # Pega o que você digitou e compara sem ligar para maiúsculas/minúsculas
            entrada = input(f"O que a {nome} usou semana passada? ").strip()

            # Procura a peça na lista ignorando se é maiúscula ou minúscula
            peca_encontrada = next((p for p in pecas if p.lower() == entrada.lower()), None)

            if peca_encontrada:
                historico_manual[nome] = peca_encontrada
                break
            else:
                print(f"⚠️ Erro! Digite exatamente como na lista: {pecas}")

    # 2. Lógica de Sorteio com Restrição Única
    while True:
        try:
            sorteio_atual = {}
            disponiveis_agora = pecas.copy()
            random.shuffle(disponiveis_agora)

            for nome in equipe:
                ultima_peca = historico_manual.get(nome)
                opcoes_validas = [p for p in disponiveis_agora if p != ultima_peca]

                escolha = random.choice(opcoes_validas)
                sorteio_atual[nome] = escolha
                disponiveis_agora.remove(escolha)

            return sorteio_atual
        except IndexError:
            continue

# 3. Execução e Apresentação
resultado = realizar_sorteio()

print("\n" + "═"*45)
print(" 🎲  RESULTADO DO SORTEIO - COMPOSIÇÕES  🎲")
print("═"*45)
for nome, peca in resultado.items():
    print(f" 💎  {nome.ljust(8)}  ➔   {peca.ljust(15)}")

print("═"*45)
print(" ✨ Boas vendas Viviane, Rayla, Jane, Kawany e Núbia! ✨")
print("═"*45)
