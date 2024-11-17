import enchant
import tkinter as tkinter
from tkinter import filedialog as filedialog


class CaesarsCipher:
    def __init__(self):

        self.alfavit = ('ABCDEFGHIJKLMNOPQRS'
                        'TUVWXYZabcdefghijklmnopqrs'
                        'tuvwxyz1234567890 !?.')
        self.key = 0
        self.decrypt_smeshenie = -1 * len(self.alfavit)
        self.encrypt_smeshenie = 0
        self.decrypted_word = ''
        self.key = 0

    def search_dictionary(self, decrypted_word):
        # проверка слова

        dictionary = enchant.Dict("en_US")
        decrypted_word_new = ''
        decrypted_word_new_list = []

        wolds_list = decrypted_word.split(' ')

        for wolds_list_id in range(len(wolds_list)):
            if len(wolds_list[wolds_list_id]) > 0:
                if dictionary.check(wolds_list[wolds_list_id]):
                    decrypted_word_new += wolds_list[wolds_list_id] + ' '
                    decrypted_word_new_list.append(wolds_list[wolds_list_id])
                    if (len(decrypted_word_new_list)) > 3:
                        self.decrypted_word = decrypted_word
                        return decrypted_word

    def decrypt(self, message_decrypt):
        # расшифровка

        while self.decrypt_smeshenie != 0:
            # print(smeshenie)
            decrypted_word = ''
            for i in message_decrypt:
                mesto = self.alfavit.find(str(i))

                if (mesto -
                        abs(self.decrypt_smeshenie) < 0):
                    new_mesto = (mesto -
                                 abs(self.decrypt_smeshenie) +
                                 len(self.alfavit))
                else:
                    new_mesto = mesto + self.decrypt_smeshenie

                decrypted_word += self.alfavit[new_mesto]

            result_search_dictionary = cipher.search_dictionary(decrypted_word)

            if len(self.decrypted_word) > 0:
                # password = ('Ключ  равен : ' +
                #          str(abs(self.decrypt_smeshenie)) + ' слово ' +
                #          passwo)
                self.key = abs(self.decrypt_smeshenie)

                return result_search_dictionary
            else:
                self.decrypt_smeshenie = self.decrypt_smeshenie + 1

    def encrypt(self, message_encrypt, key_encrypt):
        result_search_dictionary = ''

        # зашифровка
        for i in message_encrypt:
            mesto = self.alfavit.find(str(i))

            if mesto + key >= len(self.alfavit):
                new_mesto = (mesto + key_encrypt -
                             len(self.alfavit))
            else:
                new_mesto = mesto + key_encrypt
            result_search_dictionary += (
                self.alfavit)[new_mesto]
        return result


if __name__ == '__main__':
    cipher = CaesarsCipher()
    message_input = 'o3zR v..D0?yRA0R8FR8v47w0ER4.R1WdC!sLF5D'
    print(f'Идет расшифровка пароля {message_input}')
    result = cipher.decrypt(message_input)
    key = cipher.key
    print(f'{key}: {result}')

    message = ('The password to my '
               'mailbox is fBIvqX5yjw')
    key = cipher.key
    result = cipher.encrypt(message, key)
    print(f'{key}: {result}')

    root = tkinter.Tk()  # пустое родительское окно
    root.withdraw()
    directory_sorted_order = filedialog.askdirectory(
        title='Путь к файлу')
    root.destroy()  # уничтожаем родительское
    # окно
