from PIL import Image


def load_image(image_file):
    img = Image.open(image_file)
    img.load()
    if img.mode == "RGBA":
        background = Image.new("RGB", img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[3])
        img = background
        print("Converted RGBA to RGB")
    elif img.mode != "RGB":
        img = img.convert("RGB")
        print(f"Converted {img.mode} to RGB")
    else:
        print("Normal")
    return img
