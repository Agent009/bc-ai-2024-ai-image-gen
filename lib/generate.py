from lib.openAI import generate_images

def generate():
    print("\n=======================================")
    print("Let's create an AI-powered image!")
    print("=======================================\n")
    generate_images(prompt="Describe the image you want to generate: ", n=1)