fprintf('Start reading at %s\n',datestr(now,'HH:MM:SS'));
data=csvread('video_bin_2.0_kb.csv',1,1);
fprintf('Finish reading at %s\n',datestr(now,'HH:MM:SS'));
data_shape=size(data);
y=data(:,1);
X=data(:,1:data_shape(2));
fprintf('Start mrmr at %s\n ...',datestr(now,'HH:MM:SS'));
[mrmr, mrmr_s]=feast('mrmr',36,X,y);
fprintf('Finish mrmr at %s\n',datestr(now,'HH:MM:SS'));
csvwrite('40%_mrmr_video_bin_kb_2.0.csv',[mrmr mrmr_s]);

