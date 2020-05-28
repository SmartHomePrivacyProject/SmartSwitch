fprintf('Start reading at %s\n',datestr(now,'HH:MM:SS'));
data=csvread('alexa_incoming.csv',1,0);
fprintf('Finish reading at %s\n',datestr(now,'HH:MM:SS'));
data_shape=size(data);
y=data(:,1);
X=data(:,2:400);
results = zeros(100,399);
for i=0:99
    rows=y(:,1)==i;
    d = X(rows,:);
    r = mean(d);
    results(i+1,:)=r(1,1:end);
end
csvwrite('results/alexa_incoming_pattern.csv',results);