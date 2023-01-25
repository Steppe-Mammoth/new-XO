# XO Tic-Tac-Toe
_Бібліотека гри хрестики-нолики. Експерементальний функціонал з динамічними параметрами + AI_
___

## Основні можливості:
+ **Не обмежена кількість гравців в одній грі**
+ **Створення ігрової таблиці будь-якого розміру**:  
+ + *Вказавши потрібні параметри розміру: **рядка**, **стовбця** і **виграшної комбінації***
+ **Алгоритм "Штучного інтелекту" працює з будь-якими параметрами гри**

___

## Знайомство з бібліотекою
### Старт швидкої гри в консолі
_Ми можемо задати будь-який розмір для ігрової таблиці та безліч гравців для гри_ 
- _AI й перелік виграшних комбінацій для гравців підлаштуються автоматично_

_Скористаємося цим. **Замість класичної таблиці 3х3 - створимо 7х7, та 3 гравці**  
Цього разу боти хай грають один з одним. Поглянемо на це_

```python
# app.py
from game import TableParam, TableDefault, Player, Players, Symbol
from game.client.console import GameConsole

if __name__ == "__main__":
    p1 = Player(name="PETROS_ANDROID:1", symbol=Symbol('X'), role=Player.Role.ANDROID)
    p2 = Player(name="AMIGOS_ANDROID:2", symbol=Symbol('O'), role=Player.Role.ANDROID)
    p3 = Player(name="GENTOS_ANDROID:3", symbol=Symbol('K'), role=Player.Role.ANDROID)

    # p4 = Player(name="PLAYER", symbol=Symbol('P'), role=Player.Role.USER)  # Якщо без вас ніяк

    players = Players(players=[p1, p2, p3])
    table = TableDefault(param=TableParam(ROW=7, COLUMN=7, COMBINATION=5))
    # COMBINATION - кількість клітинок для виграшу, зібраних підряд одним символом

    game_console = GameConsole(players=players, table=table)
    game_console.start_game()
```

<details>
  <summary>Спроба №1</summary>
  
```python
WIN: PETROS_ANDROID:1 < X > | COMB: < ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)) >
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
  <summary>Спроба №2</summary>
  
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
  <summary>Спроба №3</summary>
  
```python
WIN: AMIGOS_ANDROID:2 < O > | COMB: < ((3, 1), (3, 2), (3, 3), (3, 4), (3, 5)) >
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



<details>
  <summary> * Короткий опис  GameConsole</summary> 

Метод `.start_game` активує цикл while з умовою виходу,
якщо гра буде логічно закінчено (Є виграш / Всі клітинки зайняті == `game_console.game_state.is_finished`)

* Для гравців в черзі, які повертають True для методу `player.is_android` застосовуються автоматичний пошук клітинки, 
а для гравців які повернуть True для `player.is_user` буде запропоновано вести індекси в консолі

</details>


__Як захочете нагрузити процесор сотнею ботів в 1000х1000 полі — ніхто не завадить!__
_Підемо далі_
___

# API
___
    
```python
from game import TableParam, TableDefault, Player, Players, Symbol, Game, ResultCode

p1 = Player(name="VERA_ANDROID", symbol=Symbol('X'), role=Player.Role.ANDROID)
p2 = Player(name="BOGDAN_PLAYER", symbol=Symbol('O'), role=Player.Role.USER)

players = Players(players=[p1, p2])
table = TableDefault(param=TableParam(ROW=3, COLUMN=3, COMBINATION=3))

game = Game(players=players, table=table)
```
+ ___Ці змінні будуть використовуватись при описі методів___
___

### GAME 
___Головний.___ _Відповідає за процес гри, обробку ходів, видачу результату._


<details>
  <summary>📂 Розгорнути</summary> 

___

