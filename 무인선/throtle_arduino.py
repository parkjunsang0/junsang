int CH_2_2;

void setup() {
    pulseIn(9,INPUT);
    pulseIn(10,INPUT);
    Serial.begin(9600);
}

void loop() {
    unsigned long value_1 = pulseIn(9,HIGH);
    unsigned long value_2 = pulseIn(10,HIGH);

    int CH_1 = map(value_1,1050,1960,1150,1850);
    int CH_2 = map(value_2,1101,2000,1130,1830);

    if (1470 <= CH_1 && CH_1 <= 1530)
    {
        CH_1 = 1500;
    }

    if (1340 <= CH_2 && CH_2 <= 1420)
    {
        CH_2_2 = 1500;
    }
    else if (1420 <= CH_2 && CH_2 <= 2000)
    {
    CH_2_2 = CH_2 + 100;
    }
    else
    CH_2_2 = CH_2 + 100;

    if (1100 <= CH_1 <= 1900 && 1100 <= CH_2 <= 1900)
    {
    Serial.print(CH_1);
    Serial.print(" ");
    Serial.printIn(CH_2_2);
    }
}