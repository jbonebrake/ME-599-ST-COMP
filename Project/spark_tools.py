# -*- coding: utf-8 -*-
#!usr/bin/env python 3

# Script for ME 599 Project
# Jonathan Bonebrake
        
def open_files(intensity_path,pathlength_path):
    import scipy.io
    
    f = scipy.io.loadmat(intensity_path)
    intensity = f['intensity']
    f = scipy.io.loadmat(pathlength_path)
    pathlength = f['pathlength']
        
    return intensity, pathlength

def color_plot(data,frame):
    
    import matplotlib.pyplot as plt
    plt.figure()
    plt.contourf(data[:,:,frame], levels = 30)
    plt.show()
    
def linearize_kernel(intensity,pathlength):
    kernel_intensity = []
    
    for page in range(intensity.shape[2]):
        
        kernel_frame = []
        
        for col in range(intensity.shape[1]):
            for row in range(intensity.shape[0]):
                
                if pathlength[row,col,page] != 0.0:
                    kernel_frame.append(intensity[row,col,page])
                    
        kernel_intensity.append(kernel_frame)
        
    return kernel_intensity

def linearize_background(intensity,pathlength):
    background_intensity = []
    
    for page in range(intensity.shape[2]):
        
        frame = []
        
        for col in range(intensity.shape[1]):
            for row in range(intensity.shape[0]):
                
                if pathlength[row,col,page] == 0.0:
                    frame.append(intensity[row,col,page])
                    
        background_intensity.append(frame)
        
    return background_intensity

    
def signal_noise(data):
    import numpy as np
    std_dev = []
    average = []
    
    for i in range(len(linear_kernel)):
        std_dev.append(np.std(data[i]))
        average.append(np.mean(data[i]))

    snr = [x/y for x, y in zip(std_dev,average)]
    
    return std_dev, average, snr

def max_loc(data):
    # determine x,y coordinates of maximum intensity value
    import numpy as np
    coordinates = []
    
    for page in range(data.shape[2]):
        ind = np.unravel_index(np.argmax(data[:,:,page], axis=None), data[:,:,page].shape)
        coordinates.append(ind)
    
    return coordinates     

def kernel_centroid(pathlength):
    from scipy import ndimage
    centroids = []
    
    for page in range(pathlength.shape[2]): 
        centroid = ndimage.measurements.center_of_mass(pathlength[:,:,page])
        centroids.append(centroid)
    
    return centroids

def distance(locations,centroids):
    import numpy as np
    distance = []
    
    for frame in range(len(locations)):
        delta = np.sqrt((locations[frame][1]-centroids[frame][1])**2 + (locations[frame][1]-centroids[frame][1])**2)
        distance.append(delta)
        
    return distance


if __name__ == '__main__': 
    
    import matplotlib.pyplot as plt
    
    pathlength_path = 'C:\\Users\\jmich\\.spyder-py3\\data\\kernel_detected\\pathlength_v7\\25-Jan-2018_run_000010_5.mat'
    intensity_path = 'C:\\Users\\jmich\\.spyder-py3\\data\\kernel_detected\\intensity_v7\\25-Jan-2018_run_000010_5.mat'
    
    intensity, pathlength = open_files(intensity_path, pathlength_path)
    
#    color_plot(intensity,10)
#    color_plot(pathlength,10)
    
    linear_kernel = linearize_kernel(intensity,pathlength)
    linear_background = linearize_background(intensity,pathlength)
    std_f,average_f,snr_f = signal_noise(linear_kernel)
    std_b,average_b,snr_b = signal_noise(linear_background)
    locations = max_loc(intensity)
    centroids  = kernel_centroid(pathlength)
    distance = distance(locations,centroids)
    
    signal_ratio = [x/y for x, y in zip(snr_f,snr_b)]
    
    plt.figure()
    plt.plot(snr_f)
    plt.plot(snr_b)
    plt.title('SNR for kernel and background')
    plt.ylabel('\sigma / \mu')
    plt.legend(['foreground','background'])
    plt.show()
    
    plt.figure()
    plt.plot(signal_ratio)
    plt.title('Ratio of kernel SNR to background SNR')
    plt.ylabel('SNR_f/SNR_b')
    plt.show()
    
    plt.figure()
    plt.plot(distance)
    plt.title('Distance between max intensity and centroid')
    plt.ylabel('distance')
    plt.show()
    
    
    
    