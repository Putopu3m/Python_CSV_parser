# CSV Processor

Простой CLI-скрипт на Python для обработки CSV-файлов с поддержкой:

- фильтрации (`--where`)
- сортировки (`--order_by`)
- агрегации (`--aggregate`)

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Putopu3m/Python_CSV_parser.git
   cd Python_CSV_parser
   ```

2. Создайте виртуальное окружение (опционально):
   ```bash
   python3 -m venv venv
   ```
   
   Активируйте виртуальное окружение:

   - **Linux / macOS**:
     ```bash
     source venv/bin/activate
     ```

   - **Windows**:
     ```cmd
     venv\Scripts\activate
     ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## Запуск скрипта
Шаблон команды запуска:
```bash
python source/main.py --filename example.csv [--where "column>|<|=|>=|<=|<>value"] [--order_by "column=asc|desc"] [--aggregate "column=func"]
```

Аргументы можно комбинировать. Порядок обработки:
1. `--where` — фильтрация
2. `--order_by` — сортировка
3. `--aggregate` — агрегация 

## Примеры

### Пример CSV (`products.csv`):

```csv
name,brand,price,rating
iphone 15 pro,apple,999,4.9
galaxy s23 ultra,samsung,1199,4.8
redmi note 12,xiaomi,199,4.6
iphone 14,apple,799,4.7
galaxy a54,samsung,349,4.2
poco x5 pro,xiaomi,299,4.4
iphone se,apple,429,4.1
galaxy z flip 5,samsung,999,4.6
redmi 10c,xiaomi,149,4.1
iphone 13 mini,apple,599,4.5
```

### Фильтрация: `price > 300`

```bash
python source/main.py --filename products.csv --where "price>300"
```

### Агрегация: `средняя цена`

```bash
python source/main.py --filename products.csv --aggregate "price=avg"
```

### Сортировка: `по рейтингу по убыванию`

```bash
python source/main.py --filename products.csv --order_by "rating=desc"
```

### Комбинированный запрос:

```bash
python source/main.py --filename products.csv --where "brand=xiaomi" --order_by "price=desc"
```

## Поддерживаемые функции агрегации

- `sum` — сумма
- `min` — минимум
- `max` — максимум
- `avg` — среднее
- `median` — медиана

## Тестирование

Для запуска тестов:

```bash
pytest pytest tests/test_csv_parsing.py
```

Покрытие составляет 80%. 