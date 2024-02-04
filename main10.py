from flask import Flask, render_template, request
import spacy

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analizuj', methods=['POST'])
def analizuj():
    tekst = request.form['tekst']
    dokument = nlp(tekst)
    sentyment = sum([token.sentiment for token in dokument]) / len(dokument)

    if sentyment > 0:
        wynik = "Pozytywny"
    elif sentyment < 0:
        wynik = "Negatywny"
    else:
        wynik = "Neutralny"

    return render_template('wynik.html', tekst=tekst, sentyment=wynik)

if __name__ == '__main__':
    app.run(debug=True)
