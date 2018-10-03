//銃コントローラ加速度センサ
/*加速度センサ
 1.VDD – 電源電圧
 2.PSD – センサ値を表示する為にVDDに接続
 3.GND – グランド
 4.Parity
 5.SelfTest
 6.X軸のデータ
 7.Y軸のデータ
 8.Z軸のデータ
*/
/*
 * 平らな状態
 * X=501,500
 * Y=515,514
 * Z=723,722
 */
#define pin_X 3
#define pin_Y 4
#define pin_Z 5
#define pilot_LED 2
#define startBit 's'
#define endBit 'e'

void setup() {
  Serial.begin(9600);

}

void loop() {
  long x,y,z;
  x=y=z=0;
  x=analogRead(pin_X);
  y=analogRead(pin_Y);
  z=analogRead(pin_Z);
  Serial.print(startBit);
  //Serial.print("X:");
  Serial.print(x);
  //Serial.print(" Y:");
  Serial.print(y);
  //Serial.print(" Z:");
  Serial.print(z);
  Serial.print(endBit);
  delay(50);
}
