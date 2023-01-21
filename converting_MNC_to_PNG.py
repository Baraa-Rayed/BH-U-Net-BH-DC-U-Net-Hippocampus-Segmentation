import numpy as np
import os    # Traverse folders 
import nibabel as nib #nii Format 1 This bag will be used in general 
import imageio   # Convert to an image 
def MNC_to_image(MNCfile):
 filenames = os.listdir(filepath) # Read nii Folder 
 slice_trans = []
 
 for f in filenames:
  # Start reading MNC Documents 
  img_path = os.path.join(filepath, f)
  img = nib.load(img_path)    # Read nii
  img_fdata = img.get_fdata()
  fname = f.replace('.mnc','')   # Remove mnc Suffix name of 
  img_f_path = os.path.join(imgfile, fname)
  # Create nii The folder of the corresponding image 
  if not os.path.exists(img_f_path):
   os.mkdir(img_f_path)    # New Folder 
 
  # Start converting to an image 
   affine = np.array([[0, 0, 1, 0],
                   [0, 1, 0, 0],
                   [1, 0, 0, 0],
                   [0, 0, 0, 1]])

   out = nib.Nifti1Image(img.get_data(), affine=affine)
  (x,y,z) = img.shape
  print(img.shape)
  
  for i in range(x):      #z Is a sequence of images 
   silce = img_fdata[i, :, :]
   ii = f'{i:03d}'# You can choose which direction of slice 
   imageio.imwrite(os.path.join(img_f_path,'{}_{}.png'.format(fname,ii)), silce)
            # Save an image 
 
if __name__ == '__main__':
 filepath = 'Filepath'
 imgfile = 'Insert the file path where you want to save the images in it'
 MNC_to_image(filepath)
