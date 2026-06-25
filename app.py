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


@app.route("/search")
def search():
    q = request.args.get("q", "").strip().lower()

    pages = [
        {"title": "Home", "endpoint": "home", "text": "Welcome"},
        {
            "title": "About Us",
            "endpoint": "about",
            "text": "Discover what we have to offer",
        },
        {"title": "Contact", "endpoint": "contact", "text": "Get in touch with us"},
    ]

    results = [
        p for p in pages if q and (q in p["title"].lower() or q in p["text"].lower())
    ]

    return render_template("search_results.html", query=q, results=results)


@app.route("/library")
def library():
    return render_template("library.html", pages=PAGES)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
