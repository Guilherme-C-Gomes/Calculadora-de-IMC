## Calculadora de IMC

Este script foi criado como parte de um pequeno projeto com o objetivo de praticar e aprender conceitos básicos de Python. É importante praticar e dominar o básico para desenvolver habilidades que permitam lidar com tarefas mais complexas de forma mais eficiente.

O Índice de Massa Corporal (IMC) é uma medida comumente usada para avaliar a relação entre o peso e a altura de uma pessoa. Este script permite calcular o IMC de acordo com os valores inseridos pelo usuário e fornece uma categoria com base nos intervalos predefinidos.

### Como usar

1. Execute o script Python `calcular_imc.py`.
2. Insira sua altura em centímetros quando solicitado.
3. Insira seu peso em quilogramas quando solicitado.
4. O script calculará automaticamente o seu IMC e fornecerá uma categoria com base nos intervalos predefinidos.

### Fórmula

O IMC é calculado utilizando a seguinte fórmula:

\[ IMC = \frac{peso}{altura^2} \]

onde:
- `peso` é o peso da pessoa em quilogramas.
- `altura` é a altura da pessoa em metros.

### Categorias de IMC

- **Abaixo do peso:** IMC < 18.5
- **Peso normal:** 18.5 ≤ IMC < 24.9
- **Sobrepeso:** 24.9 ≤ IMC < 29.9
- **Obesidade grau 1:** 29.9 ≤ IMC < 34.9
- **Obesidade grau 2 e 3:** IMC ≥ 40

### Nota

1. **Entrada de Dados (Input):** Utilização da função `input()` para receber dados do usuário, como altura e peso.

2. **Conversão de Tipos (Type Conversion):** Conversão dos dados de entrada (que são inicialmente strings) para tipos numéricos adequados (float para altura e peso).

3. **Operações Matemáticas:** Utilização de operações matemáticas básicas, como divisão, multiplicação e potenciação, para calcular o IMC.

4. **Condicionais (If-elif-else):** Utilização de estruturas condicionais para determinar a categoria do IMC com base nos valores calculados.

5. **Formatação de Strings:** Utilização de formatação de strings, especialmente com a função `format()`, para exibir o resultado do IMC com uma precisão específica.

6. **Comentários e Documentação:** Uso de comentários para documentar o código e explicar seu propósito e funcionamento.

7. **Variáveis e Atribuição:** Utilização de variáveis para armazenar e manipular valores ao longo do programa.

8. **Operadores Aritméticos:** Utilização de operadores aritméticos, como adição, subtração, multiplicação e potenciação, para realizar cálculos.

9. **Constantes:** Utilização de variáveis para armazenar valores constantes, como os limites de categorias de IMC.

10. **Loop de Programa (Main Loop):** Apesar de não estar explicitamente presente neste projeto, o conceito de um loop principal que solicita entrada do usuário e calcula o IMC poderia ser aplicado em projetos mais complexos ou em ambientes interativos.

Esses são alguns dos principais conceitos utilizados neste projeto de calculadora de IMC em Python. Eles são fundamentais para entender a lógica por trás do código e construir programas funcionais e eficazes.