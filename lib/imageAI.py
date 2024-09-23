from lib.openAI import generate_images, create_variations

def generate(prompt="Describe the image you want to generate: ", n=1):
    print("\n=======================================")
    print("Let's create an AI-powered image!")
    print("=======================================\n")
    generate_images(prompt=prompt, n=n)


def vary(image="generated_image_0.png", n=1):
    print("\n=======================================")
    print("Let's create a variation of an existing image!")
    print("=======================================\n")
    create_variations(image=image, n=n)