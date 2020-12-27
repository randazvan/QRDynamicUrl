from datetime import datetime

default_colour = [0, 0, 0, 128]
default_background = [255, 255, 255]

def get_current_dt_in_millisec():
    dt_obj = datetime.strptime('20.12.2016 09:38:42,76',
                               '%d.%m.%Y %H:%M:%S,%f')
    millisec = dt_obj.timestamp()

    return millisec


def create_static_filepath(file_type='png'):
    return "qrcodes/" + str(get_current_dt_in_millisec()) + "." + file_type


def hex_to_rgb(hex_colour, transparency=255):
    hex_colour = remove_string_char(hex_colour)
    if(len(hex_colour) == 6):
        rgb = [int(hex_colour[i:i+2], 16) for i in (0, 2, 4)]
        rgb.append(transparency)
        return rgb
    else:
        return None


def hex_to_rgb_no_transparency(hex_colour):
    hex_colour = remove_string_char(hex_colour)
    if (len(hex_colour) == 6):
        rgb = [int(hex_colour[i:i+2], 16) for i in (0, 2, 4)]
        return rgb
    else:
        return None

def remove_string_char(string):
    return string.replace("'", "")

