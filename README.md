# Controle-de-nivel-com-PID
Elaboração de um modelo de controle PID executado com microcontrolador Arduino para a efetuação do controle de nível de recipientes, apresentando a implementação de métodos para a definição dos elementos que o compõem no âmbito matemático, bem como os conceitos teóricos no qual o projeto é fundamentado e os resultados obtidos por meio de teste

## Metodologia
ara a realização do projeto, um protótipo que reproduz o comportamento de um sistema de reserva de fluidos foi elaborado, com o fluido a ser nivelado sendo água e com dois recipientes de tamanhos variados e posicionados um acima do outro, o inferior tendo uma bomba de água 12V acoplada externamente para o deslocamento do líquido para o recipiente que se encontra na posição elevada.Além disso, possui um sensor ultrassônico para a medição do nível da água no recipiente e um Arduino, que é uma placa eletrônica de código-aberto criada para prototipagem. O protótipo pode ser visualizado na imagem abaixo:

![image](https://github.com/user-attachments/assets/03883d6f-50d3-444e-9fc4-180eee2084c1)


Nesse contexto, implementou-se um algoritmo em Python que utiliza técnicas de processamento de sinais e identificação de sistemas. Primeiramente, os dados brutos são coletados do sistema para passar por uma etapa de pré-processamento, onde serão convertidos para vetores numéricos e depois  interpolados linearmente para garantir a sua discretização do tempo uniforme. A identificação do sistema foi realizada através de aproximação por filtro Butterworth de 1ª e 2ª ordem,  que, conforme (Dorf; Svoboda, 2016) se trata de um filtro elétrico passa-baixa que possui uma resposta de frequência próxima à de um filtro ideal, sendo baseada no modelo matemático desenvolvido por Butterworth conhecido como aproximação maximamente plana (ou aproximação de Butterworth), definida por (Malvino; Bates, 2016) como uma aproximação que possui como característica uma atenuação zero na maior parte da banda de passagem. Essas características fizeram com que os coeficientes do filtro fossem utilizados pelo algorítimo  por meio da função \textit{control.TransferFunction}[6], para construir as funções de transferência.
Segunda ordem:
\begin{equation}
\frac{0.02008s^2+0.04017s+0.02008}{s^2-1.561s+0.6414}
\end{equation}

Primeira ordem:
\begin{equation}
\frac{0.1367s+0.1367}{s-0.7265}
\end{equation}
