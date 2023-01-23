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
```

Метод game.step:
```python
def step(self, index_row: int, index_column: int, player: PlayerBase):
```


Метод game.result
```python
GameStateT = TypeVar('GameStateT', bound=GameStateBase, covariant=True)

def result(self, player: PlayerBase) -> GameStateT:
```

Метод game.step_result
```python

def step_result(self, index_row: int, index_column: int, player: PlayerBase) -> GameStateT:
```

Метод game.ai_get_step
```python
def ai_get_step(self, player: PlayerBase) -> CellIndex:
```

Метод game.ai_step
```python
def ai_step(self, player: PlayerBase):
```

Метод game.ai_step_result
```python
def ai_step_result(self, player: PlayerBase) -> GameStateT:
```

### TABLE

### PLAYERS

### PLAYER

### GAME STATE
...
