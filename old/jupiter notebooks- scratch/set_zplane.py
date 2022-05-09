def set_zplane(xdim, ydim):

    z_plane = img.shape[1] / 2
    z_plane = round(z_plane)
    z_plane_top = z_plane-3
    z_plane_bottom = z_plane+3