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
]
CHARS = [
    {
        "title": "Eren Yeager",
        "endpoint": "eren",
        "text": "Eren Yeager is the protagonist of Attack on Titan",
    },
    {
        "title": "Mikasa Ackerman",
        "endpoint": "mikasa",
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
    return render_template("eren.html")


@app.route("/mikasa")
def mikasa():
    return render_template("mikasa.html")


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
