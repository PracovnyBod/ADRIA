



fileName = 'stepAt0060sec.csv'


stepData = readmatrix(strcat('./', fileName), 'Delimiter', ',', 'NumHeaderLines', 1);

figure(1)

subplot(2,1,1)
plot(stepData(:,1), stepData(:,3));

subplot(2,1,2)
plot(stepData(:,1), stepData(:,2));


