#то что ниже обязательно заполнить своими данными
proxy_use = 0 #  0 - не использовать, 1 - прокси без ссылки , 2 - прокси со ссылкой для смены ip
proxy_login = 'pludg74'
proxy_password = 'a2d0'
proxy_address = 'noxy.com'
proxy_port = '199'
proxy_changeIPlink = "h04"


#то что ниже желательно настроить под себя
minimal_need_balance = 0.01 # минимальный баланс на кошельке, который должен быть, чтобы начать с ним работу
bridge_all_money = True # True  если хотите перевести максимум из доступной суммы. False - будут действовать параметры ниже
ostavit_nativ = 0.001 # указывается в нативном токене сколько оставить на кошельке. Обязательно заложите сюда комиссию сети необходимую на отправку! Чтобы вывести токены с оптимизма указывайте в этом параметре хотя бы 0,0001. в остальных сетях можно от нуля.
bridge_min = 0.005  # ETH  в орбитре минимум   0.005 к этому прибавится комиссия моста 0,0015
bridge_max = 0.009  # ETH


#укажите паузу в работе между кошельками, минимальную и максимальную. 
#При смене каждого кошелька будет выбрано случайное число. Значения указываются в секундах
timeoutMin = 1 #минимальная 
timeoutMax = 3 #максимальная
#задержки между операциями в рамках одного кошелька
timeoutTehMin = 1 #минимальная 
timeoutTehMax = 2 #максимальная

max_gas_price = 100 #максимальная цена газа в сети эфир при которой выполняются транзакции . если будет больше то скрипт будет ждать когда цена снизится


#то что ниже можно менять только если понимаешь что делаешь
proxies = { 'all': f'http://{proxy_login}:{proxy_password}@{proxy_address}:{proxy_port}',}
if proxy_use:
    request_kwargs = {"proxies":proxies, "timeout": 120}
else:
    request_kwargs = {"timeout": 120}
gas_kef=1.2 #коэфициент допустимого расхода газа на подписание транзакций. можно выставлять от 1.3 до 2


# conf = {'rpc': 'https://api.avax.network/ext/bc/C/rpc','type':2,'scan':'https://snowtrace.io/tx/'}
# conf = {'rpc': 'https://arb1.arbitrum.io/rpc','type':2,'scan':'https://arbiscan.io/tx/'}
conf = {'rpc': 'https://rpc.ankr.com/optimism','type':2,'scan':'https://optimistic.etherscan.io/tx/'}
# conf = {'rpc': 'https://rpc.ankr.com/scroll','type':0,'scan':'https://scrollscan.com/tx/'}
# conf = {'rpc': 'https://rpc.ankr.com/base','type':2,'scan':'https://basescan.org/tx/'}
# conf = {'rpc': 'https://rpc.linea.build','type':2,'scan':'https://lineascan.build/tx/'}
# conf = {'rpc': 'https://rpc.ankr.com/polygon_zkevm','type':0,'scan':'https://zkevm.polygonscan.com/tx/'}
# conf = {'rpc': 'https://rpc.ankr.com/arbitrumnova','type':2,'scan':'https://nova.arbiscan.io/tx/'}
# conf = {'rpc': 'https://rpc.ftm.tools/','type':2,'scan':'https://ftmscan.com/tx/'}
# conf = {'rpc': 'https://bscrpc.com','type':0,'scan':'https://bscscan.com/tx/'}
# conf = {'rpc': 'https://polygon-rpc.com/','type':2,'scan':'https://polygonscan.com/tx/'}
conf.update({'eth': 'https://rpc.ankr.com/eth'})


