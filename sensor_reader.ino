#include <DHT.h>

#define DHTPIN 2        // Pin where the DHT22 data pin is connected
#define DHTTYPE DHT22   // DHT 22 (AM2302)

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  if (isnan(h) || isnan(t)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  // Print as comma-separated values for Python script
  Serial.print(h);
  Serial.print(",");
  Serial.println(t);

  delay(2000); // DHT22 sampling rate is 2 seconds
}
