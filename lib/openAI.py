import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
import requests

from lib.utils import get_data_path

# ---------- Load environment variables
load_dotenv(find_dotenv())
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL")


# print(f'Using OPENAI_API_KEY, {OPENAI_API_KEY}')


# ---------- Initialise the OpenAI client
def get_openai_client():
    return OpenAI(api_key=OPENAI_API_KEY)


def get_openai_model():
    return OPENAI_MODEL or "dall-e-2"


def generate_images(prompt: str, model=get_openai_model(), size="512x512", n=1) -> list[str]:
    client = get_openai_client()
    response = client.images.generate(
        model=model,
        prompt=input(prompt),
        size=size,
        # The n parameter specifies the number of images to generate
        n=n,
    )

    image_urls = []

    for image in response.data:
        print(image.url)
        image_url = image.url
        # Download the image and save it to the "data" directory
        image_data = requests.get(image_url).content

        with open(get_data_path() + f"generated_image_{image_urls.index(image_url)}.png", "wb") as f:
            f.write(image_data)

        image_urls.append(image_url)

    return image_urls


def run_chat_completion(messages):
    client = get_openai_client()
    model = get_openai_model()
    collected_messages = []
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        # collect the system messages
        collected_messages.append(chunk_message)

    return collected_messages
