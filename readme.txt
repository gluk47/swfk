Это русский перевод книги "Snake Wrangling for Kids", позднее переработанной и выпущенной как "Python for kids".
Это клон репозитория https://code.google.com/p/swfk/, там книгу писал автор, Jason R Briggs.

В этом репозитории есть оригинальная книга без изменений в папке en, она как-то собирается при помощи latex и dvipdf.
В папке ru есть перевод (незаконченный, начатый с линуксовой версии для Питона 3), он собирается командой
  ./build.sh
которая вызывает xelatex и собирает все три версии книги. Можно собрать только нужную/нужные версии, так:
  ./build.sh macos

Ну и свежие собранные версии есть там же, book-linux.pdf, book-windows.pdf и book-macos.pdf (собраны из тех же исходников, которые лежат в свежем коммите).

Книга распространяется на условиях лицензии Creative Commons Attribution-Noncommercial-Share Alike 3.0 New Zealand License, что значит, что её можно читать, изменять и невозбранно распространять, но только под той же лицензией, бесплатно и обязательно указывая понятным образом авторство разных частей (как минимум, «оригинальной» и изменённой последним автором).
Подробнее тут почитайте: http://creativecommons.org/licenses/by-nc-sa/3.0/nz/deed.ru


This is an unofficial clone of LaTeX source of "Snake Wrangling for Kids"
The original repository was copied from here: https://code.google.com/p/swfk/, where it was maintained by the original book author, Jason R Briggs.

This repository contains both the original English book
and its Russian translation (with priority in translating to the Linux edition).

This work is licensed under the Creative Commons Attribution-Noncommercial-Share Alike 3.0 New Zealand License.
To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/nz or send a letter to Creative Commons, 171 Second Street, Suite 300, San Francisco, California, 94105, USA.

To build, you'll need xelatex (unlike the original book which builds with latex and dvipdf).
The easiest way to build the translated book is to go to the folder 'ru' and run:
  ./build.sh
or, for just some versions:
  ./build.sh macos linux
  ./build.sh windows
  ./build.sh help
If you input an incorrect target (e.g. 'help'), you'll get the list of all supported targets.

