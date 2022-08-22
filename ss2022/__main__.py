from src.CSVPrinter import CSVPrinter

if __name__ == '__main__':
    printer = CSVPrinter("sample.csv")
    l = printer.read()
    print(l)

