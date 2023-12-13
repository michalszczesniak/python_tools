from os import getcwd, listdir
from cv2 import imread, hconcat, imwrite


def merge():
    
    path = getcwd()
    files = listdir(path)
    input_images = []
    for i, single_file in enumerate(files, 0):
        if single_file.endswith('.jpg') or single_file.endswith('.png'):
            input_images.append(imread(path+ '/' + files[i]))
    if input_images:  
        im_h = hconcat(input_images)
        imwrite('mergedimage.jpg', im_h)
    else:
        print('There are no files to merge')

if __name__ == '__main__':
        merge()
        
