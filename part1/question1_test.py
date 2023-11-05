from Pregunta1 import get_city_weather

def test_get_city_weather():

  assert get_city_weather("Quito") == "22 degrees and unknown"

  assert get_city_weather("New York") == "14 degrees and rainy"

if __name__ == "__main__":
    test_get_city_weather()
