from flask import Flask, request, render_template

app = Flask(__name__)
x=0
text=""

def write_txt( txt):
    with open("data.txt", 'a', encoding='utf-8') as fos:
        fos.write(txt+'\n')

def read_txt(path):
    txt=""
    with open(path, 'r', encoding='utf-8') as fis:
        for line in fis.readlines():
            txt+=line+"\n"
    return txt 

@app.route('/')
def home():
    return render_template('aa.html')

@app.route('/aa')
def joie():
    return render_template('aa.html')

@app.route('/ab')
def colere():
    return render_template('ab.html')


@app.route('/ac')
def peur():
    return render_template('ac.html')

@app.route('/ad')
def tristesse():
    return render_template('ad.html')


@app.route('/ae')
def surprise():
    return render_template('ae.html')

@app.route('/af')
def degout():
    return render_template('af.html')

@app.route('/soumission', methods=['POST'])

def get_text():
    global x
    global text
    #print(type(request.form))
    for it in list(request.form.listvalues()):
        text+=it[0]
    write_txt("<h5>"+text+"</h5>")
    text=""
    return "roger that"

@app.route('/housni_aataoui_aime_beaucoup_nono' )
def recuperer_data():
    ss=read_txt("data.txt")
    return ss

if __name__=='__main__':
    # uvicorn.run("application:app")#, host="127.0.0.1", port=5000, log_level="info")
    app.run()

