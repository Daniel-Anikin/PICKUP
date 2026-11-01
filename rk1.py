from operator import itemgetter


class Computer:
    """Компьютер"""
    def __init__(self, id, model, price, display_class_id):
        self.id = id
        self.model = model
        self.price = price
        self.display_class_id = display_class_id


class DisplayClass:
    """Дисплейный класс"""
    def __init__(self, id, name):
        self.id = id
        self.name = name


class ComputerDisplayClass:
    """'Компьютеры дисплейного класса' (многие-ко-многим)"""
    def __init__(self, display_class_id, computer_id):
        self.display_class_id = display_class_id
        self.computer_id = computer_id


display_classes = [
    DisplayClass(1, 'дисплейный класс информатики'),
    DisplayClass(2, 'дисплейный класс программирования'),
    DisplayClass(3, 'дисплейный класс графики'),
    DisplayClass(11, 'дисплейный класс информатики (другой)'),
    DisplayClass(22, 'дисплейный класс программирования (другой)'),
    DisplayClass(33, 'дисплейный класс графики (другой)'),
]

computers = [
    Computer(1, 'Acer',          45000, 1),
    Computer(2, 'HP Pavilion',   55000, 2),
    Computer(3, 'Lenovo IdeaPad', 65000, 3),
    Computer(4, 'Asus Vivobook', 50000, 3),
    Computer(5, 'Dell Inspiron', 40000, 3),
    Computer(6, 'MacBook Air',   70000, 1),
    Computer(7, 'MSI Modern',    48000, 2),
]

computers_display_classes = [
    ComputerDisplayClass(1, 1),
    ComputerDisplayClass(2, 2),
    ComputerDisplayClass(3, 3),
    ComputerDisplayClass(3, 4),
    ComputerDisplayClass(3, 5),
    ComputerDisplayClass(1, 6),
    ComputerDisplayClass(2, 7),
    ComputerDisplayClass(11, 1),
    ComputerDisplayClass(22, 2),
    ComputerDisplayClass(33, 3),
    ComputerDisplayClass(33, 4),
    ComputerDisplayClass(33, 5),
]


def main():
    one_to_many = [(c.model, c.price, d.name)
                   for d in display_classes
                   for c in computers
                   if c.display_class_id == d.id]

    many_to_many_temp = [(d.name, cd.display_class_id, cd.computer_id)
                         for d in display_classes
                         for cd in computers_display_classes
                         if d.id == cd.display_class_id]
    many_to_many = [(c.model, c.price, dc_name)
                    for dc_name, _, comp_id in many_to_many_temp
                    for c in computers if c.id == comp_id]

    print('Задание Д1')
    res_11 = [(model, dc_name)
              for model, _, dc_name in one_to_many
              if model.endswith('r')]
    print(res_11)

    print('\nЗадание Д2')
    res_12_unsorted = []
    for d in display_classes:
        d_comps = list(filter(lambda i: i[2] == d.name, one_to_many))
        if len(d_comps) > 0:
            d_prices = [price for _, price, _ in d_comps]
            d_prices_avg = sum(d_prices) / len(d_prices)
            res_12_unsorted.append((d.name, d_prices_avg))
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nЗадание Д3')
    res_13 = {}
    for d in display_classes:
        if d.name.startswith('д'):
            d_comps = list(filter(lambda i: i[2] == d.name, many_to_many))
            d_comps_models = [x for x, _, _ in d_comps]
            res_13[d.name] = d_comps_models
    print(res_13)


if __name__ == '__main__':
    main()
