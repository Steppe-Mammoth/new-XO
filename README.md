# XO Tic-Tac-Toe

## Основні можливості:
+ **Не обмежена кількість гравців в одній грі**
+ **Створення ігрової таблиці будь-якого розміру**:  
+ + *Вказавши потрібні параметри розміру: **рядка**, **стовбця** і **виграшної комбінації***
+ **Алгоритм "Штучного інтелекту" працює з будь-якими параметрами гри**


## Знайомство з біблеотекою
### Старт швидкої гри в консолі
_Ми можемо задати будь-який розмір для ігрової таблиці та безліч гравців для гри_ 
- _AI і перелік виграшних комбінації для гравців підлаштуються автоматично_

_Скористаємося цим. **Замість класичної таблиці 3х3 - створимо 7х7, та 3 гравця**  
Цього разу боти хай грають один з одним. Поглянемо на це_

```python
# app.py
from game import TableParam, TableDefault, GameConsole, Player, Players, Symbol

if __name__ == "__main__":
    p1 = Player(name="Pertos_ANDROID:1", symbol=Symbol('X'), role=Player.Role.ANDROID)
    p2 = Player(name="Amigos_ANDROID:2", symbol=Symbol('O'), role=Player.Role.ANDROID)
    p3 = Player(name="Gentos_ANDROID:3", symbol=Symbol('K'), role=Player.Role.ANDROID)

    # p4 = Player(name="PLAYER", symbol=Symbol('P'), role=Player.Role.USER)  # Якщо без вас ніяк

    players = Players(players=[p1, p2, p3])
    table = TableDefault(param=TableParam(ROW=7, COLUMN=7, COMBINATION=5))
    # COMBINATION - кількість клітинок яких потрібно зайняти підряд одним символом для виграшгу

    game_console = GameConsole(players=players, table=table)
    game_console.start_game()
```

<details>
  <summary>Attempt #1</summary>
  
```python
WIN: ANDROID:1 < X > | COMB: < ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)) >
+-----+---+---+---+---+---+---+---+
| ↓/→ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
+-----+---+---+---+---+---+---+---+
|  0: | O | * | * | * | K | X | K |
|  1: | K | X | * | * | O | * | X |
|  2: | X | K | X | O | K | O | X |
|  3: | K | O | K | X | X | K | O |
|  4: | K | O | X | X | X | O | X |
|  5: | O | O | K | O | O | X | X |
|  6: | * | * | O | K | * | K | K |
+-----+---+---+---+---+---+---+---+
```
</details>

<details>
  <summary>Attempt #2</summary>
  
```python
PEACE: ALL USED CELLS
+-----+---+---+---+---+---+---+---+
| ↓/→ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
+-----+---+---+---+---+---+---+---+
|  0: | X | K | K | O | O | O | X |
|  1: | K | X | X | K | X | O | K |
|  2: | X | K | O | O | O | X | K |
|  3: | O | X | K | K | O | K | X |
|  4: | X | O | K | O | O | X | O |
|  5: | X | X | O | X | X | K | K |
|  6: | K | K | X | O | K | O | X |
+-----+---+---+---+---+---+---+---+
```
</details>

<details>
  <summary>Attempt #3</summary>
  
```python
WIN: ANDROID:4 < O > | COMB: < ((3, 1), (3, 2), (3, 3), (3, 4), (3, 5)) >
+-----+---+---+---+---+---+---+---+
| ↓/→ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
+-----+---+---+---+---+---+---+---+
|  0: | * | * | * | * | K | * | * |
|  1: | * | * | * | * | K | * | * |
|  2: | * | X | * | * | * | * | * |
|  3: | * | O | O | O | O | O | X |
|  4: | * | * | * | * | K | * | * |
|  5: | * | * | * | * | * | * | * |
|  6: | K | X | X | X | O | X | K |
+-----+---+---+---+---+---+---+---+
```
</details>

Метод `.start_game` активує цикл while з умовою виходу, якщо гра буде логічно закінчено (Є виграш / Всі клітинки зайняті == `game_console.game_state.is_finished`)

* Для гравців в черзі, які повертають True для методу `player.is_android` застосовуюється автоматичний пошук клітинки, а для гравців які повернуть True для `player.is_user` буде запропоновано вести індекси в консолі

___Як захочете нагрузити процесор сотнею ботів в 1000х1000 полі - ніхто не завадить!___
_Підемо далі_

# API

### GAME
```python
from game import TableParam, TableDefault, Player, Players, Symbol, Game

p1 = Player(name="Vera_ANDROID", symbol=Symbol('X'), role=Player.Role.ANDROID)
p2 = Player(name="Andruha_PLAYER", symbol=Symbol('O'), role=Player.Role.USER)

players = Players(players=[p1, p2])
table = TableDefault(param=TableParam(ROW=3, COLUMN=3, COMBINATION=3))

game = Game(players=players, table=table)
```
```python
+-----+---+---+---+
| ↓/→ | 0 | 1 | 2 |
+-----+---+---+---+
|  0: | * | * | * |
|  1: | * | * | * |
|  2: | * | * | * |
+-----+---+---+---+
```

