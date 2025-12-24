# Лабораторная работа №4 — Библиотека

Реализация симуляции работы библиотеки с использованием пользовательских коллекций, наследования и псевдослучайной модели.

## Требования

- Python 3.8+
- `typer`

Установка зависимостей:
```bash
pip install typer
```

## Структура проекта

```
lab4/
├── src/
│   ├── book.py
│   ├── collections.py
│   ├── library.py
│   ├── simulation.py
│   └── main.py
└── tests/
```
## Запуск симуляции

```bash
python -m src.main --steps 20 --seed 42
```

Пример вывода:
```
Simulation start
Steps: 20, Seed: 42
Step 1  Added book: "The Silent Forest" by G. Orwell (1862) [ISBN: 2181960013389] — 624 pp.
Step 2  Removed book: "The Silent Forest" by G. Orwell (1862) [ISBN: 2181960013389] — 624 pp.
Step 3  Search by author 'C. Dickens':
    Found: <none>
Step 4  No books found from year 2007
Step 5  Added book: "Beneath Crimson Skies" by H. Lovecraft (1887) [ISBN: 2351161559407] — 994 pp.
Step 6  No books found from year 1820
Step 7 ISBN lookup (4959310341316): not found
Step 8  Search by author 'C. Dickens':
    Found: <none>
Step 9  Search by author 'J. Austen':
    Found: <none>
Step 10  Search by author 'L. Baum':
    Found: <none>
```

### Параметры:
- `--steps` — количество шагов симуляции
- `--seed` — начальное значение генератора случайных чисел

## Тестирование

Запуск тестов:
```bash
python -m pytest tests/ -v
```

Тесты проверяют:
- корректность наследования и полиморфизма,
- работу коллекций,
- воспроизводимость симуляции.