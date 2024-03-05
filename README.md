# Автор
PLushkin https://t.me/plushkin_blog        

**На чай с плюшками автору:**
Полигон, БСК, Арбитрум - любые токены - `0x79a266c66cf9e71Af1108728e455E0B1D311e95E`

Трон TRC-20 только USDT, остальное не доходит - `TEZG4iSmr31wWnvBixKgUN9Aax4bbgu1s3`

# Чё делает
Позволяет выводить все нативнавные токены или не все, а столько сколько вы укажете.  с каждого кошелька на отдельный адресс.
Кошелек куда переводить указывается так м же в приваткейс , через табуляцию после приватника. Для каждого приватника свой кошелек вывода


# Настройка
В настройках в низу выберете или укажите свою RPC , какую укажете из той сети и будет выводиться.
Есть ограничение на газ в сети эфира. т.е. вы указываете максимальный потолок при каком газа в сети эфира можно делать транзакции.
Т.е. выводим из арбитрума, а газ проверяется все равно в сети эфира.

# Установка и запуск:

Linux/Mac - https://www.youtube.com/watch?v=8rJ-96cPFwU
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python main.py
```
Windows - https://www.youtube.com/watch?v=EqC42mnbByc
```
pip install virtualenv
virtualenv .venv
.venv\Scripts\activate
pip install -r requirements.txt

python main.py
```


