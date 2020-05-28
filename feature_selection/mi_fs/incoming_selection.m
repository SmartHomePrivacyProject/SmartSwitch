fprintf('Start reading at %s\n',datestr(now,'HH:MM:SS'));
data=csvread('wf.csv',0,0);
fprintf('Finish reading at %s\n',datestr(now,'HH:MM:SS'));
data_shape = size(data);
incoming = zeros(data_shape);
incoming(:,1)=data(:,1);
for i=1:data_shape(1)
    for j=2:data_shape(2)
        if data(i,j)<0
            incoming(i,j)=data(i,j);
        end
    end
    
end
csvwrite('results/wf_incoming.csv',incoming);