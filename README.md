# IDE-Homework

1) Я создал свой первый репозиторий на гитхабе под названием IDE-Homework. Создал файл README.md. Загрузил два файла: старый фильтр и новый.

 ![image 20](https://user-images.githubusercontent.com/94371922/142839076-6c3049e4-3064-483c-a935-79df5ce2b6d6.png)

2) Создал новый проект. 

![image](https://user-images.githubusercontent.com/94371922/142839547-278f1e3e-0c82-4d68-888b-1e1dd1adb892.png)

Устанавливаем Git в наш PyCharm. Загружаем файлы к себе.

![image](https://user-images.githubusercontent.com/94371922/142841658-a1488ec0-0606-40b1-93ef-8de65170b665.png)

3) Добавил в папку с проектом тестовое изображение.

![image](https://user-images.githubusercontent.com/94371922/142842109-030c3d3e-32b0-4f45-911c-55a05871c2e7.png)

![img](https://user-images.githubusercontent.com/94371922/142842166-bedb1e5e-666e-439a-ab1b-979f7049a976.jpg)

4) Добавил изображение в репозиторий 

![image](https://user-images.githubusercontent.com/94371922/142851983-16c0b483-e5e5-4ce6-a1b3-f531839429d0.png)

5) Запустил filter.py с помощью встроенного профилизатора cProfile. Далее, вы увидите скриншот с временем выполнения.

![image](https://user-images.githubusercontent.com/94371922/142861478-c5a31765-0826-42cf-9299-f7b41090dc0e.png)

6) Запустил old_filter.py с помощью встроенного профилизатора cProfile. Далее, вы увидите скриншот с временем выполнения.

![image](https://user-images.githubusercontent.com/94371922/142862380-a146f8b0-8b84-4440-bfc2-fecb351b5726.png)

Файл old_filter.py работает быстрее, чем filter.py, потому что большая часть времени затрачена на ввод данных с клавиатуры.

7) Создадим новый файл filter_with_filename.py, в котором уберем ручной ввод с клавиатуры. Добавим его в репозиторий.

![image](https://user-images.githubusercontent.com/94371922/142863278-1c001159-9425-48a0-9eb4-878cbdacb896.png)

![image](https://user-images.githubusercontent.com/94371922/142863344-0c083ef7-ea0d-4523-aec1-9221f7e9961c.png)

8) Запустил filter_with_filename.py с помощью встроенного профилизатора cProfile. Далее, вы увидите скриншот с временем выполнения.

![image](https://user-images.githubusercontent.com/94371922/142863528-ede1210e-7246-4375-8160-2420faa8d424.png)

Время выполнения составило 130 мс, то есть 0.13 секунды.
Обновленный фильтр работает, примерно, в 68.5 раз быстрее, чем старый фильтр. А всё из-за использования NumPy и рефакторинга кода.

Теперь покажу вам все изображения, которые получились после нашего кода.

<<Изначальная картинка, вы её видели>>

![img](https://user-images.githubusercontent.com/94371922/142864431-04891baa-bb03-4da1-bd55-bf4cd2dba35c.jpg)

<<Картинка, которая получилась после работы old_filter.py> (no comments)>

![res](https://user-images.githubusercontent.com/94371922/142864523-8aebbb49-9783-4a46-87aa-7b440b02c414.jpg)

<<Картинка, полученная работой правильного фильтра filter.py>>

![img_new](https://user-images.githubusercontent.com/94371922/142864606-64dc3bee-74c1-431c-9747-8f5faf814132.jpg)

9) К выделенным функциям напишем документацию и док-тесты.




