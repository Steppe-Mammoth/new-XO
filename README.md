# XO Tic-Tac-Toe

## Основні можливості:
+ **Можливо додати скільки завгодно гравців**

+ **Можливо створити ігрову таблицю любого розміру**:
+ + *Задавши параметри **рядка**, **стовбця** і **розмір виграшної комбінації** на свій смак*

+ *Штучний інтелект не повторює себе і працює по різним сценаріям*

+ *Додавайте свій функціонал успадковуючись від потрібних класів*


## Знайомство з біблеотекою
Замість стандартного розкладу 3х3 таблиці на двух гравців ми ...  

Створимо 3 гравця! і призначемо кожному штучний інтелект `role=Player.Role.ANDROID`  
Розмір поля хай буде 10 на 10, а виграшну комбінацію задамо розміром в 7 клітинок  
Зараз буде баталія ботів, поглянемо на цю кібер разборку

```python
from game import TableParam, TableDefault, GameConsole, Player, Players, Symbol

if __name__ == "__main__":
    p1 = Player(name="ANDROID:1", symbol=Symbol('X'), role=Player.Role.ANDROID)
    p2 = Player(name="ANDROID:4", symbol=Symbol('I'), role=Player.Role.ANDROID)
    p3 = Player(name="ANDROID:3", symbol=Symbol('K'), role=Player.Role.ANDROID)

    # p4 = Player(name="PLAYER:2", symbol=Symbol('O'), role=Player.Role.USER)  # Якщо без вас ніяк

    players = Players(players=[p1, p2, p3])
    table = TableDefault(param=TableParam(ROW=10, COLUMN=10, COMBINATION=7))

    game = GameConsole(players=players, table=table)
    game.start_game()
```
<details>
  <summary>Attempt #1</summary>
  
![Image alt](images/win_10_10.png)
</details>

<details>
  <summary>Attempt #2</summary>
  
![Image alt](images/peace_10_10.png)
</details>

+ Цей шаблон для швидкого знаходиться в app.py, можете запустити його в github codespace

___Як захочете то нагрузити процесор сотнею ботів в 1000х1000 полі - ніхто не завадить!___

_Підемо далі_

# API

### GAME
```python
from game import TableParam, TableDefault, Player, Players, Symbol, Game

p1 = Player(name="Vera_ANDROID", symbol=Symbol('X'), role=Player.Role.ANDROID)
p2 = Player(name="Andruha_PLAYER", symbol=Symbol('O'), role=Player.Role.USER)

players = Players(players=[p1, p2])
table = TableDefault(param=TableParam(ROW=3, COLUMN=3, COMBINATION=3))
# COMBINATION - кількість клітинок яких потрібно зайняти підряд одним символом для виграшгу

game = Game(players=players, table=table)
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
+-----+---+---+---+
| ↓/→ | 0 | 1 | 2 |
+-----+---+---+---+
|  0: | * | * | * |
|  1: | O | * | * |
|  2: | * | * | * |
+-----+---+---+---+
```
Фукція яка встановлює символ гравця `player.symbol` в клітинку за вказаними індексами.  
Після успішного встановлення лічильник `player.count_steps` збільшується на +1, а `game.table.count_free_cells` зменшується на -1

Примітка:
* _Якщо передані індекси не збігаються з можливими в таблиці - помилка_ `TableIndexError`
* _Якщо ви намагаєтесь встановити новий символ на вже зайняту клітинку - помилка_ `CellAlreadyUsedError`

#### Метод game.result:
```python
GameStateT = TypeVar('GameStateT', bound=GameStateBase, covariant=True)

def result(self, player: PlayerBase) -> GameStateT
```
```python
res = game.result(player=p2)
res.is_finished  # False
```
Для заданого гравця (його символа) функція проводить перевірку на виграш в гральній таблиці.  
Перевірка здійснюється по заданим комбінаціям які доступні в `game.table.combinations` 

Якщо виграш відсутній, проводиться перевірка на вільні клітинки.  
Коли одна з двух вірогідностей дійсна, автоматично викликається метод `game_state.update` який модифікує: `game.game_state`, змінюючи вньому статус `.code`, а в випадку коли гравець виграв - щей доповнює поля: `.win_player` і `.win_combination`

Пілся перевірок та можливих модифікацій - повертає об'єкт: `game_state`

Примітка: 
* _Комбінації створюються автоматично за параметрами таблиці, або передаються врчуну коли конструюється екземпляр класу Table_
* _Щоб дізнатися що одна з тригерів які логічно завершуює гру спрацювала - можно викликавши в поверненому результаті або через екземпляр гри метод: `game_state.is_finished`, якщо False - продовжуємо грати_
_Про GameState - далі. Тут коротко_

#### Метод game.step_result:
```python

def step_result(self, index_row: int, index_column: int, player: PlayerBase) -> GameStateT
```

#### Метод game.ai_get_step:
```python
def ai_get_step(self, player: PlayerBase) -> CellIndex
```

#### Метод game.ai_step:
```python
def ai_step(self, player: PlayerBase)
```

#### Метод game.ai_step_result:
```python
def ai_step_result(self, player: PlayerBase) -> GameStateT
```

### TABLE

### PLAYERS

### PLAYER

### GAME STATE
...
