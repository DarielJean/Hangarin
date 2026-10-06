from PIL import Image, ImageDraw, ImageFont

def make_icon(size, filename):
    img = Image.new('RGB', (size, size), color='#1d3557')
    draw = ImageDraw.Draw(img)
    text = "H"
    try:
        font = ImageFont.truetype("arial.ttf", int(size * 0.5))
    except:
        font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), text, font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((size - w) / 2, (size - h) / 2 - bbox[1]), text, fill="white", font=font)
    img.save(filename)

make_icon(192, 'static/img/icon-192.png')
make_icon(512, 'static/img/icon-512.png')
print("Icons created successfully.")