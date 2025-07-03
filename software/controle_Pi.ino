const int trigPin = 9;    // Pino de trigger do sensor ultrassônico
const int echoPin = 10;   // Pino de echo do sensor ultrassônico
const int IN1 = 3;        // Controle 1 da ponte H
const int IN2 = 4;        // Controle 2 da ponte H
const int EN = 5;         // Controle PWM da ponte H

const float setpoint = 14; // Distância desejada em cm
float Kp = 10.0;          // Ganho proporcional (ajustável)
float Ki = 0.6;           // Ganho integral (ajustável)

float integral = 0.0;
float lastError = 0.0;

unsigned long startTime;  // Variável para armazenar o tempo inicial

void setup() {
    Serial.begin(9600);
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
    pinMode(IN1, OUTPUT);
    pinMode(IN2, OUTPUT);
    pinMode(EN, OUTPUT);

    startTime = millis();  // Inicializa o tempo inicial
}

void loop() {
    unsigned long currentTime = millis() - startTime;  // Calcula o tempo decorrido

    float distance = getDistance();
    float error = setpoint - distance;

    // Controle PI
    integral += error; 
    float output = (Kp * error) + (Ki * integral);

    // Limitando a saída para -255 a +255
    output = constrain(output, -255, 255);

    // Controle de direção e velocidade
    if(output >= 0) {
        digitalWrite(IN1, HIGH);
        digitalWrite(IN2, LOW);
        analogWrite(EN, output);  // PWM positivo
    } else {
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, HIGH);
        analogWrite(EN, -output);  // PWM negativo (inverte a direção)
    }

    // Debug no monitor serial no formato desejado
    Serial.print(currentTime / 1000.0, 2);
    Serial.print(",");
    Serial.print(17.5 - distance);
    Serial.print(",");
    Serial.print(output);
    Serial.print(",");  // Mantém os valores na mesma linha

    delay(100);
}

float getDistance() {
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    long duration = pulseIn(echoPin, HIGH);
    return duration * 0.034 / 2; // Converte para cm
}
