# 🎲 Algoritmo de Sorteio com Restrição de Histórico

Este projeto foi desenvolvido para automatizar a distribuição de itens ou tarefas entre uma equipe, garantindo que o resultado atual nunca se repita em relação à rodada anterior. 

Originalmente criado para organizar o rodízio de composições de looks em uma loja, o sistema resolve o problema de repetição manual, trazendo imparcialidade e agilidade para o processo.

---

## 🚀 Funcionalidades

* **Lógica de Não-Repetição:** O algoritmo verifica o que cada usuário utilizou na rodada anterior e exclui essa opção do sorteio atual.
* **Interface Web Modern:** Interface limpa e responsiva construída com FastAPI e CSS, focada na usabilidade.
* **Prevenção de Conflitos:** Sistema inteligente que reinicia o sorteio automaticamente caso as restrições gerem um impasse lógico.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**: Linguagem base para a lógica.
* **FastAPI**: Framework moderno para a criação da interface web e API.
* **Uvicorn**: Servidor ASGI para rodar a aplicação.
* **Jinja2/HTML5/CSS3**: Para o front-end estilizado.

---

## 💻 Como Instalar e Rodar

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
