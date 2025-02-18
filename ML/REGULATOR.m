function vyst = REGULATOR(theta)

global ZP   

a1 = theta(1);
a2 = theta(2);
b1 = theta(3);
b2 = theta(4);
 
MATICA = [1 b1 0; a1 b2 b1; a2 0 b2];
PRAVASTRANA = [ZP(2) - a1; ZP(3) - a2; 0];
RS = MATICA\PRAVASTRANA;

T = (1 + ZP(2) + ZP(3))/(b1 + b2);

vyst = [RS' T]';