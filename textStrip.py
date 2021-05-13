import os
import re


def main():
    dir_path = 'text_files'
    new_dir_path = 'results'
    load_data(dir_path, new_dir_path)


def load_data(in_path, out_path):
    for text_file in os.listdir(in_path):
        try:
            with open(f'{in_path}/{text_file}', 'r') as file_object:
                data = strip_chars(file_object.read())
                save_to_txt(data, text_file, out_path)
                file_object.close()

        except FileNotFoundError:
            print("Input directory not found. Check the input path variable")
            if not file_object.closed:
                print('File is not closed.')


def strip_chars(text):
    my_re = re.compile(u'['
                       u'\U0001F300-\U0001F64F'
                       u'\U0001F680-\U0001F6FF'
                       u'\u2600-\u26FF\u2700-\u27BF]+',
                       re.UNICODE)
    data = my_re.sub('', text)

    to_replace = ['\\n', '\\u', '\\f']
    for char in to_replace:
        data = data.replace(char, '')

    return data


def save_to_txt(data, filename, path):
    try:
        with open(f'{path}/{filename}', 'w') as output_file:
            output_file.write(data)

    except FileNotFoundError:
        print("Output directory not found. Check the output path variable")


if __name__ == '__main__':
    main()
