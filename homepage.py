from flask import Flask, render_template, request
import random
from songListGenerator import songListGenerator
from spotifyAuthoriser import SpotifyAuthoriser
from movieListGenerator import movieListGenerator
from bookListGenerator import bookListGenerator
import cgi

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("homepage.html")

# -------------- MUSIC PAGES ------------- #


@app.route("/music/")
def music_page():
    return render_template("music_page_1.html")


@app.route("/music/generated_list/", methods=["GET", "POST"])
def music_page_2():
    global mood_selected
    global generated_list

    if request.method == "POST":
        mood_selected = request.form.get("mood")
        print(f"Selected Mood: {mood_selected}")

        listGenerator = songListGenerator(mood_selected)
        generated_list = listGenerator.generate_list()
        print(generated_list)

        return render_template("music_page_2.html", generated_list=generated_list)

    mood_selected = request.args.get("mood", default="")
    if mood_selected:
        listGenerator = songListGenerator(mood_selected)
        generated_list = listGenerator.generate_list()
    else:
        generated_list = []

    return render_template("music_page_2.html", generated_list=generated_list)


@app.route("/music/generated_list/connect_spotify/", methods=["GET", "POST"])
def music_page_3():
    if request.method == "GET":
        print("\nInside if")
        global username
        username = request.args.get("spotify_username")
    print("\nbefore return")
    return render_template("music_page_3.html")


@app.route("/music/generated_list/connect_spotify/complete")
def music_page_4():
    global generated_list
    username = "kh8lr0m9qqxobjc5cdyglki5z"
    print(f"\nUsername: {username}\n")

    connect_spotify = SpotifyAuthoriser(user=username)
    return render_template("music_page_4.html")

# -------------- MOVIES PAGES ------------- #


@app.route("/movies/")
def movies_page_1():
    return render_template("movies_page_1.html")


@app.route("/movies/generated_list/", methods=["GET", "POST"])
def movies_page_2():
    global mood_selected
    global generated_list

    if request.method == "POST":
        mood_selected = request.form.get("mood")
        print(f"Selected Mood: {mood_selected}")

        listGenerator = movieListGenerator(mood_selected)
        generated_list = listGenerator.generate_list()

        return render_template("movies_page_2.html", generated_list=generated_list)

    mood_selected = request.args.get("mood", default="")
    if mood_selected:
        listGenerator = movieListGenerator(mood_selected)
        generated_list = listGenerator.generate_list()
    else:
        generated_list = []

    return render_template("movies_page_2.html", generated_list=generated_list)


# -------------- BOOKS PAGES ------------- #


@app.route("/books/")
def books_page_1():
    return render_template("books_page_1.html")


@app.route("/books/generated_list/", methods=["GET", "POST"])
def books_page_2():
    global mood_selected
    global generated_list

    if request.method == "POST":
        mood_selected = request.form.get("mood")
        print(f"Selected Mood: {mood_selected}")

        listGenerator = bookListGenerator(mood_selected)
        generated_list = listGenerator.generate_list()

        return render_template("books_page_2.html", generated_list=generated_list)

    mood_selected = request.args.get("mood", default="")
    if mood_selected:
        listGenerator = bookListGenerator(mood_selected)
        generated_list = listGenerator.generate_list()
    else:
        generated_list = []

    return render_template("books_page_2.html", generated_list=generated_list)


if __name__ == "__main__":
    app.run(debug=True)


# -------------- HOMEPAGE ------------- #

# @app.route("/home")
# def homepage():
#     return render_template("homepage.html")


# @app.route("/music/generated_list/")
# def music_page_2():
#     global generated_list
#     listGenerator = songListGenerator(mood_selected)
#     generated_list = listGenerator.generate_list()
#     return render_template("music_page_2.html")


# @app.route("/music/generated_list/", methods=["GET"])
# def music_page_23():
#     global mood_selected
#     # global generated_list

#     mood_selected = request.form.get("mood")
#     print(f"Selected Mood: {mood_selected}")

#     # listGenerator = songListGenerator(mood_selected)
#     # generated_list = listGenerator.generate_list()

#     return render_template("music_page_2.html", generated_list=generated_list)

#     # return redirect("/music/generated_list/result")

# @app.route("/movies/generated_list/")
# def movies_page_2():
#     listGenerator = movieListGenerator(mood_selected)
#     list = listGenerator.generate_list()
#     return render_template("movies_page_2.html")


# @app.route("/books/generated_list/")
# def books_page_2():
#     listGenerator = bookListGenerator(mood_selected)
#     list = listGenerator.generate_list()
#     return render_template("books_page_2.html")
