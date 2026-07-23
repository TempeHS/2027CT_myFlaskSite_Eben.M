from flask import Flask, render_template, request

app = Flask(__name__)

PAGES = [
    {"title": "Home", "endpoint": "home", "text": "Welcome"},
    {
        "title": "About Us",
        "endpoint": "about",
        "text": "Discover what we have to offer",
    },
    {"title": "Contact", "endpoint": "contact", "text": "Get in touch with us"},
    {"title": "Library", "endpoint": "library", "text": "Browse all pages"},
    {
        "title": "Eren Yeager",
        "endpoint": "eren",
        "text": "Work in Progress: Coming Soon!",
    },
    {
        "title": "Mikasa Ackerman",
        "endpoint": "mikasa",
        "text": "Work in Progress: Coming Soon!",
    },
    {
        "title": "Armin Arlert",
        "endpoint": "armin",
        "text": "Work in Progress: Coming Soon!",
    },
    {
        "title": "Pure Titan",
        "endpoint": "titan",
        "text": "Work in Progress: Coming Soon!",
    },
    {
        "title": "Abnormal Titan",
        "endpoint": "abnormal",
        "text": "Work in Progress: Coming Soon!",
    },
    {
        "title": "Attack Titan",
        "endpoint": "attack",
        "text": "Work in Progress: Coming Soon!",
    },
    {
        "title": "Founding Titan",
        "endpoint": "founding",
        "text": "Work in Progress: Coming Soon!",
    },
    {
        "title": "Armoured Titan",
        "endpoint": "armoured",
        "text": "Work in Progress: Coming Soon!",
    },
    {
        "title": "Female Titan",
        "endpoint": "female",
        "text": "Work in Progress: Coming Soon!",
    },
    {
        "title": "Colossal Titan",
        "endpoint": "colossal",
        "text": "Work in Progress: Coming Soon!",
    },
    {
        "title": "Beast Titan",
        "endpoint": "beast",
        "text": "Work in Progress: Coming Soon!",
    },
    {
        "title": "Jaw Titan",
        "endpoint": "jaw",
        "text": "Work in Progress: Coming Soon!",
    },
    {
        "title": "Cart Titan",
        "endpoint": "cart",
        "text": "Work in Progress: Coming Soon!",
    },
    {
        "title": "Warhammer Titan",
        "endpoint": "warhammer",
        "text": "Work in Progress: Coming Soon!",
    },
]
CHARS = [
    {
        "title": "Eren Yeager",
        "endpoint": "eren",
        "text": "Work in Progress: Coming Soon!",
    },
    {
        "title": "Mikasa Ackerman",
        "endpoint": "mikasa",
        "text": "Work in Progress: Coming Soon!",
    },
    {
        "title": "Armin Arlert",
        "endpoint": "armin",
        "text": "Work in Progress: Coming Soon!",
    },
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


@app.route("/eren")
def eren():
    return render_template("characters/eren.html")


@app.route("/mikasa")
def mikasa():
    return render_template("characters/mikasa.html")


@app.route("/armin")
def armin():
    return render_template("characters/armin.html")


@app.route("/titan")
def titan():
    return render_template("titans/titan.html")


@app.route("/abnormal")
def abnormal():
    return render_template("titans/abnormal.html")


@app.route("/attack")
def attack():
    return render_template("titans/attack.html")


@app.route("/founding")
def founding():
    return render_template("titans/founding.html")


@app.route("/armoured")
def armoured():
    return render_template("titans/armoured.html")


@app.route("/female")
def female():
    return render_template("titans/female.html")


@app.route("/colossal")
def colossal():
    return render_template("titans/colossal.html")


@app.route("/beast")
def beast():
    return render_template("titans/beast.html")


@app.route("/jaw")
def jaw():
    return render_template("titans/jaw.html")


@app.route("/cart")
def cart():
    return render_template("titans/cart.html")


@app.route("/warhammer")
def warhammer():
    return render_template("titans/warhammer.html")


@app.route("/search")
def search():
    q = request.args.get("q", "").strip().lower()

    results = [
        p for p in PAGES if q and (q in p["title"].lower() or q in p["text"].lower())
    ]

    return render_template("search_results.html", query=q, results=results)


@app.route("/characters")
def characters():
    return render_template("characters.html", characters=CHARS)


@app.route("/library")
def library():
    return render_template("library.html", pages=PAGES)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
