### Project 1. Guess a number             
Game: The computer guesses an integer from 1 to 100. You need to write a program that guesses the guessed number in the minimum number of attempts.                                                                    
Run the game 1000 times and count the average number of attempts when searching for the hidden number.                 
                                        
**Solution**
This project was completed using the binary search algorithm.                                   
The algorithm compares the middle element of the sorted array with the element it is looking for to decide where to continue searching. If the target element is larger than the middle element, it cannot be located in the first half of the collection, so the first half is discarded and only the second half of the array remains for consideration. Thus, the number of possible options is reduced by at least half with each attempt.                          
                          
_________________________________                       
                                   
## Угадай число!             

Игра: Компьютер загадывает целое число от 1 до 100. Нужно написать программу, которая угадывает загаданное число наименьшим количеством попыток.                                   
Запустить игру 1000 раз и посчитать среднее количество попыток при поиске загаданного числа.                                                                   
                                  
**Решение**
Данный проект выполнен с помощью алгоритма бинарного поиска.                 
Алгоритм сравнивает средний элемент отсортированного массива с элементом, который он ищет, чтобы решить, где продолжить поиск. Если целевой элемент больше среднего элемента – он не может быть расположен в первой половине коллекции, поэтому первая половина отбрасывается и в рассмотрении остается только вторая половина массива. Таким образом количество возможных вариантов с каждой попыткой сокращается как минимум вдвое.
