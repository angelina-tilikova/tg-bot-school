from aiogram import Bot, Dispatcher, types, F, html
from aiogram.enums import ParseMode



# ToDo: 
text1 = ''' Большинство из вас не задумывается когда произносит: 
"Да я на все сто проц уверен, что к/р не будет!". 
Но многие ли помнят-знают что такое проценты? \n
<b>Сотая часть метра – сантиметр 1/100м.
Сотая часть центнера – килограмм 1/100ц.
Сотая часть рубля – копейка 1/100руб. </b>\n
Люди давно заметили, что сотые доли величин удобны в практической деятельности. 
Поэтому для них было придумано специальное название и обозначение процент.
Записи 2%, 5% читают: «Два процента», «Пять процентов».
Математическим знаком процент записывается так - %.\n
<b>Один процент </b> – это одна сотая часть от какого-либо числа. \n
Тоесть, чтобы получить 1% от всего числа, нам надо разделись все число на 100, \n 1) n:100%. \n
А чтобы от числа получить не 1%, а например 58%? Для этого полученный 1% умножаем
на 58,  \n2) (n:100%)*58%. \n Но можно ли сократить количество махинаций проводимых над числом?
Да. Например, найдем 43% от числа 732. Для этого 43% разделим на 100%,  \n1) 43:100 = 0.43.\n
Далее число 732 умножаем на полученный результат от 1 действия,  \n2) 732 * 0.43 = 314.76.\n
Правда, возникает вопрос:"Тут же столько же действий, как и в первом варианте решения?".
Возможно, но все таки во втором варианте решения можно опустить 1 действие, посчитать в уме, 
думаю для многих легко число которое меньше ста поделить на сто.'''



text2 = '''
👉 <b>разность квадратов:</b> a^2 - b^2 = (a - b)*(a + b)
👉 <b>разность кубов:</b>      a^3 - b^3 = (a - b)(a^2 + ab + b^2)
👉 <b>сумма кубов:</b>          a^3 + b^3 = (a + b)(a^2 - ab + b^2)
👉 <b>квадрат суммы:</b>       (a + b)^2 = a^2 + 2ab + b^2
👉 <b>квадрат разности:</b>   (a - b)^2 = a^2 - 2ab + b^2
👉 <b>куб разности:</b>       (a - b)^3 =  a^3 - 3a^2b + 3ab^2 - b^3 
👉 <b>куб суммы:</b>          (a + b)^3 =  a^3 + 3a^2b + 3ab^2 + b^3
'''