#### - Зробити крок. `game.step`:
```python
def step(self, index_row: int, index_column: int, player: PlayerBase)
```
```python
# input
game.step(index_row=1, index_column=0, player=p2)  
game.step(index_row=1, index_column=2, player=p2)  
game.step(index_row=1, index_column=1, player=p2) 
```
```python
# output
+-----+---+---+---+   ->   +-----+---+---+---+   ->   +-----+---+---+---+  
| ↓/→ | 0 | 1 | 2 |   ->   | ↓/→ | 0 | 1 | 2 |   ->   | ↓/→ | 0 | 1 | 2 |
+-----+---+---+---+   ->   +-----+---+---+---+   ->   +-----+---+---+---+
|  0: | * | * | * |   ->   |  0: | * | * | * |   ->   |  0: | * | * | * |
|  1: | O | * | * |   ->   |  1: | O | * | O |   ->   |  1: | O | O | O |
|  2: | * | * | * |   ->   |  2: | * | * | * |   ->   |  2: | * | * | * |
+-----+---+---+---+   ->   +-----+---+---+---+   ->   +-----+---+---+---+
```
Функція встановлює символ гравця `player.symbol` в клітинку за вказаними індексами.  
Після успішного встановлення лічильник `player.count_steps` збільшується на +1,
а `game.table.count_free_cells` зменшується на -1

Примітка:
* _Якщо передані індекси не збігаються з можливими в таблиці - помилка_ `TableIndexError`
* _Якщо ви намагаєтесь встановити новий символ на вже зайняту клітинку - помилка_ `CellAlreadyUsedError`

___

#### - Отримати результат. `game.result`:

```python
def result(self, player: PlayerBase) -> GameStateT
```
_Перевіримо результат наших попередніх 3-ох кроків (в блоці вище), очікуємо виграш_
```python
# input
res = game.result(player=p2)
    
match res.code:
    case ResultCode.NO_RESULT:
        print('STATUS: NO RESULT')
    case ResultCode.WINNER:
        print(f'STATUS: WINNER. Player: {res.win_player.name}, Win comb: {res.win_combination}')
    case ResultCode.ALL_CELLS_USED:
        print('STATUS: DRAW')
``` 
```python   
# output
STATUS: WINNER. Player: BOGDAN_PLAYER, Win comb: ((1, 0), (1, 1), (1, 2))
```
Для заданого гравця функція проводить 2 перевірки:
* _Пошуку виграшу. Звіряється з виграшними комбінаціями_
* _Перевірка на нічию. Звіряється з показником вільних клітинок_
  
Коли одна з двух вірогідностей дійсна, автоматично викликається метод `game_state.update`, який модифікує: `game_state`,
змінюючи в ньому статус `.code`, а в випадку коли гравець виграв — ще й доповнює поля:
`.win_player` і `.win_combination` 

Після перевірок та можливих модифікацій — повертає об'єкт: `game_state`

Примітка: 
* `assert res == game.game_state  # True`
* _Список всіх виграшних комбінацій цієї гри доступний в `game.table.combinations`_
* _Дізнатися залишок вільних клітинок можна в `game.table.count_free_cells`_
* _Щоб перевірити що одна з тригерів які логічно завершує гру спрацювала — викликаємо в game_state метод: `.is_finished`,
якщо True - в нас є виграш або нічия. Також можете використати `.is_winner` або `.is_draw`.  
Детальніше див. розділ GameState_

___

#### - Зробити крок і повернути результат. `game.step_result`:

```python
def step_result(self, index_row: int, index_column: int, player: PlayerBase) -> GameStateT
```
* **Об'єднувальний метод**. _Заміняє почерговий виклик  `game.step` і `game.result`, повертає результат останнього_

---

#### - AI. Отримати індекс найкращої клітинки для гравця. `game.ai_get_step`:

```python
def ai_get_step(self, player: PlayerBase) -> CellIndex
```
AI повертає кортеж з двома індексами (`index_row: int, index_column: int`) клітинки
    
* _Детальніше див. розділ AI_

---

#### - AI. Зробити хід для гравця. `game.ai_step`:

```python
def ai_step(self, player: PlayerBase)
```
* **Об'єднувальний метод**. _Заміняє почерговий виклик.  `game.ai_get_step` і `game.step`_

---

#### - AI. Зробити хід для гравця і повернути результат. `game.ai_step_result`:

```python
def ai_step_result(self, player: PlayerBase) -> GameStateT
```
* **Об'єднувальний метод**. _Заміняє почерговий виклик  `game.ai_get_step` і `game.step_result`,
повертає результат останнього_
    