#### Метод game.step:
```python
def step(self, index_row: int, index_column: int, player: PlayerBase)
```
```python
game.step(index_row=1, index_column=0, player=p2)  # my first step
```
```python
+-----+---+---+---+
| ↓/→ | 0 | 1 | 2 |
+-----+---+---+---+
|  0: | * | * | * |
|  1: | O | * | * |
|  2: | * | * | * |
+-----+---+---+---+
```
Фукція встановлює символ гравця `player.symbol` в клітинку за вказаними індексами.  
Після успішного встановлення лічильник `player.count_steps` збільшується на +1, а `game.table.count_free_cells` зменшується на -1

Примітка:
* _Якщо передані індекси не збігаються з можливими в таблиці - помилка_ `TableIndexError`
* _Якщо ви намагаєтесь встановити новий символ на вже зайняту клітинку - помилка_ `CellAlreadyUsedError`

#### Метод game.result:
```python
def result(self, player: PlayerBase) -> GameStateT
```
```python
res = game.result(player=p2)
```
```python
res.is_finished  # False
assert res == game.game_state  # True
```
Для заданого гравця (його символа) функція проводить 2 перевірки
* _Пошуку виграшу, де здійснюється перевірка по комбінаціям які доступні в `game.table.combinations`_
* _Перевірка на нічию. Порівнюється значення результату `game.table.count_free_cells`_
  
Коли одна з двух вірогідностей дійсна, автоматично викликається метод `game_state.update`, який модифікує: `game_state`, змінюючи вньому статус `.code`, а в випадку коли гравець виграв - щей доповнює поля: `.win_player` і `.win_combination`

Пілся перевірок та можливих модифікацій - повертає об'єкт: `game_state`

Примітка: 
* _Щоб дізнатися що одна з тригерів які логічно завершуює гру спрацювала - викликаєм в game_state метод: `.is_finished`, якщо True - в нас є виграш або нічия. Детальніше див. розділ GameState_

#### Метод game.step_result:
```python
def step_result(self, index_row: int, index_column: int, player: PlayerBase) -> GameStateT
```
Об'єднувальний метод. Замніняє почерговий виклик  `game.step` і `game.result`


#### Метод game.ai_get_step:
```python
def ai_get_step(self, player: PlayerBase) -> CellIndex
```
Для вказаного гравця, знаходить найкращу клітинку для ходу.  
Повертає кортеж з двома елементами (`index_row: int, index_column: int`)


#### Метод game.ai_step:
```python
def ai_step(self, player: PlayerBase)
```
Об'єднувальний метод. Замніняє почерговий виклик  `game.ai_get_step` і `game.step`

#### Метод game.ai_step_result:
```python
def ai_step_result(self, player: PlayerBase) -> GameStateT
```
Об'єднувальний метод. Замніняє почерговий виклик  `game.ai_get_step` і `game.step_result` повертаючи результат останього
...

### TABLE

* _Комбінації створюються автоматично за параметрами таблиці, або передаються врчуну коли конструюється екземпляр класу Table_
...

### PLAYERS
...

### PLAYER
...

### GAME STATE
...

### AI

Короткий приклад роботи:
```python
p1 = Player(name="PLAYER", symbol=Symbol('X'))
p2 = Player(name="ANDROID", symbol=Symbol('O'))
...
```
```python
game.step(2, 2, player=p1)
game.step(0, 0, player=p1)

game.ai_step(p2)  # result in second table

+-----+---+---+---+   ->   +-----+---+---+---+
| ↓/→ | 0 | 1 | 2 |   ->   | ↓/→ | 0 | 1 | 2 |
+-----+---+---+---+   ->   +-----+---+---+---+
|  0: | X | * | * |   ->   |  0: | X | * | * |
|  1: | * | * | * |   ->   |  1: | * | O | * |
|  2: | * | * | X |   ->   |  2: | * | * | X |
+-----+---+---+---+   ->   +-----+---+---+---+
```
* AI алгоритм розуміє, що наступний хід для суперника буде виграшний, тому перекриває його

Розглянемо другу ситуацію
```python
game.step(0, 0, player=p1)  # X
game.step(2, 0, player=p1)  # X

game.step(0, 2, player=p2)  # O
game.step(2, 2, player=p2)  # O

game.ai_step(p2)  # result in second table

+-----+---+---+---+   ->   +-----+---+---+---+
| ↓/→ | 0 | 1 | 2 |   ->   | ↓/→ | 0 | 1 | 2 |
+-----+---+---+---+   ->   +-----+---+---+---+
|  0: | X | * | O |   ->   |  0: | X | * | O |
|  1: | * | * | * |   ->   |  1: | * | * | O |
|  2: | X | * | O |   ->   |  2: | X | * | O |
+-----+---+---+---+   ->   +-----+---+---+---+
```
* AI алгоритм ставить в пріоритет свій виграш, розуміючи що наступного ходу для суперника вже не буде
