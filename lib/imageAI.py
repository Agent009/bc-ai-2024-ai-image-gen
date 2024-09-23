from lib.openAI import generate_images, create_variations, edit_image

def generate(prompt="Describe the image you want to generate: ", n=1):
    print("\n=======================================")
    print("Let's create an AI-powered image!")
    print("=======================================\n")
    generate_images(prompt=prompt, n=n)


def vary(image="Coconut.png", n=1):
    print("\n=======================================")
    print("Let's create a variation of an existing image!")
    print("=======================================\n")
    create_variations(image=image, n=n)


def edit(prompt="Describe the image you want the mask to be replaced with: ", image="Coconut.png", mask="Mask.png", n=1):
    print("\n=======================================")
    print("Let's create a variation of an existing image!")
    print("=======================================\n")
    edit_image(prompt=prompt, image=image, mask=mask, n=n)