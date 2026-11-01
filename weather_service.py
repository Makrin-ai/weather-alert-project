class WeatherService:
    """Класс для получения и хранения данных о погоде."""

    def __init__(self):
        self.temperature = 0.0
        self.condition = ""

    def update_weather(self, temperature: float, condition: str):
        self.temperature = temperature
        self.condition = condition

    def get_temperature(self) -> float:
        return self.temperature


class WeatherAlert:
    """Класс для проверки условий и генерации оповещений."""

    def __init__(self, threshold: float):
        self.threshold = threshold

    def check_alert(self, service: WeatherService) -> bool:
        if service.get_temperature() < self.threshold:
            print(
                f"ВНИМАНИЕ! Температура {service.get_temperature()}°C "
                f"ниже порога {self.threshold}°C"
            )
            return True
        return False