from calculator_factories import *
from class_calculator import Calculator


def main():
    root = make_root('Calculadora')
    label = make_label(root)
    display = make_display(root)
    buttons = make_button(root)

    calculator = Calculator(root, label, display, buttons)
    calculator.start()


if __name__ == '__main__':
    main()
