import requests
import string
import random
from PIL import Image
from io import BytesIO
from secret_guide.settings import MEDIA_ROOT, STATIC_ROOT


def id_generator(size=20, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def paste_watermark_on_image(image_url: str, quest_type: str):
    try:
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))

        watermark = Image.open(
            f"{STATIC_ROOT}/quest/img/CARD_{quest_type}.png")

        new_height = int(img.height * 0.15)
        new_width = int(watermark.width * (new_height / watermark.height))

        watermark = watermark.resize(tuple([new_width, new_height]))
        x = img.width // 2 - watermark.width // 2
        y = img.height - watermark.height - 10
        img.paste(watermark, (x, y),  watermark)

        path = f"cards/card{id_generator()}.png"
        img.save(f"{MEDIA_ROOT}{path}")

        return path

    except Exception as err:
        print(f"{err=}")
        return None


# handle('{"url": "https://files.salebot.pro/uploads/message_files/bf91d2e5-d15b-416d-852a-a15b9922e420.jpg"}')
