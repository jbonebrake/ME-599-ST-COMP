% script to read and split kernel detected files into intensity/boundary 
% files, and save to appropriate location

clc
clear 
close all

[file, path ] = uigetfile('*.mat', 'Select one or more','MultiSelect','on');
save_path_intensity = 'C:\Users\jmich\.spyder-py3\data\kernel_detected\intensity_v7\';
save_path_pathlength = 'C:\Users\jmich\.spyder-py3\data\kernel_detected\pathlength_v7\';

for i = 1:1%size(file,2)
    load(strcat(path,file{i}))
%    print(file{i})
    for j  = 1:10%size(spark,2)
        intensity = spark{j}.radiance;
        pathlength = spark{j}.pathlengths;
        intensity_name = strcat(save_path_intensity, file{i}(1:end-14), num2str(j))
        pathlength_name = strcat(save_path_pathlength, file{i}(1:end-14), num2str(j))
        
        save(intensity_name,'intensity','-v7')
        save(pathlength_name, 'pathlength','-v7')
    end
end

        
    