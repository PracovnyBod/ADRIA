function odhadTheta = MNS(vst)
global P

P_n = P;

theta = vst(6:9);

h_n1 = [vst(2:5)];
y_n1 = vst(1);

e_n1 = y_n1 - h_n1' * theta;    
Y_n1 = (P_n*h_n1)/(1+h_n1'*P_n*h_n1);
P_n1 = P_n - Y_n1*h_n1'*P_n;
odhadTheta = theta + Y_n1*e_n1;  

P = P_n1;