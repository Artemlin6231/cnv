# cnv
Файл make.sh скачивает необходимые библиотеки(из requirements.txt) и запускает скрипт inherited.sh
Команда для исполнения: ./make.sh parents1.txt parents2.txt child.txt n name
где n - частота, отсекающая все cnv, которые выше и name - имя файлов
На выходе будет график зависимости наследованных признаков от фильтрующей частоты в формате pdf, и csv-файл ненаследованных cnv при фильрующей частоте n
