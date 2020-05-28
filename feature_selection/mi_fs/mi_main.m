fprintf('Start reading at %s\n',datestr(now,'HH:MM:SS'));
data=csvread('video_bin_2.0_kb.csv',1,1);

fprintf('Finish reading at %s\n',datestr(now,'HH:MM:SS'));
data_shape=size(data);
% for i=1:data_shape(1)
%     l = length(data(i,:));
%     
% end
y=data(:,1);
X=data(:,2:data_shape(2));
mi_packets=[];
size_x=size(X);
parfor i=1:90   
    I = mi(X(:,i),y);
    r = [i,I];
    mi_packets=[mi_packets;r];    
    fprintf('Finish %d at %s\n',i,datestr(now,'HH:MM:SS'));
end
csvwrite('results/mi_video_bin_2.0_kb.csv',mi_packets);