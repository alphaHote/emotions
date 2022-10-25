
from flask import Flask, render_template
# import GLOBAL as g
app = Flask(__name__)

cache = {}
cache["i"]=0
cache["data"]=[
        ("01.01.20",2000),
        ("02.01.20",2010),
        ("03.01.20",2020),
        ("04.01.20",2100),
        ("05.01.20",2001),
        ("06.01.20",1000),
        ("07.01.20",1500),
        ("08.01.20",1800),
        ("09.01.20",2100),
        ("10.01.20",2050),
        ("11.01.20",1400),
        ("12.01.20",3000),
        ("13.01.20",2900)
    ]
cache["data"]=cache["data"]
la_suite_des_donnees=[
        ("13.01.20",2000),
        ("14.01.20",2010),
        ("15.01.20",2020),
        ("16.01.20",2100),
        ("17.01.20",2001),
        ("18.01.20",1000),
        ("19.01.20",1500),
        ("20.01.20",1800),
        ("21.01.20",2100),
        ("22.01.20",2050),
        ("23.01.20",1400),
        ("24.01.20",3000),
        ("25.01.20",2900)
    ]
cache["suite"]=la_suite_des_donnees


@app.route("/login")
def login():
    return render_template("form.html")



@app.route("/")
def home():
    labels_=[row[0] for row in cache["data"]]
    values_=[row[1] for row in cache["data"]]
    return render_template("graphe.html",labels=labels_,values=values_)



@app.route("/<int:val>/<string:date>",methods=('GET','POST'))
def home_(val,date):
    print(val)
    print(date)
    cache["data"].append((date,val))
    labels_=[row[0] for row in cache["data"]]
    values_=[row[1] for row in cache["data"]]
    return render_template("graphe.html",labels=labels_,values=values_)


@app.route('/envoyerMessage/<string:message>',methods=('GET','POST'))
def envoi_message(message):
    print(message)

    if cache["i"]<len(cache["suite"]):
        cache["data"].append(cache["suite"][cache["i"]])
        cache["i"]+=1
    else :
        cache["i"]
        cache["data"]=cache["suite"]

    labels_=[row[0] for row in cache["data"]]
    values_=[row[1] for row in cache["data"]]
    return render_template("graphe.html",labels=labels_,values=values_)





if __name__=="__main__":
    app.run()