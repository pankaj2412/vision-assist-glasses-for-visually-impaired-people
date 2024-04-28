const int trigPin = 8; // Trigger pin for the ultrasonic sensor
const int echoPin = 10; // Echo pin for the ultrasonic sensor
const int buzzerPin = 7; // Buzzer control pin

long duration;
int distance;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(buzzerPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // Trigger the ultrasonic sensor
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Measure the time it takes for the echo to return
  duration = pulseIn(echoPin, HIGH);

  // Calculate the distance in centimeters
  distance = duration / 58.2;

  // Print the distance to the serial monitor
  Serial.print("Distance: ");
  Serial.println(distance);

  // Check if the distance is less than a certain threshold
  if (distance < 50) { // Adjust the threshold as needed
    // Turn on the buzzer
    digitalWrite(buzzerPin, LOW);
  } else {
    // Turn off the buzzer
    digitalWrite(buzzerPin, HIGH);
  }
}
