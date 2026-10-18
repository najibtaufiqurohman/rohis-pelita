
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def beranda():
    return render_template("index.html")


@app.route("/tentang")
def tentang():
    return render_template("tentang.html")


@app.route("/kegiatan")
def kegiatan():
    return render_template("kegiatan.html")


@app.route("/struktur")
def struktur():
    return render_template("struktur.html")


@app.route("/galeri")
def galeri():
    return render_template("galeri.html")


@app.route("/kontak")
def kontak():
    return render_template("kontak.html")


if __name__ == "__main__":
    app.run(debug=True)