</details>

___

___
### TABLE
_Виставляє ходи в ігрове поле, і вираховує всі виграшні комбінації для себе_

<details>
  <summary>📂 Розгорнути</summary> 

___

_Екземпляр Table доступний в `game.table`_

___
#### - Отримати ігрове поле. `table.game_field`:

```python
@property
def game_field(self) -> GameFieldType
 ```  
Повертає двовимірний список ігрового поля 

Примітка:
+ _Також доступний в `game.game_field`_

___
#### - Отримати список виграшних комбінацій. `table.combinations`:    

```python
@property
def combinations(self) -> CombsType
```  
Повертає список всіх виграшних комбінацій для цієї таблиці
* _Комбінації створюються автоматично за параметрами таблиці,
або передаються вручну в конструктор екземпляра класу Table_

___

#### - Отримати кількість вільних клітинок. `table.count_free_cells`:   

```python
@property
def count_free_cells(self) -> int
```  
Повертає кількість вільних клітинок в таблиці

___

#### - Встановити символ в клітку. `table.set_symbol_cell`:   

```python
@property
def set_symbol_cell(self, index_row: int, index_column: int, symbol: SymbolBase)
``` 
Встановлює переданий символ за вказаними індексами ігрового поля.  
Зменшує рахунок вільних клітинок на -1  
    
Примітка:
* _Саме цей метод викликається в `game.step`_
    
</details>  

___
___

### PLAYERS
 
_Список гравців, Відповідає за їх почерговість_ 
   
<details>
  <summary>📂 Розгорнути</summary> 
  
___

_Екземпляр Players доступний в `game.players`_

___

#### - Отримати список гравців. `players.player_list`:   

```python
@property
def players_list(self) -> list[PlayerT]:
```  
Повертає список всіх гравців  

Примітка:
* _Цей список змінюється після застосування методу `players.shuffle_players`_
    
___


#### - Отримати поточного гравця. `players.current_player`:   

```python
@property
def current_player(self) -> PlayerT
```  
Повертає поточного гравця з черги
    
___

#### - Встановити й отримати наступного гравця. `players.set_get_next_player`:        

```python
def set_get_next_player(self) -> PlayerT
```  
Заміняє поточного гравця на наступного з черги й повертає його

Примітка:
* _Після цього цей гравець доступний в методі `players.current_player`_
    
___

#### - Перемішати список гравців. `players.shuffle_players`:        
```python
def shuffle_players(self)
```  
Перемішує список гравців й заміняє чинну чергу на нову.  
    
Примітка:
* _Перший гравець з нової черги буде встановлений як теперішній, і доступний в `players.current_player`_

</details>  

___

___
### PLAYER

_Інформація про гравця, і кількість кроків_

<details>
  <summary>📂 Розгорнути</summary> 

___

#### - Отримати роль. `player.role`:   
```python
@property
def role(self) -> Role
```  
Повертає роль гравця

___

#### - Отримати символ. `player.symbol`:   
```python
@property
def symbol(self) -> SymbolBase
```  
Повертає об'єкт класу Symbol гравця

___

#### - Отримати кількість кроків гравця. `player.count_steps`:   
```python
@property
def count_steps(self) -> int
```  
Повертає кількість зроблених кроків гравця

___

#### - Це андроїд? `player.is_android`:   
```python
@property
def is_android(self) -> bool
```  
Повертає True якщо гравець з роллю `Role.ANDROID`  
Інакше - False

___

#### - Це юзер? `player.is_user`:  
```python
@property
def is_user(self) -> bool
```  
Повертає True якщо гравець з роллю `Role.USER`  
Інакше - False

___

#### - Додати крок для гравця. `player.add_count_step`:  
```python
def add_count_step(self)
```  
Додає +1 до лічильника кроків гравця  

Примітка:
* Цей метод автоматично викликається в `table.set_symbol_cell`

___

___
</details>  

___
___

### GAME STATE
...

___
___
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
* AI алгоритм розуміє, що наступний хід для суперника ймовірно збере виграшну комбінацію, тому перекриває його

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
___
