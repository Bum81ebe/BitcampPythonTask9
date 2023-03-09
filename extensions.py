# Formats #files


text = input("tell me your file name and format ")

if text.endswith(".jpg") or text.endswith(".jpeg"):
    print("image/jpg")
elif text.endswith(".gif"):
    print("image/gif")
elif text.endswith(".png"):
    print("image/png")
elif text.endswith(".pdf"):
    print("application/pdf")
elif text.endswith(".txt"):
    print("application/txt")
elif text.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")