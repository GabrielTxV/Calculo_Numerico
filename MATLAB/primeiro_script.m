clc;

in = input('Digite um valor numerico: ');
fim = input('Digite outro valor numerico: ');
x = linspace(in,fim,100);

plot(x, abs(x));

grid on;