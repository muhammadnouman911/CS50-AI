IMAGE_EXTENSIONS = ("gif", "jpg", "jpeg", "png")
APPLICATION_EXTENSIONS = ("pdf", "zip")
PLAIN_EXTENSIONS = ("txt",)


def main():
    file_name = input("File name: ").strip().lower()

    print(check_extension(file_name))


def check_extension(file):
    for extension in (IMAGE_EXTENSIONS + APPLICATION_EXTENSIONS + PLAIN_EXTENSIONS):
        if file.endswith(f".{extension}"):
            if extension in IMAGE_EXTENSIONS:
                extension = extension if extension != "jpg" else "jpeg"
                return f"image/{extension}"
            elif extension in APPLICATION_EXTENSIONS:
                return f"application/{extension}"
            else:
                return f"text/plain"

    return "application/octet-stream"


main()