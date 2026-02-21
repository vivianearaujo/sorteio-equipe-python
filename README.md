## 📸 Demonstração do Sistema

### 🎫 Sorteio
<div align="center">
  <img src="./sorteio.png" width="600px" alt="Tela de Sorteio">
</div>

### 🏆 Resultado
<div align="center">
  <img src="./resultado.png" width="600px" alt="Tela de Resultado">
</div>

🎲 Sorteador My Acessórios — Gestão de Composições
Este projeto foi desenvolvido por mim (Viviane Santos) para automatizar a distribuição de itens entre uma equipe, garantindo que o resultado atual nunca se repita em relação à rodada anterior.

Originalmente criado para organizar o rodízio de composições de looks em uma loja, o sistema resolve o problema de repetição manual, trazendo imparcialidade e agilidade para o processo.

🚀 Funcionalidades
Lógica de Não-Repetição: O algoritmo verifica o que cada vendedora utilizou na semana anterior e exclui essa opção do sorteio atual.

Gestão Dinâmica de Equipe: Agora é possível adicionar ou excluir vendedoras diretamente pela interface, sem precisar mexer no código.

Interface Web Moderna: Interface limpa, responsiva e estilizada com foco na usabilidade comercial.

Prevenção de Conflitos: Sistema inteligente que reinicia o sorteio automaticamente caso as restrições gerem um impasse lógico.

🛠️ Tecnologias Utilizadas
Python 3.x: Linguagem base para a lógica.

FastAPI: Framework moderno e rápido para a criação da interface web.

Uvicorn: Servidor ASGI para rodar a aplicação.

HTML5/CSS3: Para o front-end personalizado com a identidade da marca.

PyInstaller: Utilizado para transformar o projeto em um executável (.exe) para Windows.

💻 Como Instalar e Rodar
Clone o repositório:
git clone https://github.com/SEU-USUARIO/sorteador-my-acessorios.git

Instale as dependências:
pip install fastapi uvicorn python-multipart

Inicie o servidor:
python run_sorteio.py
