#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from pathlib import Path


def list_files(path, show_size, only_dir, size=""):
    for item in path.iterdir():
        if item.is_file() and not (only_dir):
            if show_size:
                size = item.stat().st_size
            print(f"{item.name} {size}")
        elif item.is_dir():
            if show_size:
                size = item.stat().st_size
            print(f"{item.name}/ {size}")

            list_files(item, show_size, only_dir)


def main():
    parser = argparse.ArgumentParser(
        description="Утилита для отображения дерева каталогов и файлов"
    )
    parser.add_argument("path", nargs="?", default=".", help="Путь к каталогу")
    parser.add_argument(
        "-d", "--dir", default=False, help="Показывать содержимое директории"
    )
    parser.add_argument(
        "-s", "--showsize", default=False, help="Показать размер файлов"
    )
    args = parser.parse_args()

    path = Path(args.path)
    only_dir = args.dir
    show_size = args.showsize

    if path.is_dir():
        list_files(path, show_size, only_dir)
    else:
        print(f"Путь {args.path} не существует или не является каталогом")


if __name__ == "__main__":
    main()
