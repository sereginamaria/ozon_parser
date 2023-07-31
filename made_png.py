from PIL import Image


def main():
    new_img = Image.new('RGB', (1024, 1280), 'blue')
    new_img.show()


if __name__ == "__main__":
    main()
