import os

current_dir = os.path.dirname(__file__)

css_path = os.path.join(current_dir, '..', 'assets', 'css', 'global.css')

def get_image_path(filename: str):
    return os.path.join(current_dir, '..', 'assets', 'images', filename)
