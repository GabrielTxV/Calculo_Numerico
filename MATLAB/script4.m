clc;

a = input("Digite um valor inteiro: ");
b = input("Digite outro valor inteiro: ");

media = (a + b)/2;
fprintf("A media calculada = %.2f\n", media);
if (media>=7)
    fprintf("Aprovado com media: %.2f\n", media);
else 
    fprintf("Reprovado com media: %.2f\n", media);
end

