'''
@Time    : 2022/8/4 10:09
@Author  : leeguandon@gmail.com
'''
import os
from pathlib import Path
from tqdm import tqdm

folder = Path("/home/ivms/local_disk/vcg_furnitures/img_download")

image_file = [*folder.glob("*.jpg")]

for img in tqdm(image_file):
    name = img.stem
    with open(Path(folder, f"{name}.txt"), 'w', encoding='utf-8') as f:
        f.write(name)

    # pass
