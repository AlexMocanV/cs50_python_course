x = input("FILE name: ")
x = x.strip().split(".")
# dict [str, str]
extensions = {
    "gif": "image/gif", 
    "jpg": "image/jpeg", 
    "png": "image/png", 
    "jpeg" : "image/jpeg",
    "pdf": "application/pdf",
    "txt": "text/plain", 
    "zip": "application/zip"
    }

# get (key, default) returns the value for key if key is in the dictionary, else default. 
# If default is not given, it defaults to None, so that this method never raises a KeyError.
print(extensions.get(x[-1].lower(), "application/octet-stream"))
