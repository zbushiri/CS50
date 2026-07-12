# Asks user for file name
fname = input("File name: ").strip().lower()
# Print depending on file name
if fname.endswith(".pdf"):
    print("application/pdf")
elif fname.endswith(".png"):
    print("image/png")
elif fname.endswith((".jpg", ".jpeg")):
    print("image/jpeg")
elif fname.endswith(".gif"):
    print("image/gif")
elif fname.endswith(".txt"):
    print("text/plain")
elif fname.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")