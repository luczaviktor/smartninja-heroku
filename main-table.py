from flask import Flask, render_template, request, make_response

app = Flask(__name__)

class Filmek():
    def __init__(self, cim, leiras, IMDB):
        self.cim = cim
        self.leiras = leiras
        self.IMDB = IMDB

egy = Filmek("A vezércsel",
              "Orphaned at the tender age of nine, prodigious introvert Beth Harmon discovers and masters the game of chess in 1960s USA. But child stardom comes at a price.",
              "https://www.imdb.com/title/tt10048342/?ref_=hm_fanfav_tt_1_pd_fp1")
ketto = Filmek("Amerika kapitány: Az első bosszúálló",
                 "Steve Rogers, a rejected military soldier, transforms into Captain America after taking a dose of a Super-Soldier serum. But being Captain America comes at a price as he attempts to take down a war monger and a terrorist organization.",
                 "https://www.imdb.com/title/tt0458339/?ref_=nv_sr_srsg_0")
harom = Filmek("Batman - A denevérember (1989)",
                  "The Dark Knight of Gotham City begins his war on crime with his first major enemy being Jack Napier, a criminal who becomes the clownishly homicidal Joker.",
                  "https://www.imdb.com/title/tt0096895/?ref_=nv_sr_srsg_7")
filmek = [egy, ketto, harom]

@app.route("/")
def index():
    return render_template("table.html")

user_dict = {}

def cvs():
    with open("felhasznalo.csv", 'r') as user_file:
        content = user_file.read().splitlines()
        for row in content:
            (username, pwd) = row.split(",")
            user_dict[username] = pwd
        return user_dict

def cvs_iras(username, password):
    with open("felhasznalo.csv", 'a+') as user_file:
        content = user_file.read().splitlines()
        for row in content:
            (name, pwd) = row.split(",")
            user_dict[name] = pwd
        if username is None:
            pass
        else:
            user_dict.update({username: password})
        user_file.write(str("\n" + username + "," + password))

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username in user_dict:
        if user_dict[username] == password:
            response = make_response(render_template("table.html", filmek = filmek, name = username))
            response.set_cookie("user_name", username)
    else:
        response = render_template("table.html")

    return response

@app.route("/logout", methods=["POST"])
def logout():
    response = make_response(render_template("table.html"))
    response.set_cookie("user_name", expires=0)
    return response

@app.route("/regisztracio", methods=["POST"])
def regisztracio():
    username = request.form.get("username")
    password = request.form.get("password")
    cvs_iras(username, password)
    message = "Sikeresen regisztrált oldalunkon. Most már bejelentkezhet."

    response = make_response(render_template("table.html", message=message))

    return response

@app.route("/regisztracio-oldal", methods=["GET"])
def regisztracio_oldal():
    response = make_response(render_template("regisztracio.html"))

    return response

if __name__ == '__main__':
    app.run()