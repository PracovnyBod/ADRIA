clear all;

pModelKoef = [
9.066120820215151913e-07
-3.410454352015338799e-04
-1.615890544785271096e-02
2.180836138929650048e+01
-1.672898734153517807e+03
];


pModelKoef_inv = [
-6.519524468685905000e-10
1.364697965483804428e-06
-8.063595019441653590e-04
2.669774671866143034e-01
8.031177874564231445e+01
];

T1pModelKoef = [
1.035690502248605546e-07
-5.199736955688934615e-05
7.076262763987984684e-03
-1.943403477780802132e-03
];

T2pModelKoef = [
-2.192700968493659594e-06
5.579350060836428841e-04
2.230879583956927453e-02
];


namerData_1 = csvread('./dataRepo/allSig_log_prev_mer1_up.csv');
namerData_2 = csvread('./dataRepo/allSig_log_prev_mer2_up.csv');
namerData_3 = csvread('./dataRepo/allSig_log_prev_mer3_up.csv');
namerData_4 = csvread('./dataRepo/allSig_log_prev_mer4_up.csv');
namerData_5 = csvread('./dataRepo/allSig_log_prev_mer5_up.csv');
namerData_6 = csvread('./dataRepo/allSig_log_prev_mer6_up.csv');






