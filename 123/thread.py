from threading import Thread

def traficlights(product):
    for i in product:
        print(f'Горит {i} светофор')

all_products = ['Красный', 'Желтый' , 'Зеленый']

t1 = Thread(target=traficlights, args=(all_products,))
t1.start()