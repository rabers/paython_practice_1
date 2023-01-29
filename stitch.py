from PIL import Image
import glob
import os
from os import path

images_list = []

# This first part is an attempt to have the code running on several sets of images to be stitched for several outputs
#- but due to the memory allocation issue - the loop iterates only once for only one collection of images to be stitched
root_dir = "/Users/shayraber/data/"
for directory in os.scandir(root_dir):
    if directory.is_dir():
        #print(directory)
        dir_as_str = ''.join(str(directory))
        #print(as_str[as_str.index("'")+1:as_str.index("'>")])
        images_list.append(dir_as_str[dir_as_str.index("'")+1:dir_as_str.index("'>")])
        #print(images_list)
#images_list holds the list of directories, where each directory holds a set of images completing the bigger image
for i in images_list:
    image_file_base_name = []
    image_file_full_path = []
    #print(i)
    image_set_dir = "/Users/shayraber/data/"+i+'/Img'
    #print(image_set_dir+'/*.jpg')
    for file in glob.glob(image_set_dir+'/*.jpg'):
        image_file_base_name.append(os.path.basename(file))
        image_file_full_path.append(file)
        #print(image_file_full_path)

    image_file_base_name.sort(reverse=True)
    image_file_full_path.sort(reverse=False)
    #print(image_file_base_name,'\n')

    #print(image_file_base_name[0])
    #print(image_file_full_path[0])

    path_str = ''.join(str(image_file_full_path[0]))
    base_str = ''.join(str(image_file_base_name[0]))

    idx_columns = base_str.index("C")
    idx_lines = base_str.index("L")
    idx_filetype = base_str.index(".")
    idx_folder = path_str.index(".img/")

    num_of_lines = int(base_str[idx_lines+1:idx_columns]) +1  #This variable holds the # of lines as it appears after the 'L' within the file name - need to be modified accordingly
    num_of_columns = int(base_str[idx_columns+1:idx_filetype])+1  #This variable holds the # of columns as it appears after the 'C' within the file name - need to be modified accordingly
    #print(num_of_columns)
    #print(num_of_lines)
    target_folder = path_str[:idx_folder+4]
    #print(target_folder)
    a_small_image = Image.open(path_str)
    a_small_image_size = a_small_image.size
    px = a_small_image_size[0]
    py = a_small_image_size[1]
    new_image = Image.new('RGB',(num_of_columns*px, num_of_lines*py), (250,250,250))
    #new_image = Image.new('RGB',(17*1388, 23*1038), (250,250,250))

#     #print(image_file_full_path[1])
#     #print(image_file_full_path[10])
#     #print(image_file_full_path[390])
#     #print(num_of_columns)
#     #print(num_of_lines)
    #print(px)
    #print(py)
    counter = 0
    for y in range(num_of_lines):
        for x in range(num_of_columns):
            image_to_paste = Image.open(image_file_full_path[counter])
            new_image.paste(image_to_paste,(x*px,y*py))
            counter += 1
    #target_full_path = target_folder[target_folder.index("/")+1:target_folder.index(".img")] + "_MERGED.jpg"
    target_full_path = target_folder + "/Img/merged.jpg"
    print(target_full_path)
    print(target_folder)
    new_image.save(target_full_path,"JPEG")
#     #new_image.save("RawData/20220921_D2_S19069032B24.img/merged_image_final.jpg","JPEG")
