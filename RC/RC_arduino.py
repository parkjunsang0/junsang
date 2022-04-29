int CH_3;
void setup() {
  pulseIn(9,INPUT);
  pulseIn(10,INPUT);
  pulseIn(11,INPUT);
  Serial.begin(9600);

}

void loop() {
  int value_1 = pulseIn(9,HIGH);
  int value_2 = pulseIn(10,HIGH);
  int value_3 = pulseIn(11,HIGH);
  int CH_1 = map(value_1,970,2030,1120,1880);
  int CH_2 = map(value_2,970,2030,1120,1880);
  int CH_2_1 = (3000-CH_2);
  if (1480<=CH_1&&CH_1<=1520)
  {
    CH_1=1500;
  }
  if (1480<=CH_2_1&&CH_2_1<=1520)
  {
    CH_2_1=1500;
  }
  if (value_3<1500)
  {
    CH_3=0;
  }
  if (1500<value_3)
  {
    CH_3=1;
  }
  
  Serial.print(CH_1);
  Serial.print(" ");
  Serial.print(CH_2_1);
  Serial.print(" ");
  Serial.println(CH_3);
}
