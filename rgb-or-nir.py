"""
Classify images into RGB or NIR.
Take a folder of mixed images, then 
- copy images detected as `RGB` into folder `./rgb/`
- copy images detected as `NIR` into folder `./nir/`
"""

def RGB_or_NIR(img):
    """
    Take an image array of HSV, return `answer` of either `RGB` or `NIR`.
    """
    ansewr = None
    
    if img[:,:,0].sum() == 0 and img[:,:,1].sum() == 0 and img[:,:,2].sum() > 0 :
        answer = 'NIR'
    else:
        answer = 'RGB'
        
    return answer

def classify_rgb_or_nir(inpath):
    import cv2
    import glob
    import shutil

    for fname in glob.glob(inpath + '*.jpg'):
        #print(fname)
        img = cv2.imread(fname)
        
        if img is None:
            print('Failed to load image file: ', fname)
            #sys.exit(1)
            pass
        
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            
            # classify into `RGB` or `NIR`
            answer = RGB_or_NIR(img)
            
            if answer == 'RGB':
                #print('move ' + fname, ' to RGB folder', answer)
                shutil.copy(fname, inpath + 'rgb/')

                
            elif answer == 'NIR':
                #print('move ' + fname, ' to NIR folder', answer)
                shutil.copy(fname, inpath + 'nir/')
    return

if __name__ == "__main__":

    import os
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_path", required=True, help="Path to image folder")
    args = vars(parser.parse_args())

    # check for valid folder
    if os.path.exists(args['input_path']):
        
        # classify image into RGB or NIR
        classify_rgb_or_nir(args['input_path'])

    else: 
        print(args['input_path'], ' invalid.')

        