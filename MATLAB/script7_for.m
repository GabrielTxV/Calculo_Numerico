clc;

soma = 0;
total = 10;

for i=1:total
    fprintf ('%d ', i);
    v(i) = input('Digite um valor inteiro:');
  %  soma = soma + v;
end

fprintf('A soma calculada = %.2f\n', sum(v));      
fprintf('A média calculada = %.2f\n', sum(v)/total);
fprintf('A maior entrada = %.2f\n', max(v));
fprintf('A menor entrada = %.2f\n', min(v));