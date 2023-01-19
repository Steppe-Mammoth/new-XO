# XO Tic-Tac-Toe

## Основні можливості:
+ **Можливо додати скільки завгодно гравців**

+ **Можливо створити ігрову таблицю любого розміру**:
+ + *Задавши параметри **рядка**, **стовбця** і **розмір виграшної комбінації** на свій смак*

+ *Штучний інтелект не повторює себе і працює по різним сценаріям*

+ *Додавайте свій функціонал успадковуючись від потрібних класів*


## Знайомство з біблеотекою
Створимо... 3 гравця! і призначемо кожному штучний інтелект `role=Player.Role.ANDROID`
Зараз буде баталія ботів, поглянемо на цю кібер разборку

```python
from game import TableParam, TableDefault, GameConsole, Player, Players, SymbolBase

p1 = Player(name="ANDROID:1", symbol=SymbolBase('X'), role=Player.Role.ANDROID)
p2 = Player(name="ANDROID:4", symbol=SymbolBase('I'), role=Player.Role.ANDROID)
p3 = Player(name="ANDROID:3", symbol=SymbolBase('K'), role=Player.Role.ANDROID)

# p4 = Player(name="PLAYER:2", symbol=SymbolBase('O'), role=Player.Role.USER)

players = Players(players=[p1, p2, p3])
table = TableDefault(param=TableParam(10, 10, 7))

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

___Це цікаво звісно, можна створити 100 ботів на 1000х1000 полі, але підемо далі___

### Перейдемо до основного API
...
