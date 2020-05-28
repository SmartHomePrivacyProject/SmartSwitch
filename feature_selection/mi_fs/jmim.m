function [selected_feature, feature_set] = jmim(s_feature, f_set, labels, score_list)
%I_xy_c = H_x_c - (H_xcy - H_cy) + I_y_c;

size_f=size(f_set);
size_s=size(s_feature);
size_l=size(labels);
pool=zeros(size_s(1,1),size_f(1,2));
%labels = normalize(labels);
H_c = h(labels);

parfor i=1:size_f(1,2)  
    min_jmi=1000;
    idx=0;
    candidate_f = f_set(:,i);
    %candidate_f = normalize(candidate_f);
    H_x_c = condh(candidate_f, labels);
    if isequal(candidate_f, ones(size_l(1,1),1))
        continue
    end
  
    for j=1:size_s(1,2)

        sf=s_feature(3:end,j);
        sf_idx=s_feature(1,j);
        I_y_c=score_list(sf_idx,2);                            
        xcy = [candidate_f labels sf];
      
        %xcy = normalize(xcy);
        H_xcy = h(xcy);
        %h_xcy = h(xcy);
        %sf = normalize(sf);
        H_y_c = condh(sf,labels);
        H_cy = H_y_c + H_c;     
        I_xy_c = H_x_c - (H_xcy - H_cy) + I_y_c;
        
        if (I_xy_c < min_jmi)
            min_jmi = I_xy_c;
            min_feature = candidate_f;
            idx=i;
        end
    end
    new_feature=[idx; min_jmi; min_feature];
    pool(:,i)=new_feature;
   
end
max_candidate_score = 0;
max_candidate_idx = 0;
max_candidate = [];
size_p=size(pool);
for k=1:size_p(1,2)
    if(pool(2,k)>max_candidate_score)
        max_candidate_score = pool(2,k);
        max_candidate_idx = pool(1,k);
        max_candidate = pool(3:end,k);
    end
end
selected_feature=[max_candidate_idx;max_candidate_score;max_candidate];
f_set(:,max_candidate_idx)=ones(size_l(1,1),1);
feature_set=f_set;

