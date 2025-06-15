import base64

with open("img/zoom.png", "rb") as image_file:
    encoded = base64.b64encode(image_file.read()).decode()

print(encoded)
