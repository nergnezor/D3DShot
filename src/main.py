# pip install torch===1.4.0 torchvision===0.5.0 -f https://download.pytorch.org/whl/torch_stable.html

import d3dshot
import shutil
from pathlib import Path
import time
import os


nSeconds = 1.0
outDir = Path('out')
region = (0, 0, 300, 300)


if outDir.exists() and outDir.is_dir():
    shutil.rmtree(outDir)
os.mkdir(outDir)


d = d3dshot.create(capture_output='numpy')
print(d.display)
# d.capture(target_fps=60, region=region)
d.capture()
time.sleep(nSeconds)  # Capture is non-blocking so we wait explicitely
d.stop()
time.sleep(0.1)
start = time.time()
d.frame_buffer_to_disk(directory=outDir.name)
generatedImages = os.listdir(outDir)
print('Captured ' + str(len(generatedImages)/nSeconds) + ' images per second')
print('Read framebuffer: ' + str(time.time() - start) + 's elapsed')

# d.benchmark()
