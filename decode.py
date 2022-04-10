import cv2
from PIL import Image
import streamlit as st
from common import countpixels, generaterandom, randomnumber, msgtobin, numtobin
def decode(fname,key):
    #Function to perform decoding
    st.write("Decoding Image!!!Please Wait....")
    decbin=""#Empty string to store binary equivalent of the encoded data.
    ans=""#Empty string to store the actual encoded data
    img=cv2.imread(fname)#Opening the image file
    c=0
    
    pos=generaterandom.generaterandom(key)#Generating the first random number using the key
    for row in img:#Iterating through rows of an image
        for pix in row:#Iterating through the pixels of a row
            
                if c==pos:
                    r=numtobin.numtobin(pix[0])
                    g=numtobin.numtobin(pix[1])
                    b=numtobin.numtobin(pix[2])
                    decbin=decbin+r[-1]+g[-1]+b[-1]#Extracting LSBs from R,G,B Values of the pixel
                    key=pos
                    pos=generaterandom.generaterandom(key)


                c+=1
    all_bytes = [ decbin[i: i+8] for i in range(0, len(decbin), 8) ]#Split the binary string to get substrings of 8 characters
    for i in all_bytes:
        if chr(int(i,2))=="$":#Breaking out of loop if the special end charcter is found
            break
        ans+=chr(int(i,2))
        
    if ans[0:3]!="!@#":#Checking if the special starting characters are found
        st.write("Image not encoded using the software")
    else:  
      st.write("The Hidden Data is ")#Displayingthe hidden data
      st.write(ans[3:])
    print(ans)
    
