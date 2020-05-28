fprintf('Start reading at %s\n',datestr(now,'HH:MM:SS'));
data=csvread('video_bin_1.0_kb.csv',1,1);
%data=csvread('alexa.csv',1,1);
score_list=csvread('mi_video_bin_1.0_kb.csv');
%score_list=csvread('mi_alexa.csv');
fprintf('Finish reading at %s\n',datestr(now,'HH:MM:SS'));

y=data(:,1);
f_set=data(:,2:end);
size_f_set=size(f_set);
feature_dim=size_f_set(1,1);

num_to_select = 72;
%results=zeros(feature_dim(1,1)+2,num_to_select);
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
%f_set(:,max_id)=[];
f_set(:,max_id) = ones(feature_dim,1);
%s_feature=struct('id', max_id, 'feature', max_feature, 'score', max_mi);
s_feature=[max_id; max_mi; max_feature];
num_of_selected = size(s_feature);
while num_of_selected(1,2) < num_to_select
    fprintf('Start jmim at %s\n ...',datestr(now,'HH:MM:SS'));
    [selected_feature, f_set] = jmim(s_feature, f_set, y, score_list);
    s_feature=[s_feature selected_feature];
    num_of_selected = size(s_feature);
    fprintf('End jmim at %s\n',datestr(now,'HH:MM:SS'));
    disp('size: ');
    disp(size(s_feature));
end

fprintf('Finish mrmr at %s\n',datestr(now,'HH:MM:SS'));
csvwrite('40%_jmim_video_bin_kb_1.0.csv',s_feature(1:2,1:end)');