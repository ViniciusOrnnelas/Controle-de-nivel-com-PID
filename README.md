# Controle-de-nivel-com-PID
Este projeto tem como objetivo o desenvolvimento de um sistema de controle de nível de água utilizando um controlador PID implementado em um microcontrolador Arduino.

## Materiais e tecnologias utilizadas

O projeto consiste em:
- Um protótipo com dois reservatórios de água;
- Sensor ultrassônico para medir o nível;
- Bomba de água de 12V para transferência do líquido;
- Arduino Uno;
- Algoritmos de identificação de sistemas e sintonia de controladores implementados em Python;
- Controle embarcado utilizando algoritmo PI.


## Metodologia
A metodologia completa está descrita no arquivo [`docs/metodologia.md`](docs/metodologia.md).

## Arduino (PI Controller)

O código fonte está em [`software/controle_pi.ino`](software/controle_pi.ino)



## Resultados
A combinação dos elementos de eletrônicos com o controlador PID e PI ser visualizado abaixo:
Após a determinação do sistema, foi executado um outro algorítimo em Python que realizou a sintonia de Ziegler-Nichols para um controlador PID. A função findpeak da biblioteca SciPy

| **Controlador** | **Kp** | **Ki** | **Kd** |
| --------------- | ------ | ------ | ------ |
| P               | 1.0000 | -      | -      |
| PI              | 0.9000 | 0.9549 | -      |
| PID             | 1.2000 | 2.1221 | 0.1690 |



