import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from behave import given, when, then  # noqa: E402
from weather_service import WeatherService, WeatherAlert  # noqa: E402


@given("текущая температура воздуха равна {temp} градусов")
def step_impl(context, temp):
    context.service = WeatherService()
    context.service.update_weather(float(temp), "Clear")


@given("настроен порог оповещения {threshold} градусов")
def step_impl(context, threshold):
    context.alert = WeatherAlert(float(threshold))


@when("система проверяет погодные условия")
def step_impl(context):
    context.result = context.alert.check_alert(context.service)


@then("пользователь получает уведомление")
def step_impl(context):
    assert context.result is True


@then("пользователь не получает уведомлений")
def step_impl(context):
    assert context.result is False