int CH_2_2;
void setup(){
    pulseIn(9,INPUT);
    pulseIn(10,INPUT);
    Serial.begin(9600);
}
void loop(){
    unsigned long value_1 = pulseIn(9,HIGH);
    unsigned long value_2 = pulesIn(10,HIGH);
    int CH_1 = map(value_1,  ,  ,  ,  );
    int CH_2 = map(value_2,  ,  ,  ,  );
    if (1470<=CH_1<=1530)
    {
    CH_1=1500;
    }
    if (1370<=CH_2<=1430)
    {
    CH_2_2=1500;
    }
    else if (1430<CH_2<=2000)
    {
    CH_2_2=CH_2+100;
    }
    else
    {
    CH_2_2=CH_2+100;
    }
    if 1100<=CH_1<=1900&&1100<=CH_1<=1900
    {
    Serial.print(CH_1);
    Serial.print(" ");
    Serial.printIn(CH_2_2);
    }
}

import serial
import pigpio
pi2=pigpio.pi()
port="dev/ttyACM0"
serialfromArduino=serial.Serial(port,9600)
while True:
    input_s = serialfromArduino.readline()
    input_s = input_s.decode("utf-8")
    input = input_s.replace("\r\n","")
    CH_1 = int(input[0:4])
    CH_2 = int(input[5:9])
    throtle = abs(1500-CH_1)
    if CH_2>1500:
        if (1500-CH_1)<0:
            pi2.set_servo_pulsewidth(19,CH_2-throtle)
            pi2.set_servo_pulsewidth(9,CH_2)
        elif (1500-CH_1)>0:

        else:

    elif CH_2<1500:
        if (1500 - CH_1) < 0:

        elif (1500 - CH_1) > 0:

        else:

    else:
        if (1500 - CH_1) < 0:

        elif (1500 - CH_1) > 0:

        else: