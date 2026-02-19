from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

equipe = ["Viviane", "Rayla", "Jane", "Kawany", "Núbia", "Joyce"]
pecas = ["Mix Verão", "Prata", "Dourado", "Longo Dourado", "Mix de Banho", "Bijour"]

# CSS Estilizado para o Sorteio
ESTILO_SORTEIO = """
<style>
    :root { --ouro: #D4AF37; --rosa: #ff69b4; --vinho: #800000; }
    body { font-family: 'Segoe UI', sans-serif; background: #fff5f8; text-align: center; }
    .card-sorteio { background: white; border-radius: 15px; padding: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); display: inline-block; margin-top: 20px; }
    .resultado-item { border-bottom: 1px solid #eee; padding: 10px; display: flex; justify-content: space-between; width: 300px; }
    .vendedora { font-weight: bold; color: var(--vinho); }
    .peca { color: var(--ouro); font-weight: bold; }
    select { padding: 8px; border-radius: 5px; border: 1px solid var(--rosa); margin: 5px; }
    button { background: var(--vinho); color: white; padding: 10px 20px; border: none; border-radius: 20px; cursor: pointer; font-weight: bold; }
</style>
"""

@app.get("/", response_class=HTMLResponse)
async def pagina_sorteio():
    # Cria os menus de seleção para cada vendedora
    inputs = ""
    for nome in equipe:
        opcoes = "".join([f"<option value='{p}'>{p}</option>" for p in pecas])
        inputs += f"<div><label>{nome}:</label> <select name='{nome}'>{opcoes}</select></div>"
    
    return f"""
    <html>
        <head><title>Sorteio My Acessórios</title>{ESTILO_SORTEIO}</head>
        <body>
            <h1 style='color: var(--vinho)'>✨ Sorteio de Composições ✨</h1>
            <p>Selecione o que cada uma usou na <b>semana passada</b>:</p>
            <form action="/sortear" method="post">
                <div class="card-sorteio">{inputs}<br><button type="submit">GERAR SORTEIO DA SEMANA</button></div>
            </form>
        </body>
    </html>
    """

@app.post("/sortear", response_class=HTMLResponse)
async def sortear(
    # Aqui o FastAPI recebe as escolhas da semana passada
    Viviane: str = Form(...), Rayla: str = Form(...), Jane: str = Form(...), 
    Kawany: str = Form(...), Núbia: str = Form(...), Joyce: str = Form(...)
):
    historico = {"Viviane": Viviane, "Rayla": Rayla, "Jane": Jane, "Kawany": Kawany, "Núbia": Núbia, "Joyce": Joyce}
    
    # Lógica do Sorteio (mesma que você já fez)
    while True:
        try:
            sorteio_final = {}
            disponiveis = pecas.copy()
            random.shuffle(disponiveis)
            for nome in equipe:
                opcoes_validas = [p for p in disponiveis if p != historico[nome]]
                escolha = random.choice(opcoes_validas)
                sorteio_final[nome] = escolha
                disponiveis.remove(escolha)
            break
        except: continue

    res_html = "".join([f"<div class='resultado-item'><span class='vendedora'>{n}</span> <span class='peca'>💎 {p}</span></div>" for n, p in sorteio_final.items()])
    
    return f"""
    <html>
        <head>{ESTILO_SORTEIO}</head>
        <body>
            <h1 style='color: var(--vinho)'>🎲 Resultado da Semana 🎲</h1>
            <div class="card-sorteio">{res_html}<br><a href="/">Refazer Sorteio</a></div>
        </body>
    </html>
    """
