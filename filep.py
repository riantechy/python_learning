try:
    stream = open("C:\Users\bchirchir\Documentsile.txt", "rt")
    # Processing goes here.
    stream.close()
except Exception as exc:
    print("Cannot open the file:", exc)