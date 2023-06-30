def main():
    ext = input("File name: ").strip(' ').lower()

    if is_ext(ext) == True:
        ext = ext.split('.')

    nb_ext = -1
    for i in ext:
        nb_ext += 1

    match ext[nb_ext]:
        case "gif" | "png" :
            return(print(f"image/{ext[nb_ext]}"))
        case "jpg" | "jpeg" :
            return(print("image/jpeg"))
        case "pdf" | "zip" :
            return(print(f"application/{ext[nb_ext]}"))
        case "txt":
            return(print("text/plain"))

    return(print("application/octet-stream"))


def is_ext(ext):
    for c in ext:
        if c == '.':
            return True
    return False


main()