#ImageCopyEx.py
#U Must have Source Image--must opened in Read Mode with binary Format
#decide Destination Image--must opened in Write Mode with binary Format
def imagecopy(srcfile,dstfile):
    try:
        with open(srcfile,"rb") as rp:
            with open(dstfile,"wb") as wp:
                imgdata=rp.read()
                wp.write(imgdata)
                print("Image Copied---Verify")
    except FileNotFoundError:
        print("Source Image does not Exist")

#Main Program
imagecopy("kvr.png","kvpython.png")