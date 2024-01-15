import random
import base64

def generate_captcha():
    # Generate random number
    num = random.randint(100000, 999999)

    # Encode number to base64
    encoded_num = base64.b64encode(str(num).encode())

    # Cut the encoded number by 10 characters from the left
    captcha = encoded_num[:10].decode()

    return captcha


def main():
    # Generate captcha
    captcha = generate_captcha()

    # Display captcha
    print("Masukkan Captcha: ")
    print(captcha)

    # Get user input
    user_input = input()

    # Check if user input is correct
    if user_input == captcha:
        print("Captcha benar!")
    else:
        print("Captcha salah!")


if __name__ == "__main__":
    main()
