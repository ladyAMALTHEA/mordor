def get_age(path, filename):
    czi = czifile.imread(path)
    img=czi.squeeze()

    data = {}
    for channel in channel_list:
        data[channel] = img[channel_dict[channel],...]
    #dimensions of the image
    ydim = img.shape[2]
    xdim = img.shape[3]
    zoom_x1 = round(xdim/2-xdim/5)
    zoom_x2 = round(xdim-(xdim/2-xdim/5))
    zoom_y1 = round(ydim/2-ydim/5)
    zoom_y2 = round(ydim-(ydim/2-ydim/5))

    #output images
    max_projection = data[age_channel].max(0)
    mid_slice =round(img.shape[1] / 2)
    stage_slice = data[age_channel][mid_slice,:,:]
    age_zoom_top = max_projection[zoom_y1:zoom_y2,  zoom_x1:zoom_x2]
    age_zoom_mid = stage_slice[zoom_y1:zoom_y2,  zoom_x1:zoom_x2]


    #to see images
    fig = plt.figure(figsize=(200,200))
    ax=fig.add_subplot(2,2,1)
    plt.imshow(max_projection, cmap='gray', vmin=bkgd_signal, vmax=np.max(max_projection)-1)
    ax=fig.add_subplot(2,2,2)
    plt.imshow(stage_slice, cmap='gray', vmin=bkgd_signal, vmax=np.max(stage_slice)-1)
    ax=fig.add_subplot(2,2,3)
    plt.imshow(age_zoom_top, cmap='gray', vmin=bkgd_signal, vmax=np.max(age_zoom_top)-1)
    ax=fig.add_subplot(2,2,4)
    plt.imshow(age_zoom_mid, cmap='gray', vmin=bkgd_signal, vmax=np.max(age_zoom_top)-1)

    #time to save
    os.makedirs(path[:-4], exist_ok=True)
    fig.savefig(os.path.join(path[:-4], f"{filename[:-4]}_DAPI"))