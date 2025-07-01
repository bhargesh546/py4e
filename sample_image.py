import urllib.request, urllib.parse, urllib.error

img = 'https://media.istockphoto.com/id/814423752/photo/eye-of-model-with-colorful-art-make-up-close-up.jpg?s=612x612&w=0&k=20&c=l15OdMWjgCKycMMShP8UK94ELVlEGvt7GmB_esHWPYE='

image = urllib.request.urlopen(img)
fhandle = open('image1.jpg', 'wb')

size = 0
while True:
    info = image.read(10000)
    if (len(info) < 1):
        break
    size += len(info)
    fhandle.write(info)

print(f"Number of characters in the file are: {size}")
fhandle.close()