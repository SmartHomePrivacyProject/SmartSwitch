fprintf('Start reading at %s\n',datestr(now,'HH:MM:SS'));
data=csvread('video_bin_0.05_kb.csv',1,1);
score_list=csvread('mi_video_bin_0.05_kb.csv');
fprintf('Finish reading at %s\n',datestr(now,'HH:MM:SS'));
data_shape=size(data);
y=data(:,1);
X=data(:,2:data_shape(2));

max_mi = 0;
max_id = 0;
size_sl=size(score_list);

for i=1:size_sl(1,1)
    if(score_list(i, 2)>max_mi)
        max_mi = score_list(i,2);
        max_id = i;
        max_feature = f_set(:,i);
        size_f=size(max_feature);
    end
end
mifs_packets = [max_id, max_mi];
selected_shape = size(mifs_packets);

while selected_shape(2) < 360
   
    parfor i=1:selected_shape(1)
        beta = 0.5;
        max = 0;
        max_j = 0;
        for j=1:data_shape(2)-1
            if ~ismember(j,mifs_packets(:,1))
                I = mi(X(:,j),y);
                I_xx = mi(X(:,j),X(:,mifs_packets(i,1)));
                II = I - beta * I_xx;
                if II > max
                    max = II;
                    max_j = j;
                end
             end
        end
        r = [max_j,max];
        mifs_packets=[mifs_packets;r];
        selected_shape = size(mifs_packets);
        fprintf('Finish at %s\n',datestr(now,'HH:MM:SS'));
    end
   
end
csvwrite('mifs_video_bin_0.05.csv',mifs_packets(1:2,1:end)');