import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
import requests

from lib.utils import get_data_path, get_generations_path

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

    return handle_generated_images(response, prefix="generated_image_")


def create_variations(image: str, model=get_openai_model(), size="1024x1024", n=1) -> list[str]:
    client = get_openai_client()
    response = client.images.create_variation(
        model=model,
        image=open(get_data_path() + image, "rb"),
        size=size,
        # The n parameter specifies the number of images to generate
        n=n,
    )

    return handle_generated_images(response, prefix="image_variation_")


def edit_image(prompt: str, image: str, mask: str, model=get_openai_model(), size="512x512", n=1) -> list[str]:
    client = get_openai_client()
    response = client.images.edit(
        model=model,
        image=open(get_data_path() + image, "rb"),
        mask=open(get_data_path() + mask, "rb"),
        prompt=input(prompt),
        size=size,
        # The n parameter specifies the number of images to generate
        n=n,
    )

    return handle_generated_images(response, prefix="edited_image_")


def handle_generated_images(response, prefix="generated_image_"):
    image_urls = []

    for image in response.data:
        print(image.url)
        image_url = image.url
        image_urls.append(image_url)
        # Download the image and save it to the "data" directory
        image_data = requests.get(image_url).content

        try:
            with open(get_generations_path() + f"{prefix}{image_urls.index(image_url)}.png", "wb") as f:
                f.write(image_data)
        except Exception as e:
            print(f"Error saving image: {e}")

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
