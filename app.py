from flask import Flask, render_template
import secondary_functions as sf

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/api/qrcode/text/<text>')
def text_qr_code(text):

    return sf.create_text_qr_code(text)


@app.route('/api/qrcode/text/<text>/<background_colour>')
def text_colours_qr_code(text, background_colour):

    return sf.create_text_qr_code(text, background_colour)


@app.route('/api/qrcode/vcard/<text>')
def vcard_qr_code(text):

    return sf.create_text_qr_code(text, vcard=1)


@app.route('/api/qrcode/vcard/<text>/<background_colour>')
def vcard_colours_qr_code(text, background_colour):

    return sf.create_text_qr_code(text, background_colour, vcard=1)


if __name__ == '__main__':
    app.run()
