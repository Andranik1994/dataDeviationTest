from os import path


class Utils:

    @staticmethod
    def input_valid_path(file_name):
        while True:
            print(f'Input path for {file_name}:')
            path_address = input()
            if path.exists(path_address):
                return path_address
            else:
                print('File does not exist try one more time !')
                continue

    @staticmethod
    def input_m_or_f():
        print("'M' or 'F'")
        value = input()
        while value not in ("M", "F"):
            print("'M' or 'F'")
            value = input()
        return value
