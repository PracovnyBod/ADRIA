clear all
clc



pModelKoef = csvread('./dataRepo/pModelKoef.csv');



u_PB1 = 112;

ok_u_PB1 = 20;

y_PB1 = polyval(pModelKoef, u_PB1);



u_PB2 = 212;

ok_u_PB2 = 20;

y_PB2 = polyval(pModelKoef, u_PB2);




data_Ts = 0.02;
sim('ar06_ident_v00')


%% ------------------------------------------------------------------------

figure(01);

subplot(2,1,1)

plot(simIdentData.Time, simIdentData.Data(:,1), 'k')

hold on;

plot( [0, 50], [y_PB1, y_PB1], 'r--')
plot( [50, 100], [y_PB2, y_PB2], 'r--')

hold off;

subplot(2,1,2)

plot(simIdentData.Time, simIdentData.Data(:,2), 'k')

hold on;

plot( [0, 50], [u_PB1, u_PB1], 'r--')
plot( [50, 100], [u_PB2, u_PB2], 'r--')

hold off;

%% ------------------------------------------------------------------------

 
tmpMask = (simIdentData.Time >= 10) & (simIdentData.Time < 50);

identData_PB1_time = simIdentData.Time(tmpMask);
identData_PB1_time = identData_PB1_time - identData_PB1_time(1);

identData_PB1 = simIdentData.Data(tmpMask,:);

identData_PB1(:,1) = identData_PB1(:,1) - y_PB1;
identData_PB1(:,2) = identData_PB1(:,2) - u_PB1;

idDAT_PB1 = iddata(identData_PB1(:,1), identData_PB1(:,2), data_Ts);






tmpMask = (simIdentData.Time >= 60) & (simIdentData.Time < 100);

identData_PB2_time = simIdentData.Time(tmpMask);
identData_PB2_time = identData_PB2_time - identData_PB2_time(1);

identData_PB2 = simIdentData.Data(tmpMask,:);

identData_PB2(:,1) = identData_PB2(:,1) - y_PB2;
identData_PB2(:,2) = identData_PB2(:,2) - u_PB2;

idDAT_PB2 = iddata(identData_PB2(:,1), identData_PB2(:,2), data_Ts);




%% ------------------------------------------------------------------------

figure(11);

subplot(2,1,1)

plot(identData_PB1_time, identData_PB1(:,1), 'k')

subplot(2,1,2)

plot(identData_PB1_time, identData_PB1(:,2), 'k')




figure(12);

subplot(2,1,1)

plot(identData_PB2_time, identData_PB2(:,1), 'k')

subplot(2,1,2)

plot(identData_PB2_time, identData_PB2(:,2), 'k')


%% ------------------------------------------------------------------------


sys_PB1_z = arx(idDAT_PB1, [2,1,1])

sys_PB1_s = d2c(sys_PB1_z)



sys_PB2_z = arx(idDAT_PB2, [2,1,1])

sys_PB2_s = d2c(sys_PB2_z)


%% ------------------------------------------------------------------------
% porovnanie jednokrokovej predikcie pre ARX

figure(31);

compare(idDAT_PB1, sys_PB1_z, 1)

figure(32);

compare(idDAT_PB2, sys_PB2_z, 1)




%% ------------------------------------------------------------------------
% pololopatisticke porovnanie pre spojity identifikovany system


mojSys_PB1 = tf(sys_PB1_s.B, sys_PB1_s.A);

mojSys_PB1_plot = series(mojSys_PB1, 40);

[step_Y, step_T] = step(mojSys_PB1_plot);


tmp_Mask = identData_PB1_time < 10;

PCH_PB1_plot = [identData_PB1_time(tmp_Mask), identData_PB1(tmp_Mask,1) - identData_PB1(end,1)];

figure(33);
plot(PCH_PB1_plot(:,1), PCH_PB1_plot(:,2), 'k') 

hold on
plot(step_T, step_Y, 'b') 
hold off

legend('data', 'model')


%% ------------------------------------------------------------------------
% este viac pololopatisticke porovnanie pre spojity identifikovany system


sim('ar06_ident_v00_res')


