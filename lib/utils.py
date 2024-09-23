import torch


def get_data_path():
    return "./data/"


def get_generations_path():
    return "./generated/"


def multiline_input(prompt: str) -> str:
    """
    Captures multi-line user input. Input is terminated by pressing ENTER twice.
    :param prompt: The prompt asking for user input
    :return: The multiline user input
    """
    print(prompt)  # Display the prompt once
    lines = []

    while True:
        line = input()  # No need to show the prompt again
        if line == "":
            break
        lines.append(line)

    user_input = "\n".join(lines)
    return user_input


def check_cuda():
    """
    This function checks the availability and details of CUDA and GPU for PyTorch.

    It prints the following information:
    1. The CUDA version that PyTorch is using.
    2. Whether a GPU is available for PyTorch.
    3. The name of the GPU if available, otherwise, it prints "No GPU detected".

    Parameters:
    None

    Returns:
    None
    """
    print(f"CUDA version that PyTorch is using: {torch.version.cuda}")
    print(f"GPU is available for PyTorch? {torch.cuda.is_available()}")
    print("GPU if available: " + torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU detected")
