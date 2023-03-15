import os
import sys
import glob
import pyheif
from PIL import Image

my_name = sys.argv[1]
start_num = int(sys.argv[2])
home_dir = os.path.expanduser('~')
raw_target_dir = os.path.join(home_dir, 'Downloads') # raw images
jpg_target_dir = os.path.join(home_dir, 'Desktop/_dev/labelme/examples/custom') # jpg images
heic_list = [glob.glob(e) for e in [os.path.join(raw_target_dir, '*.heic'), os.path.join(raw_target_dir, '*.HEIC')]]
ext_jpg = '.jpg'

def flatten_list():
  list = []
  for i in heic_list:
    for j in i:
      list.append(j)
  return list

list = flatten_list()

for heic in list:
    heic_base_name = os.path.basename(heic)
    transfered_name = f'n_{my_name}_{str(start_num).zfill(2)}{ext_jpg}'
    jpg_file = os.path.join(jpg_target_dir, transfered_name)
    heif_file = pyheif.read(heic)
    img = Image.frombytes(
      heif_file.mode,
      heif_file.size,
      heif_file.data,
      "raw",
      heif_file.mode,
      heif_file.stride,
    )
    img.thumbnail((413, 531))
    img.save(f'{jpg_file}')
    start_num += 1
    print(f'{heic_base_name} ==> {os.path.basename(transfered_name)}: Transfering into 512^2 Pixel... Success!')
