clear all;
clc

global P ZP lambdaKoef

% Perioda vzorkovania
Tvz = 0.1;

% Identifikovana sustava
B = [0 0.15];
A = [1 0.3 0.2];

% Zelany polynom
ZP = conv([1 -0.8],[1 -0.8]);

lambdaKoef = 0.95

% Startovacia matica P
P = diag([20, 10^2, 10^5, 10^5]) ;