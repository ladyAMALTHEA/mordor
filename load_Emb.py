def load_embryo(config.txt): # ask Jeff how to write the proper syntax here.  
    czi = czifile.imread(file_name)
    img=czi.squeeze()
    data = {}
    for channel in channel_list:
        data[channel] = img[channel_dict[channel],...]
    
    xdim = img.shape[2]
    ydim = img.shape[3]

