from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
import random

app = FastAPI()

# Lista inicial de vendedoras e peças
equipe = ["Viviane", "Rayla", "Jane", "Kawany", "Núbia", "Joyce"]
pecas = ["Mix Verão", "Prata", "Dourado", "Longo Dourado", "Mix de Banho", "Bijour"]

ESTILO_SORTEIO = """
<style>
    :root { --ouro: #D4AF37; --rosa: #ff69b4; --vinho: #800000; }
    body { font-family: 'Segoe UI', sans-serif; background: #fff5f8; text-align: center; padding: 20px; color: #333; }
    .card { background: white; border-radius: 15px; padding: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); display: inline-block; margin: 10px; vertical-align: top; min-width: 350px; }
    .item { border-bottom: 1px solid #eee; padding: 10px; display: flex; justify-content: space-between; align-items: center; }
    .vendedora { font-weight: bold; color: var(--vinho); }
    .peca { color: var(--ouro); font-weight: bold; }
    select, input { padding: 8px; border-radius: 5px; border: 1px solid var(--rosa); margin: 5px; }
    button { background: var(--vinho); color: white; padding: 10px 20px; border: none; border-radius: 20px; cursor: pointer; font-weight: bold; transition: 0.3s; }
    button:hover { background: var(--rosa); }
    .btn-excluir { background: #ff4d4d; color: white !important; padding: 2px 8px; border-radius: 10px; font-size: 12px; text-decoration: none; }
    .btn-add { background: #28a745; margin-top: 10px; }
    .footer { margin-top: 40px; padding: 20px; border-top: 1px solid #ddd; color: var(--vinho); font-size: 14px; }
    a { text-decoration: none; color: var(--vinho); font-weight: bold; }
</style>
"""

def get_footer():
    return '<div class="footer">💎 Sistema desenvolvido por <b>Viviane Santos</b> — 2026</div>'

@app.get("/", response_class=HTMLResponse)
async def pagina_principal():
    inputs_sorteio = ""
    lista_gerenciamento = ""
    
    for nome in equipe:
        opcoes = "".join([f"<option value='{p}'>{p}</option>" for p in pecas])
        inputs_sorteio += f"<div class='item'><label class='vendedora'>{nome}:</label> <select name='{nome}'>{opcoes}</select></div>"
        lista_gerenciamento += f"<div class='item'><span>{nome}</span> <a href='/excluir/{nome}' class='btn-excluir'>Excluir</a></div>"

    return f"""
    <html>
        <head><title>Sorteio My Acessórios</title>{ESTILO_SORTEIO}</head>
        <body>
            <h1 style='color: var(--vinho)'>✨ Gestão de Composições ✨</h1>
            
            <div style="display: flex; justify-content: center; flex-wrap: wrap;">
                <div class="card">
                    <h3>🎲 Realizar Sorteio</h3>
                    <form action="/sortear" method="post">
                        {inputs_sorteio}
                        <br>
                        <button type="submit">GERAR SORTEIO DA SEMANA</button>
                    </form>
                </div>

                <div class="card">
                    <h3>👥 Gerenciar Atendentes</h3>
                    <form action="/adicionar" method="post">
                        <input type="text" name="novo_nome" placeholder="Nome da vendedora" required>
                        <br>
                        <button type="submit" class="btn-add">+ Adicionar</button>
                    </form>
                    <div style="margin-top: 20px; text-align: left;">
                        {lista_gerenciamento}
                    </div>
                </div>
            </div>
            {get_footer()}
        </body>
    </html>
    """

@app.post("/adicionar")
async def adicionar_atendente(novo_nome: str = Form(...)):
    nome_limpo = novo_nome.strip()
    if nome_limpo and nome_limpo not in equipe:
        equipe.append(nome_limpo)
    return RedirectResponse(url="/", status_code=303)

@app.get("/excluir/{nome}")
async def excluir_atendente(nome: str):
    if nome in equipe:
        equipe.remove(nome)
    return RedirectResponse(url="/", status_code=303)

@app.post("/sortear", response_class=HTMLResponse)
async def sortear(request: Request):
    form_data = await request.form()
    historico = {nome: form_data.get(nome) for nome in equipe}
    
    intentos = 0
    sorteio_final = {}
    
    while intentos < 100:
        try:
            temp_sorteio = {}
            disponiveis = pecas.copy()
            random.shuffle(disponiveis)
            for nome in equipe:
                opcoes_validas = [p for p in disponiveis if p != historico.get(nome)]
                escolha = random.choice(opcoes_validas)
                temp_sorteio[nome] = escolha
                disponiveis.remove(escolha)
            sorteio_final = temp_sorteio
            break
        except: 
            intentos += 1
            continue

    res_html = "".join([f"<div class='item'><span class='vendedora'>{n}</span> <span class='peca'>💎 {p}</span></div>" for n, p in sorteio_final.items()])
    
    return f"""
    <html>
        <head>{ESTILO_SORTEIO}</head>
        <body>
            <h1 style='color: var(--vinho)'>🎲 Resultado 🎲</h1>
            <div class="card">{res_html}<br><a href="/">⬅ Voltar</a></div>
            {get_footer()}
        </body>
    </html>
    """
