from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Imed Mnif',
        'title': 'First Blog Post',
        'content': 'First post content',
        'date_posted': 'May 31, 2019'
    },
    {
        'author': 'Omar Mnif',
        'title': 'Second Blog Post',
        'content': 'Second post content',
        'date_posted': 'May 30, 2019'
    }
]


@app.route("/home")
@app.route("/")
def home():
        return render_template("home.html", posts=posts)

@app.route("/about")
def about():
        return render_template("about.html", title='About')

if __name__ == "__main__":
    app.run(debug=True)
