import xml.etree.ElementTree as ET
import cv2
import numpy
import os.path
from os import walk
file_count = 6095
chapter_name = "Arisa"
tree = ET.parse('data_set/xml/'+chapter_name+'.xml')
root = tree.getroot()

for pages in root.findall('pages'):

    for page in pages:
        # for face in page:
        #     print(face.attrib)
        #     print(face.get('xmin'))
        #     exit()
        page_number = page.get('index')
        file_name = str(page_number)
        len_fname = len(file_name)

        if len_fname == 1:
            image_name = str('00')+file_name+".jpg"
        elif len_fname == 3:
            image_name = file_name+".jpg"
        else:
            image_name = str('0')+file_name+".jpg"

        image_path = "data_set/images/"+chapter_name+"/"+image_name

        count = 0
        for face in page:
           if face.tag == "face":
                count = count +1
                xmin = face.get('xmin')
                ymin = face.get('ymin')
                xmax = face.get('xmax')
                ymax = face.get('ymax')
                xmn = int(xmin)
                xmx = int(xmax)
                ymn = int(ymin)
                ymx = int(ymax)
                img1 = cv2.imread(image_path, 0)

                cropped = img1[ymn:ymx, xmn:xmx]

                #rectangle = cv2.rectangle(img1, (xmn, ymn), (xmx, ymx), (255, 0, 0), 2)

                file_name = image_name.replace(".jpg", "")
                #filename is image number
                #save_crop to file_crop
                file_crop = file_name+"-"+str(count)+".jpg"

                file_count = file_count + 1
                save_path = "data_set/face/"+str(file_count)+".jpg"


                cv2.imwrite(save_path, cropped)

                #cv2.imshow("show",rectangle)
                #k = cv2.waitKey(0)
                #exit()








