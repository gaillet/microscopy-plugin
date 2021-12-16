import numpy as np
import os
import shutil
from PIL import Image as im
import numpy

src = 'C:/Users/vgaillet/Downloads/mouse_cerebellum/tomo300511_subv3_1/069000/069000_151000/069000_151000_145510.tiff'
dst = 'C:/Users/vgaillet/OneDrive - Fondation Campus Biotech Geneva/Pictures'

#destination = shutil.copy2(src, dst)

I = im.open('C:/Users/vgaillet/OneDrive - Fondation Campus Biotech Geneva/Pictures/000000_000172___000427_0c.tif')

imarray = numpy.array(I)

maxi = np.amax(imarray)
mini = np.amin(imarray)

imarray = imarray/maxi*255
maxi = np.amax(imarray)
I = im.fromarray(imarray)
I.show()
