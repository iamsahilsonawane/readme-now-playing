import base64
import re

import requests


def build_medium_card(track, output):
    image = str(base64.b64encode(requests.get(
        track['album']['images'][1]['url']).content))[2: -1]
    output = re.sub(r"{{ image }}", image, output)

    duration = str(int(track['duration_ms'] / 1000))
    output = re.sub(r"{{ duration }}", duration, output)

    animation = "unset"
    if len(track['name']) <= 20:
        font_size = "24"
    else:
        animation = "text-scroll infinite linear 20s"
        font_size = "22"
    output = re.sub(r"{{ title_animation }}", animation, output)
    output = re.sub(r"{{ title_font_size }}", font_size, output)
    output = re.sub(r"{{ title }}", track['name'], output)

    animation = "unset"
    artists = ' & '.join([artist['name'] for artist in track['artists']])
    if len(artists) <= 29:
        font_size = "16"
    else:
        animation = "text-scroll infinite linear 20s"
        font_size = "12"
    ouptut = re.sub(r"{{ artist_animation }}", animation, output)
    output = re.sub(r"{{ artist_font_size }}", font_size, output)
    output = re.sub(r"{{ artist }}", artists, output)

    animation = "unset"
    album = track['album']
    if len(album['name']) <= 28:
        subtitle = album['name'] + ' • ' + album['release_date'].split('-')[0]
        font_size = "14"
    elif len(album['name']) <= 36:
        subtitle = album['name']
        font_size = "14"
    elif len(album['name']) <= 33:
        font_size = "12"
        subtitle = album['name'] + ' • ' + album['release_date'].split('-')[0]
    elif len(album['name']) <= 40:
        font_size = "12"
        subtitle = album['name']
    else:
        font_size = "12"
        subtitle = album['name']
        animation = "text-scroll infinite linear 20s"
    output = re.sub(r"{{ sub_animation }}", animation, output)
    output = re.sub(r"{{ sub_font_size }}", font_size, output)
    output = re.sub(r"{{ subtitle }}", subtitle, output)

    return output