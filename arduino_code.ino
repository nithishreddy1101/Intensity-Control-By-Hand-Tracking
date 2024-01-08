

SerialData serialData(1,3); //(numOfValsRec,digitsPerValRec)

/*0 or 1 - 1 digit
0 to 99 -  2 digits 
0 to 999 - 3 digits 
 */

int valsRec[1];

void setup() {
  serialData.begin(115200); 
  pinMode(9,OUTPUT); //connect to pin 9 
 
}

void loop() {
  
  serialData.Get(valsRec);
  digitalWrite(1,valsRec[0]);

}
