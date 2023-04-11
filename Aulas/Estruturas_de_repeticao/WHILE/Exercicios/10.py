# Chico tem 1,50m e cresce 2 centímetros por ano, enquanto Juca tem 1,10m e cresce 5 centímetros    por ano. Considerando que Chico e Juca continuem crescendo constantemente, escreva um algoritmo  que calcule quantos anos seriam necessários para Juca ser mais alto que Chico.

chico = float(1.50)
juca = float(1.10)
anos = 0

while (chico >= juca):
    chico += 0.02
    juca += 0.05
    anos += 1
print(f"Para Juca ser maior que Chico será necessário {anos} anos")