#!/usr/bin/env python3
# -*- config: utf-8 -*-

from dataclasses import dataclass, field
from typing import List


class IllegalTimeError(Exception):
    def __init__(self, time, message="Запрещенное время : "):
        self.time = time
        self.message = message
        super(IllegalTimeError, self).__init__(message)

    def __str__(self):
        return f
        return f"{self.time} -> {self.message}"


class UnknownCommandError(Exception):
    def __init__(self, command, message="Unknown command"):
        self.command = command
        self.message = message
        super(UnknownCommandError, self).__init__(message)

    def __str__(self):
        return f
        return f"{self.command} -> {self.message}"

@dataclass(frozen=True)
class poez:
    name: str
    num: str
    time: str


@dataclass
class Staff:
    poezd: List[poez] = field(default_factory=lambda: [])

    def add(self, name, num, time):
        self.poezd.append(
            poez(
                name=name,
                num=num,
                time=time
            )
        )

        self.poezd.sort(key=lambda poez: poez.num)

    def __str__(self):
        # Заголовок таблицы.
        table = []
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 17
        )
        table.append(line)
        table.append(
            '| {:^4} | {:^30} | {:^20} | {:^17} |'.format(
                "№",
                "Пункт назначения",
                "Номер поезда",
                "Время отправления"
            )
        )
        table.append(line)


        for idx, poez in enumerate(self.poezd, 1):
            table.append(
                '| {:>4} | {:<30} | {:<20} | {:>17} |'.format(
                    idx,
                    poez.name,
                    poez.num,
                    poez.time
                )
            )

        table.append(line)

        return '\n'.join(table)

    def select(self, times):

        parts = command.split(' ', maxsplit=2)
        times = int(parts[1])
        result = []

        for poez1 in self.poezd:
            if poez1.time == times:
                result.append(poezd)

        return result

    def load(self, filename):
        with open(filename, 'r', encoding='utf8') as fin:
            xml = fin.read()
        parser = ET.XMLParser(encoding="utf8")
        tree = ET.fromstring(xml, parser=parser)
        self.poezd = []

        for poez_element in tree:
            name, num, time = None, None, None

            for element in poez_element:
                if element.tag == 'name':
                    name = element.text
                elif element.tag == 'num':
                    num = element.text
                elif element.tag == 'time':
                    time = element.text

                if name is not None and num is not None \
                        and time is not None:
                    self.poezd.append(
                        poez(
                            name=name,
                            num=time,
                            time=time
                        )
                    )

    def save(self, filename):
        root = ET.Element('poezd')
        for poez in self.poezd:
            poez_element = ET.Element('poez')

            name_element = ET.SubElement(poez_element, 'name')
            name_element.text = poez.name

            num_element = ET.SubElement(poez_element, 'num')
            num_element.text = poez.num

            time_element = ET.SubElement(poez_element, 'time')
            time_element.text = str(poez.time)

            root.append(poez_element)

        tree = ET.ElementTree(root)
        with open(filename, 'wb') as fout:
            tree.write(fout, encoding='utf8', xml_declaration=True)