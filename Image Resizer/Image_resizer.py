import cv2

p=input("Enter the photo name: ")
source = p + ".jpg"
destination = 'newImage.png'


src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

if src is None:
    print(f"Unable to read the image from {source}")
else:
    
    scale_percent = 50

 
    new_width = int(src.shape[1] * scale_percent / 100)
    new_height = int(src.shape[0] * scale_percent / 100)

    output = cv2.resize(src, (new_width, new_height))

    if cv2.imwrite(destination, output):
        print(f"Image resized successfully and saved to {destination}")
    else:
        print("Error: Unable to save the resized image")
    