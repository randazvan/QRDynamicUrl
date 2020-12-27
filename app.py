from flask import Flask, send_file
import pyqrcode as pq
import secondary_functions as sf

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/qrcode/<text>')
def text_qr_code(text):

    filename = sf.create_static_filepath()
    qrcode = pq.create(text)
    qrcode.png(filename, scale=10, module_color=sf.default_colour, background=sf.default_background)

    return send_file(filename)\


@app.route('/api/qrcode/<text>/<code_colour>/<background_colour>')
def text_colours_qr_code(text, code_colour, background_colour):

    #converting colours from hex to RGB
    hex_code_colour = sf.hex_to_rgb(code_colour)
    hex_background_colour = sf.hex_to_rgb(background_colour)
    filename = sf.create_static_filepath()
    qrcode = pq.create(text)
    qrcode.png(filename,
               scale=10,
               module_color=hex_code_colour if hex_code_colour else sf.default_colour,
               background=hex_background_colour if hex_background_colour else sf.default_background)

    return send_file(filename)


if __name__ == '__main__':
    app.run()
