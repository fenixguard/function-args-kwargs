

class Contact:

    def __init__(self, first_name, second_name, phone_number, favorite_contact=False, **kwargs):
        self.first_name = first_name
        self.second_name = second_name
        self.phone_number = phone_number
        self.favorite_contact = favorite_contact
        self.additional_information = ''
        if kwargs:
            for key, value in kwargs.items():
                self.additional_information += f'\t\t{key}: {value}\n'
        else:
            self.additional_information = '\t\tОтсутствует'

    def __str__(self):
        return '\n'.join([f'Имя: {self.first_name}',
                          f'Фамилия: {self.second_name}',
                          f'Телефон: {self.phone_number}',
                          'В избранных: да' if self.favorite_contact else 'В избранных: нет',
                          'Дополнительная информация:',
                          f'{self.additional_information}'])


class PhoneBook:

    def __init__(self):
        pass
