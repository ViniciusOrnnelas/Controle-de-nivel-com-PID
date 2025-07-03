# Metodologia

Foi construído um protótipo que simula o comportamento de um sistema de reserva de fluidos. Os principais componentes são:

- Sensor ultrassônico para leitura do nível
- Bomba 12V para movimentar água entre recipientes
- Arduino Uno
- Algoritmos em Python para identificação do sistema e ajuste do controlador

A modelagem matemática utilizou filtros de Butterworth de 1ª e 2ª ordem:

### Segunda ordem
$$
\frac{0.02008s^2+0.04017s+0.02008}{s^2-1.561s+0.6414}
$$

### Primeira ordem
$$
\frac{0.1367s+0.1367}{s-0.7265}
$$

A sintonia do PID foi feita com o método de Ziegler-Nichols.

As respostas do sistema mostraram que os controladores PI e PID foram capazes de manter o nível de água com precisão satisfatória.
