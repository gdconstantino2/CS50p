x = input("File name: ")

#images
if (x.lower().strip().endswith(".jpeg")) or (x.lower().strip().endswith(".jpg")):
    print("image/jpeg")
elif (x.lower().strip().endswith(".gif")):
    print("image/gif")
elif (x.lower().strip().endswith(".png")):
    print("image/png")
#application
elif (x.lower().strip().endswith(".pdf")):
    print(f"application/pdf")
elif (x.lower().strip().endswith(".zip")):
    print(f"application/zip")
#text
elif (x.lower().strip().endswith(".txt")):
    print(f"text/plain")
#others
else:
    print("application/octet-stream")
