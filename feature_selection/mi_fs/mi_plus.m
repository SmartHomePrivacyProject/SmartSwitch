fprintf('Start reading at %s\n',datestr(now,'HH:MM:SS'));
data=csvread('video_bin_2.0_kb.csv',1,1);
fprintf('Finish reading at %s\n',datestr(now,'HH:MM:SS'));
data_shape=size(data);
y=data(:,1);
X=data(:,2:data_shape(2));
aa = (data_shape(2)-1) * 90;
mi_packets=zeros(aa,3);

for i=1:data_shape(2)-1
    pool=zeros(data_shape(2)-1,3);
    fprintf('Start %d at %s\n',i,datestr(now,'HH:MM:SS'));
    for j=i+1:data_shape(2)-1        
        I = mi(X(:,i),X(:,j));
        r = [[i,j],I];
        pool(j-1,1:end)=r;    
    end
    [max,idx]=maxk(pool(:,3),100);
    mi_packets((i-1)*90+1:i*90,:) = pool(idx,:);
    fprintf('Finish %d at %s\n',i,datestr(now,'HH:MM:SS'));   
end
csvwrite('results/mi_plus_video_kb_2.0.csv',mi_packets);