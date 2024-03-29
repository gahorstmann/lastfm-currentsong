import requests
import json
import base64

    
def get_image_lastfm(url) -> bytes:
    response = requests.get(url)
    content = response.text
    if response.status_code != 200:
        return ""
    if "thumbor call failed" in content:
        return ""
    return response.content

def get_image(data: json) -> str:
    data.sort(key=lambda x: x["size"])
    for image in data:
        image_byte = get_image_lastfm(image["#text"])
        if image_byte != "":
            encoded_string = base64.b64encode(image_byte)
            format = image["#text"].split(".")[-1]
            data_image = f"data:image/{format};base64," + encoded_string.decode("utf-8")
            return data_image
