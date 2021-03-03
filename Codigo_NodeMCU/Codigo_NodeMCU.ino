#include <Wire.h>
#include <DFRobot_MAX30102.h>

//#include <Adafruit_MLX90614.h>
//#include <SoftwareSerial.h>
DFRobot_MAX30102 particleSensor;
 
//SoftwareSerial mySerial(0, 1); // RX, TX
int Dato =0;

int32_t SPO2; //SPO2
int8_t SPO2Valid; //Flag to display if SPO2 calculation is valid
int32_t heartRate; //Heart-rate
int8_t heartRateValid; //Flag to display if heart-rate calculation is valid 
uint32_t period =10000L;       // 4 segundos
//Adafruit_MLX90614 mlx = Adafruit_MLX90614();
 float vref = 3.3;
float resolution = vref/1023;
void setup() {
  Serial.begin(115200);
  //mySerial.begin(9600);
  //mlx.begin(); 
  while (!particleSensor.begin()) {
    Serial.println("MAX30102 was not found");
    delay(1000);
  }

  particleSensor.sensorConfiguration(/*ledBrightness=*/50, /*sampleAverage=*/SAMPLEAVG_4, \
                        /*ledMode=*/MODE_MULTILED, /*sampleRate=*/SAMPLERATE_100, \
                        /*pulseWidth=*/PULSEWIDTH_411, /*adcRange=*/ADCRANGE_16384); 
    
}
void loop(){
  unsigned long current=millis();
  delay(2000);
  Dato = Serial.read();
  //Serial.print("I received: ");
  Serial.println(Dato);
  delay(1000);


if(Dato==49){//49 es el 1 en ASCII
  
  //Serial.begin(9600);

  //delay(3000);
 // Serial.end();
 // Serial.begin(9600);


for( uint32_t tStart = millis();  (millis()-tStart) < period;  ){
    
  //Serial.println(mlx.readObjectTempC()+3.3); 
  //delay(500); 
  float temperature = analogRead(A0);
 temperature = (temperature*resolution);
 temperature = temperature*100;
 Serial.println(temperature);
 delay(1000); 
}
Serial.write("a");
  Serial.println();
  delay(10);
   }


   
else if(Dato==50){//50 es el 2 en ASCII
  
 //delay(3000);
 // Serial.end();
 // Serial.begin(115200);

for( uint32_t tStart = millis();  (millis()-tStart) < period;  ){
  particleSensor.heartrateAndOxygenSaturation(/**SPO2=*/&SPO2, /**SPO2Valid=*/&SPO2Valid, /**heartRate=*/&heartRate, /**heartRateValid=*/&heartRateValid);
  Serial.println(SPO2, DEC);

}   

Serial.write("a");
  Serial.println();
  delay(10);
//  delay(3000);
 // Serial.end();
//  Serial.begin(9600);

   }

else if (Dato==51){//51 es el 3 en ASCII
    for( uint32_t tStart = millis();  (millis()-tStart) < period;  ){
  particleSensor.heartrateAndOxygenSaturation(/**SPO2=*/&SPO2, /**SPO2Valid=*/&SPO2Valid, /**heartRate=*/&heartRate, /**heartRateValid=*/&heartRateValid);
  Serial.println(heartRate, DEC);

}

Serial.write("a");
  Serial.println();
  delay(10);   

    }


  }
