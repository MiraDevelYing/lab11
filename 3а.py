#3 а) Дан двійковий файл f, компоненти якого є цілими ненульовими числами, причому кількість від'ємних чисел
# дорівнює кількості додатних, а загальне число компонентів кратне 5. Використовуючи допоміжний файл h, переписати в
# порядку проходження компоненти файлу f в файл g - три додатних, три від'ємних, три додатних, три від'ємних і так далі.
# Дудук Вадим 122-Г

from random import *
import struct


def main():
    def randomNumbers():
        
        with open("f.txt", mode="wb") as f:
            array = []
            for i in range(30):
                array.append(randint(1, 100))
                array.append(randint(-100, -1))
            
            shuffle(array)
          
            f.write(struct.pack("60i", *array))

    randomNumbers()

    with open("f.txt", mode="rb") as file_f:
        with open("g.txt", mode="w") as file_g:
            with open("h.txt", mode="w") as file_h:
               
                try:
                    file_h.write(' '.join(map(str, struct.unpack("60i", file_f.readline()))))
                except struct.error:
                    main()
            with open("h.txt", mode="r") as file_h:
               
                numbers = list(map(int, file_h.readline().split()))
               
                id_, n, len_num = 0, 0, 0
                
                minus = True
               
                arr = []
                while True:
                    
                    if (numbers[id_] < 0) and minus and (n < 3):
                        
                        arr.append(str(numbers[id_]))
                    
                    elif (numbers[id_] > 0) and (not minus) and (n < 3):
                       
                        arr.append(str(numbers[id_]))
                    else:
                        id_ += 1
                        continue
                  
                    numbers.pop(id_)
                    id_ = 0
                    n += 1
                    len_num += 1

                    
                    if n == 3:
                        n = 0
                        minus = not minus

                  
                    if len_num == 60:
                        break
            
            file_g.write(', '.join(arr))


if __name__ == '__main__':
    main()
