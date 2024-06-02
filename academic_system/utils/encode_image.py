import base64

def generate_encoded_image(image_path: str):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()

    return encoded_image