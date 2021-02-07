# SII_DS_Labs
1 лабораторная работа с дополнением для 2 лабораторной работы (атрибуты листьев) представлена на изображении Ontologia.jpg. Тема - онтология оружия из игры Dark Souls.
Во 2 лабораторной работе были реализованы вычисления Манхеттенского расстояния, Евклидова расстояния, близости по дереву и коэффициента корреляции. отдельные функции вучислений объеденены в функцию lab2, которая принимае дерево онтологии и список листьев, вызывает отдельные функции вычислений и печатает результаты вычислений.
В 3 лабораторной работе реализована коллаборативная фильтрация. ранжирование листьев базируется на опыте других игроков (использовании ими того или иного оружия), который хранится в таблице Book1.xlsx. Резльтатом является вывод списка оружий состояший из 5 предметов наиболее подходящих для игрока, исходя из оружия, название которого он ввёл. 3 лабораторная работа реализована в функции lab3
В 4 лабораторной работе реализована контентно-ориентированная фильтрация. Фильтрация реализована на основе разделения предметов по тематическим группам, информация о которых хранится в Book2.xlsx. Резльтатом является вывод списка оружий состояший из 5 предметов наиболее подходящих для игрока, исходя из оружия, название которого он ввёл. 3 лабораторная работа реализована в функции lab4
В 5 лабораторной работе реализован подбор по параметрам. при выполнении функции lab5 "игрок" вводит требуемые параметры (в случае диаппазона - 2 параметра подряд, сначала нижняя граница, после верхняя), после чего происходит подбор. При нахождении подходящих предметов выводится их список, если требуемые предметы не найдены выводится сообщение об этом и список из 5 элементов, наиболее подходящих под параметры.
6-7 лабораторные работы объединяют предыдущие лабораторные работы в диалоговую систему формата вопрос-ответ. Диалог реализован от лица персонажа "Хранительница Костра", но отличается от реального характера персонажа, показанного в игре. Присутствует вариативность сообщений предложения вариантов действия, сообщений о неверном вводе команды и сообщений о необнаружении требуемого оружия. так же есть вариативность ввода команд. Специфика темы предполагает, что оружия часто имеют сходные, а порой и почти одинаковые названия, потому было решено, что вариативность ввода названий оружия повредит функционалу и не была реализована. варианты сообщений представлены в файле dictionari.py, диалог начинается от стартовой функции start и частично присутствует в остальных функциях, так как в них происходит запрашивание тех или иных параметров или же их вывод.
9 лабораторная работа реализована в файле лаб9(2).jpg 
ДИСКЛЕЙМЕР
Характер куклы взят из игры Bloodborn. её характер и поведение смоделированы на основе статьи https://bloodborne.fandom.com/ru/wiki/Кукла#14, фразы взяты там же и применены по подходящим ситуациям с некоторыми изменениями для большей ситуативной уместности.