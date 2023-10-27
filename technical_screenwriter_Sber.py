import json
from _datetime import datetime as dt
'''Задание
По каждой операции есть:
        - date - информация о дате совершения операции
        - state - статус перевода (EXECUTED - выполнена, CANCELED - отменена)
        - operationAmount - сумма операции и валюта
        - description - описание типа перевода
        - from - откуда
        - to - куда
Задача
Вывести на экран список из 5 последних совершенных (выполненных) операций клиента в формате:
        <дата перевода> <описание перевода>
        <откуда> -> <куда>
        <сумма перевода> <валюта>
    Пример для одной операции:
        14.10.2018 Перевод организации
        Visa Platinum 7000 79** **** 6361 -> Счет **9638
        82771.72 руб.
Условия
• решение должно представлять из себя скрипт на языке python
• вывести последние 5 выполенных (EXECUTED) операций на экран
• операции разделены пустой строкой
• дата перевода должна быть в формате ДД.ММ.ГГГГ (пример 14.10.2018)
• сверху списка должны быть самые последние операции (по дате)
• номер карты должен маскироваться и не отображаться целиком, в формате XXXX XX** **** XXXX (видны первые 6 цифр и
 последние 4, разбито по блокам по 4 цифры, разделенных пробелом)
• номер счета должен маскироваться и не отображаться целиком, в формате **XXXX (видны только последние 4 цифры номера счета)'''
with open('operations.json', encoding='utf-8') as f:
    data = json.load(f)
    operations = 0
    for op in data:
        if op['state'] == 'EXECUTED':

            date_operation = f"{dt.strftime(dt.strptime(op['date'], '%Y-%m-%dT%H:%M:%S.%f'),'%d.%m.%Y')} {op['description']}"
            operation_from = '-> '
            operation_to = op['to'].rsplit(' ', 1)
            amount_cur = f"{op['operationAmount']['amount']} {op['operationAmount']['currency']['name']}"

            try:
                operation_from = op['from'].rsplit(' ', 1)
                if len(operation_from[1]) < 20:
                    operation_from = operation_from[0] + f' {operation_from[1][:4]} {operation_from[1][4:6]}' + '** ' + '**** ' + operation_from[1][-4:] + ' -> '
                else:
                    operation_from = operation_from[0] + ' **' + operation_from[1][-4:] + ' -> '
            except KeyError:
                print('Это вклад, о таких операциях в задании ничего не сказано, но я выведу')



            if len(operation_to[1]) < 20:
                operation_to = operation_to[0] + operation_to[0] + f' {operation_to[1][:4]} {operation_to[1][4:6]}' + '** ' + '**** ' + operation_to[1][-4:]
            else:
                operation_to = operation_to[0] + ' **' + operation_to[1][-4:]

            print(date_operation, operation_from + operation_to, amount_cur+'\n', sep='\n')

            operations += 1
            if operations == 5:
                break
