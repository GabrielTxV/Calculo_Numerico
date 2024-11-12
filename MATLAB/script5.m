clc;

a = input("Digite um valor inteiro: ");
b = input("Digite outro valor inteiro: ");

media = (a + b)/2;
fprintf("A media calculada = %.2f\n", media);
if (media>=7)
    fprintf("Aprovado com media: %.2f\n", media);
elseif (media<3)
    fprintf("Reprovado com media: %.2f\n", media);
else 
    fprintf("Prova final com media: %.2f\n", media);
end

