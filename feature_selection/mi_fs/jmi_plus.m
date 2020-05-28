fprintf('Start reading at %s\n',datestr(now,'HH:MM:SS'));
data=csvread('video_bin_0.05_kb.csv',1,1);
score_list=csvread('mi_video_bin_0.05_kb.csv');
fprintf('Finish reading at %s\n',datestr(now,'HH:MM:SS'));
data_shape=size(data);
label=data(:,1);
X=data(:,2:data_shape(2));

mi_packets=zeros(data_shape(2)*10,3);
size_x=size(X);

% [f, s]=feast('jmi', 400, X, y);
H_c = h(label);
for i=1:size_x(2)
    pool=zeros(data_shape(2)-1,3);
    fprintf('Start %d at %s\n',i,datestr(now,'HH:MM:SS'));
    for j=i+1:size_x(2)
        I_y_c=score_list(j,2);            
        H_x_c = condh(X(:,i), label);
        xcy = [X(:,i) label X(:,j)];
        H_xcy = h(xcy);
        
        H_y_c = condh(X(:,j),label);
        H_cy = H_y_c + H_c; 
        I_xy_c = H_x_c - (H_xcy - H_cy) + I_y_c;
%         if (I_xy_c < 0)
%             fprintf(I_xy_c);
%         end
        r = [[i,j],I_xy_c];
        pool(j-1,:) = r;
        
    end  
    [max,idx]=maxk(pool(:,3),10);
    mi_packets((i-1)*10+1:i*10,:) = pool(idx,:);
    fprintf('Finish %d at %s\n',i,datestr(now,'HH:MM:SS'));
    
end
csvwrite('results/jmi_plus_video_kb_2.0.csv',mi_packets);