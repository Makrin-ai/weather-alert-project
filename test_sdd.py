import pytest
from weather_service import WeatherService, WeatherAlert


# Таблица спецификации из отчёта:
# | Температура | Порог | Ожидание |
# | -10         | -5    | True     |
# | -5          | -5    | False    |
# | 0           | -5    | False    |
# | 15          | -5    | False    |

test_data = [
    (-10, -5, True,  "Ниже порога — оповещение"),
    (-5,  -5, False, "Равно порогу — без оповещения"),
    (0,   -5, False, "Выше порога — без оповещения"),
    (15,  -5, False, "Намного выше порога — без оповещения"),
]


@pytest.mark.parametrize("temp, threshold, expected, comment", test_data)
def test_weather_alert_specification(temp, threshold, expected, comment):
    service = WeatherService()
    service.update_weather(temperature=temp, condition="Test")
    alert = WeatherAlert(threshold=threshold)

    result = alert.check_alert(service)
    assert result == expected, f"{comment}: ожидалось {expected}, получено {result}"