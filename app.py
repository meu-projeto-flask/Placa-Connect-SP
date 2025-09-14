from flask import Flask, render_template, request, redirect, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Configuração banco SQLite
DB_PATH = os.path.join("data", "pedidos.db")
WHATSAPP_NUMERO = "5511941780511"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS pedidos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    telefone TEXT,
                    servico TEXT,
                    mensagem TEXT
                )''')
    conn.commit()
    conn.close()

def salvar_pedido(nome, telefone, servico, mensagem):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO pedidos (nome, telefone, servico, mensagem) VALUES (?, ?, ?, ?)",
              (nome, telefone, servico, mensagem))
    conn.commit()
    conn.close()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/regras-emplacamento")
def regras():
    return render_template("regras.html")

@app.route("/servicos")
def servicos():
    return render_template("servicos.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    nome = request.form.get("nome")
    telefone = request.form.get("telefone")
    servico = request.form.get("servico")
    mensagem = request.form.get("mensagem")

    salvar_pedido(nome, telefone, servico, mensagem)
    flash("Pedido enviado com sucesso! Entraremos em contato pelo WhatsApp.")

    wa_text = f"Olá, meu nome é {nome}. Gostaria de {servico}. Telefone: {telefone}. Mensagem: {mensagem}"
    return redirect(f"https://wa.me/{WHATSAPP_NUMERO}?text={wa_text}")

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
