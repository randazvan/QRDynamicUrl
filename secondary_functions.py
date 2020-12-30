from datetime import datetime
import pyqrcode as pq
from flask import send_file
import os
import ast


# Default variables of the QR code
default_colour = '000000'
default_background = 'ffffff'
default_qr_version = 6
default_qr_error = 'M'
default_png_scale = 10


# Get the current time in milliseconds
def get_current_dt_in_millisec():
    dt_obj = datetime.now()

    millisec = int(dt_obj.timestamp())

    return millisec


# Creating the static file to save the QR code
def create_static_filepath(file_type='png'):
    return os.path.join(os.path.dirname(__file__), 'qrcodes/') + str(get_current_dt_in_millisec()) + "." + file_type


# Transform HEX colour from URL in RGB with transparency variable
def hex_to_rgb(hex_colour, transparency=255):
    hex_colour = hex_colour.replace("'", "")
    if len(hex_colour) == 6:
        rgb = [int(hex_colour[i:i+2], 16) for i in (0, 2, 4)]
        rgb.append(transparency)
        return rgb
    else:
        return None


# Transform HEX colour from URL in RGB without transparency variable
def hex_to_rgb_no_transparency(hex_colour):
    hex_colour = hex_colour.replace("'", "")
    if len(hex_colour) == 6:
        rgb = [int(hex_colour[i:i+2], 16) for i in (0, 2, 4)]
        return rgb
    else:
        return None


# creating a text qr code
def create_text_qr_code(text,
                        background_colour=default_background,
                        qr_error=default_qr_error,
                        qr_version=default_qr_version,
                        vcard=0):

    # check if we need to create VCARD data
    if vcard == 1:
        text = vcard_data_preparation(text)
        qr_version = 6

    # image destination file
    filename = create_static_filepath()

    # Change HEX to RGB colour
    hex_background_colour = hex_to_rgb(background_colour)

    # create the QR code
    qrcode = pq.create(text, error=qr_error, version=qr_version)
    qrcode.png(filename, scale=default_png_scale, module_color=default_colour, background=hex_background_colour)

    return send_file(filename)


# Checking the VCARD data
def vcard_data_preparation(text):

    text.replace("'", '"')

    vcard = {}
    vcard['BEGIN'] = 'VCARD'
    vcard.update(ast.literal_eval(text))
    vcard['END'] = 'VCARD'

    print(vcard)
    vcard_text = ''

    for key, value in vcard.items():
        vcard_text += key + ':' + value + '\n'

    print(vcard_text)

    return vcard_text

