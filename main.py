import decimal
from statistics import mean
import time
from web3 import Web3
import requests
import random
from datetime import datetime
import config
from config import conf
import fun
from fun import *




current_datetime = datetime.now()
print(f"\n\n {current_datetime}")
print(f'============================================= Плюшкин Блог =============================================')
print(f'subscribe to : https://t.me/plushkin_blog \n============================================================================================================\n')


keys_list = []
with open("private_keys.txt", "r") as f:
    for row in f:
        private_key=row.strip()
        if private_key:
            keys_list.append(private_key)

random.shuffle(keys_list)
i=0
for private_key in keys_list:
    string_list = private_key.split("	")
    private_key = string_list[0]
    wallet_out = string_list[1] if len(string_list) > 1 else ""
    if wallet_out=="":
        log("не указан кошелек куда переводить токены. в файле с приватными ключами укажите на против каждого приватника через табуляцию адресс куда перевести токены") 
        continue
    i+=1
    if config.proxy_use == 2:
        while True:
            try:
                requests.get(url=config.proxy_changeIPlink)
                fun.timeOut("teh")
                result = requests.get(url="https://yadreno.com/checkip/", proxies=config.proxies)
                print(f'Ваш новый IP-адрес: {result.text}')
                break
            except Exception as error:
                print(' !!! Не смог подключиться через Proxy, повторяем через 2 минуты... ! Чтобы остановить программу нажмите CTRL+C или закройте терминал')
                time.sleep(120)

    try:
        web3 = Web3(Web3.HTTPProvider(conf['rpc'], request_kwargs=config.request_kwargs))
        account = web3.eth.account.from_key(private_key)
        wallet = account.address    
        balance = web3.eth.get_balance(wallet)
        balance_decimal = float(Web3.from_wei(balance, 'ether'))
    except Exception as error:
        log_error(f'Ошибка подключения в ноде: {error}')   

    log(f"I-{i}: Начинаю работу с {wallet}")
    if balance_decimal < config.minimal_need_balance:
        log(f"low balance , меньше {config.minimal_need_balance}")          
        continue

    ostavit_nativ = random.uniform(config.ostavit_nativ[0], config.ostavit_nativ[1])
    if config.bridge_all_money:
        amount = balance_decimal - ostavit_nativ * config.gas_kef
    else:
        amount = random.uniform(config.bridge_min,config.bridge_max)
    if balance_decimal < amount + ostavit_nativ:
        log(f" low balance")          
        continue

    value = web3.to_wei(amount, 'ether')

    # ожидает подходящий газ
    wait_gas_price_eth()

    try:
        wallet_out = web3.to_checksum_address(wallet_out)
        gasPrice = web3.eth.gas_price

        transaction = {
            "chainId": web3.eth.chain_id,
            'from': wallet,
            'to': wallet_out,
            'value':value,
            'gasPrice': gasPrice,
            'nonce': web3.eth.get_transaction_count(wallet),
        }
        gasLimit = int(web3.eth.estimate_gas(transaction)* config.gas_kef)
        transaction['gas'] = gasLimit
        if conf['type']:
            maxPriorityFeePerGas = web3.eth.max_priority_fee
            fee_history = web3.eth.fee_history(10, 'latest', [10, 90])
            baseFee=round(mean(fee_history['baseFeePerGas']))
            maxFeePerGas = maxPriorityFeePerGas + round(baseFee * config.gas_kef)

            del transaction['gasPrice']
            transaction['maxFeePerGas'] = maxFeePerGas
            transaction['maxPriorityFeePerGas'] = maxPriorityFeePerGas



        signed_txn = web3.eth.account.sign_transaction(transaction, private_key)
        txn_hash = web3.to_hex(web3.eth.send_raw_transaction(signed_txn.rawTransaction))
        tx_result = web3.eth.wait_for_transaction_receipt(txn_hash)

        if tx_result['status'] == 1:
            log_ok(f'send OK: {conf["scan"]}{txn_hash}')
            fun.delete_private_key_from_file("private_keys", private_key)
            fun.delete_wallet_from_file("send_false_pk", private_key)
        else:
            log_error(f'send false: {conf["scan"]}{txn_hash}')
            save_wallet_to("send_false_pk", private_key)
            # keys_list.append(private_key)
        


    except Exception as error:
        fun.log_error(f'send false: {error}')
        save_wallet_to("send_false_pk", private_key)
        # keys_list.append(private_key)



    timeOut()
    

    
log("Ну типа все, кошельки закончились!")