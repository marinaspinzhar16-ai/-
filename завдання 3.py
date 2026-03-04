import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація colorama
init(autoreset=True)


def print_directory_structure(path: Path, indent: str = ""):
    try:
        for item in sorted(path.iterdir()):
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}📂 {item.name}{Style.RESET_ALL}")
                print_directory_structure(item, indent + "   ")
            else:
                print(f"{indent}{Fore.GREEN}📜 {item.name}{Style.RESET_ALL}")
    except PermissionError:
        print(f"{indent}{Fore.RED}Немає доступу до {path.name}{Style.RESET_ALL}")


def main():
    # Перевірка наявності аргументу
    if len(sys.argv) != 2:
        print(Fore.RED + "Будь ласка, вкажіть шлях до директорії.")
        print("Приклад: python hw03.py /шлях/до/директорії")
        sys.exit(1)

    directory_path = Path(sys.argv[1])

    # Перевірка існування шляху
    if not directory_path.exists():
        print(Fore.RED + "Вказаний шлях не існує.")
        sys.exit(1)

    if not directory_path.is_dir():
        print(Fore.RED + "Вказаний шлях не є директорією.")
        sys.exit(1)

    print(f"{Fore.YELLOW}📦 {directory_path.name}{Style.RESET_ALL}")
    print_directory_structure(directory_path)


if __name__ == "__main__":
    main()
