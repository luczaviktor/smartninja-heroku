from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    filmek=[egy, ketto, harom]
    return render_template("table.html", filmek = filmek)

class filmek():
    def __init__(self, cim, leiras, IMDB):
        self.cim = cim
        self.leiras = leiras
        self.IMDB = IMDB

egy = filmek("A vezércsel",
              "Orphaned at the tender age of nine, prodigious introvert Beth Harmon discovers and masters the game of chess in 1960s USA. But child stardom comes at a price.",
              "https://www.imdb.com/title/tt10048342/?ref_=hm_fanfav_tt_1_pd_fp1")
ketto = filmek("Amerika kapitány: Az első bosszúálló",
                 "Steve Rogers, a rejected military soldier, transforms into Captain America after taking a dose of a Super-Soldier serum. But being Captain America comes at a price as he attempts to take down a war monger and a terrorist organization.",
                 "https://www.imdb.com/title/tt0458339/?ref_=nv_sr_srsg_0")
harom = filmek("Batman - A denevérember (1989)",
                  "The Dark Knight of Gotham City begins his war on crime with his first major enemy being Jack Napier, a criminal who becomes the clownishly homicidal Joker.",
                  "https://www.imdb.com/title/tt0096895/?ref_=nv_sr_srsg_7")

if __name__ == '__main__':
    app.run()