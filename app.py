from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", title="Início")

@app.route("/servicos")
def servicos():
    return render_template("servicos.html", title="Serviços")

@app.route("/contato", methods=["GET", "POST"])
def contato():
    if request.method == "POST":
        nome = request.form["nome"]
        telefone = request.form["telefone"]
        mensagem = request.form["mensagem"]
        numero = "5511941780511"
        texto = f"Olá, meu nome é {nome}. Telefone: {telefone}. Mensagem: {mensagem}"
        return redirect(f"https://wa.me/{numero}?text={texto}")
    return render_template("contato.html", title="Contato")

@app.route("/sitemap.xml")
def sitemap():
    return render_template("sitemap.xml"), 200, {"Content-Type": "application/xml"}

@app.route("/robots.txt")
def robots():
    return app.send_static_file("robots.txt")

if __name__ == "__main__":
    app.run(debug=True)
