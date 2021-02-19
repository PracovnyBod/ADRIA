clear all;
clc

global P

% Perioda vzorkovania
Tvz = 0.1;

% Identifikovana sustava
B = [0 0.15];
A = [1 0.3 0.2];

% Prepis do diskretneho tvaru (len tak pre zaujimavost...)
Gs = tf(B,A);
Gz = c2d(Gs,Tvz);
[Bz,Az] = tfdata(Gz,'v')

% Startovacia matica P
P = 10^6 * eye(4,4) ;