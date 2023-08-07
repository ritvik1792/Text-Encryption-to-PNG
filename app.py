import time
from flask import Flask, render_template, request
import convertionOfMsgToAsciiImg
import gettingRandomImage
import generatingPrivateKey
import encryption

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
@app.route('/', methods=['GET'])

def getText():
    text = request.form['input_text']
    convertionOfMsgToAsciiImg.writeToFile(text)
    #generating the ascii img
    convertionOfMsgToAsciiImg.comtai()
    #getting a random image
    gettingRandomImage.gri()
    #generating a private key
    generatingPrivateKey.gpk()
    #encryption
    encryption.encr()
    time.sleep(5)
    return render_template('output.html', p="../enc.png")

if __name__ == '__main__':
    app.run(debug=True)


