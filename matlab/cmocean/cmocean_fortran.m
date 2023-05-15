%%%%%%%%%%%%% Create .txt files with cmocean RGB for fortran %%%%%%%%%%%%%%
% Example of how to use it: cmocean_fortran('curl') or
% cmocean_fortran('-curl')

function cmocean_fortran(color_cmocean)

RGB_matlab = cmocean(color_cmocean,100);
RGB_fortran = round(RGB_matlab*255);

if(color_cmocean(1) == '-')
    name_file = [color_cmocean(2:end) '_r.txt'];
else
    name_file = [color_cmocean '.txt'];
end

% writematrix(RGB_fortran,name_file,'Delimiter',' ');
writematrix(RGB_fortran,name_file,'Delimiter','tab')
end