import cv2
from PIL import Image
import streamlit as st
from common import countpixels, generaterandom, randomnumber, msgtobin, numtobin
def encode(fname,data,key):
    #Function to carry out encoding process
    img=cv2.imread(fname)#Opening the image
    
    binstr=msgtobin.msgtobin(data)#Converting the secret message to it's binary equivalent
    
    if len(binstr)>((img.shape[0]*img.shape[1]*3)):#Checking if image has sufficient pixels to encode the image.
        st.error("Small image size.Please encode small data or provide a big image")
    
   
    else:
        st.write("Encoding Image!!!Please Wait.....")
        blen=len(binstr)
        encpos=randomnumber.randomnumber((blen//3)+1,key)#Generating a list of random numbers.
        ind=0
        c=0
        
        if max(encpos)>=countpixels.countpixels(fname):#Checking if the there are sufficient random pixels to encode the data
            st.error("Pixels not sufficient.Choose another key.")
            return
        
        
        
        for row in img:#Iterating through rows of an image
            for pix in row:#Iterating through the pixels of a row

                if ind<blen and c in encpos:#Encoding in red value of the pixel
                    rval=numtobin.numtobin(pix[0])
                    pix[0]=int(rval[:-1]+binstr[ind],2)
                    ind+=1
                
                if ind<blen and c in encpos:#Encoding in the green value of pixel
                    gval=numtobin.numtobin(pix[1])
                    pix[1]=int(gval[:-1]+binstr[ind],2)
                    ind+=1

                if ind<blen and c in encpos:#Encoding in the blue value of the pixel.
                    bval=numtobin.numtobin(pix[2])
                    pix[2]=int(bval[:-1]+binstr[ind],2)
                    ind+=1

                if ind>=blen:#Breaking out the loop if all the bits in the binary data are encoded.
                    
                    break

                c+=1
        
              





             
        cv2.imwrite("enc.png",img)#Storing the encoded image in CWD
        st.write("Image stored in current directory")
