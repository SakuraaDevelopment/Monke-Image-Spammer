import requests #for downloading the file to your computer
import shutil #for downloading the file to your computer
import random #for random name
import os #for moving files and renaming them
from pathlib import Path #for finding the current file location

FilePath = Path(__file__).absolute()
DirPath = Path().absolute()

print("Started Monke Image Spammer")
for x in range(4000): #repeat 4000 times (around 1gb
    rnumber = random.randrange(1,999999999999999999999999999999999999999999999999999999) #chooses name 1-99999ect
    image_url = "https://pngimg.com/uploads/monkey/monkey_PNG18729.png" #gets image url
    filename = image_url.split("/")[-1]

    r = requests.get(image_url, stream=True)

    if r.status_code == 200:
        r.raw.decode_content = True

        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

        print('Monke: ', filename) #Shows when sucsessfully downloaded
        os.rename(r'{}\monkey_PNG18729.png'.format(DirPath), r'{}\monke\{}monke.png'.format(DirPath, rnumber)) #renames and moves to monke folder
    else:
        print('Monke Couldn\'t be downloaded! Check your internet.') #Shows when failed to download