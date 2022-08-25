import os
import sys
from PIL import Image

start_num = sys.argv[1]
home_dir = os.path.expanduser('~')
raw_target_dir = os.path.join(home_dir, 'Desktop/_Dev/labelme/examples/raw_imgs') # raw images
jpg_target_dir = os.path.join(home_dir, 'Desktop/_Dev/labelme/examples/custom') # jpg images
raw_list = os.listdir(raw_target_dir) # raw images list

# rename .heic into .jpg with counting number
# i = int(start_num)
# for heic in raw_list:
#     file_number = str(i).zfill(2)
#     ext_jpg = '.jpg'
#     if heic.endswith('.heic'):
#         os.rename(f'{raw_target_dir}/{heic}', f'{raw_target_dir}/in_{file_number}{ext_jpg}')
#         print(f'{heic} ==> {file_number}{ext_jpg}: Transfering... Success!')
#         i += 1
#     else:
#         print(f'{heic} ==> {file_number}{ext_jpg}: Transfering... Failed!')

# resize .jpg into 512x512