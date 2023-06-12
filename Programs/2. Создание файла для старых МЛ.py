import time


createdNumber = int(time.time())
series = input('Номер серии: ')
printOrderNumber = input('Номер заказа на печать: ')
firstNumber = input('От какого числа начнем счет: ')
quantityOfTickets = input('Сколько билетов нужно: ')
newTicketsML = input('Грузим билеты для новых билетов МЛ? д или н')

quantity = int(quantityOfTickets)
lastNumber = int(firstNumber) + quantity

HEADER = 'ticketNumber;nominalCost;lotteryName;amountWin;checkCode;series;printOrderNumber;partner;salePlace;cashed;sold;packNumber;boxNumber\n'
TEXT = f';100;моменталка;500;123456789;{series};{printOrderNumber};;;false;false;Trixie {createdNumber};Trixie {createdNumber}\n'
SCRIPT = f'SELECT * FROM instant_handler.instant_ticket\nwhere box_number = \'Trixie {createdNumber}\''

file = open('Билеты МЛ для загрузки.txt', 'w', encoding='utf-8')
file.write(HEADER)
file = open('Билеты МЛ для загрузки.txt', 'a', encoding='utf-8')

for i in range(int(firstNumber),lastNumber):
    if int(firstNumber[0]) == 0:
        file.write(f'0{i}{TEXT}')
    else:
        file.write(f'{i}{TEXT}')

if newTicketsML == 'д':
    file = open('Скрипт для изменения билетов в БД.txt', 'w', encoding='utf-8')
    file.write(SCRIPT)
elif newTicketsML == 'н' or newTicketsML == '':
    print('Ну, ок. Сегодня без скрипта')
    time.sleep(3)
else:
    print('Русскими буквами было написано "д" или "н" -_-')
    time.sleep(3)
file.close()
