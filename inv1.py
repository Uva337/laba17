#!/usr/bin/env python3
# -*- config: utf-8 -*-

# Использовать словарь, содержащий следующие ключи: название пункта назначения; номер
# поезда; время отправления. Написать программу, выполняющую следующие действия:
# ввод с клавиатуры данных в список, состоящий из словарей заданной структуры; записи должны
# быть упорядочены по номерам поездов;
# вывод на экран информации о поезде, номер которого введен с клавиатуры; если таких поездов нет,
# выдать на дисплей соответствующее сообщение.



from dataclasses import dataclass, field
import logging
import sys
import xml.etree.ElementTree as ET
import modul


if __name__ == '__main__':

    logging.basicConfig(
        filename='poezd.log',
        level=logging.INFO,
        format='%(asctime)s %(levelname)s:%(message)s'
    )
    staff = Staff()

    while True:

        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':

            name = input("Название пункта назначения: ")
            num = input("Номер поезда: ")
            time = input("Время отправления: ")

            staff.add(name, num, time)
            logging.info(
                f"Добавлено название: {name}, "
                f"Добавлен номер: {num}, "
                f"Добавлено время {time}. "
            )

        elif command == 'list':
            print(staff)
            logging.info("Отображен список поездов.")

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=2)
            selected = staff.select(parts[1])

            if selected:
                for c, poez in enumerate(selected, 1):
                    print(
                        ('Название:', poez.name),
                        ('Номер :', poez.num, ),
                        ('Время:', poez.time)
                    )
                logging.info(
                    f"Найден путь с названием {poez.name}"
                )
            else:
                    print("Таких названий нет!")
                    logging.warning(
                        f"Путь с названием {poez.name} не найден.")
        elif command.startswith('load '):
            parts = command.split(' ', maxsplit=1)
            staff.load(parts[1])
            logging.info(f"Загружены данные из файла {parts[1]}.")
        elif command.startswith('save '):
            parts = command.split(' ', maxsplit=1)
            staff.save(parts[1])
            logging.info(f"Сохранены данные в файл {parts[1]}.")

        elif command == 'help':

            print("Список команд:\n")
            print("add - добавить поезд;")
            print("list - вывести список поездов;")
            print("select <номер поезда> - запросить информацию о выбранном времени;")
            print("help - отобразить справку;")
            print("load <имя файла> - загрузить данные из файла;")
            print("save <имя файла> - сохранить данные в файл;")
            print("exit - завершить работу с программой.")
        else:
            raise UnknownCommandError(command)
    except Exception as exc:
        logging.error(f"Ошибка: {exc}")
        print(exc, file=sys.stderr)