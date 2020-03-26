from utils.files import get_files
from pathlib import Path
from typing import Union


def ljspeech(path: Union[str, Path]):
    txt_file = get_files(path, extension='.csv')

    assert len(txt_file) == 1

    text_dict = {}

    with open(txt_file[0], encoding='utf-8') as f:
        for line in f:
            split = line.split('|')
            text_dict[split[0]] = split[-2]

    print('-' * 20 + 'Text dict' + '-' * 20)
    print(text_dict)
    return text_dict
