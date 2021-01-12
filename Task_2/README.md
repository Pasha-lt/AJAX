# Задание 2

1. Написать функцию, которая конвертирует "Decimal Degrees (DD)" формат координат в "Degrees Decimal Minutes (DDM)" формат координат
2. С помощью pytest написать параметризированный тест, который принимает на вход значение в DD формате и ожидаемое значение в DDM формате

Пример:
```python
def test_cordinates(given_dd, expected_ddm)
```
Тест дата для параметризации:
```python
TEST_DATA_LONGITUDE = [
  (-180, "180^0W"),
  (-180.0, "180^0W"),
  (-13.912, "13^54.72W"),
  (0, "0^0E"),
  (180.0, "180^0E"),
  (180, "180^0E"),
  (170.0323, "170^1.938E"),
]
```
Для выполнения данной команды нам нужно нужно инсталировать pytest.
Чтобы не нарушать экосистему создаем виртуальное окружения.
```
python3 -m venv env
```

Затем активируем наше виртуальное окружение. 
```
source env/bin/activate
```
После чего установим в виртальное окружение наши зависимости.
```
pip install -r requirement.txt
```
Теперь можем запускать наши тесты через терминал.
```
python -m pytest
```
Также мы можем запустить через pycharm.

Вывод:
```
============================= test session starts ==============================
platform linux -- Python 3.8.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- /usr/bin/python3.8
cachedir: .pytest_cache
rootdir: /home/admin2/Desktop/AJAX_QA/Task_2
collecting ... collected 7 items

test_DDtoDDM.py::test_convert_result['-180' -> '180^0W'] PASSED          [ 14%]
test_DDtoDDM.py::test_convert_result['-180.0' -> '180^0W'] PASSED        [ 28%]
test_DDtoDDM.py::test_convert_result['-13.912' -> '13^54.72W'] PASSED    [ 42%]
test_DDtoDDM.py::test_convert_result['0' -> '0^0E'] PASSED               [ 57%]
test_DDtoDDM.py::test_convert_result['180.0' -> '180^0E'] PASSED         [ 71%]
test_DDtoDDM.py::test_convert_result['180' -> '180^0E'] PASSED           [ 85%]
test_DDtoDDM.py::test_convert_result['170.0323' -> '170^1.938E'] PASSED  [100%]

============================== 7 passed in 0.04s ===============================
```
