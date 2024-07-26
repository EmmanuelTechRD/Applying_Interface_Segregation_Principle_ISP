from abc import ABC, abstractmethod

class IPrint(ABC):
    @abstractmethod
    def print(self, document):
        pass

class IScan(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class SimplePrinter(IPrint):
    def print(self, document):
        print(f"Imprimiendo documento desde Impresora Básica: {document}")

class MultiFunctionPrinter(IPrint, IScan):
    def print(self, document):
        print(f"Imprimiendo documento desde Impresora Multifuncional: {document}")

    def scan(self, document):
        print(f"Escaneando documento desde Impresora Multifuncional: {document}")

# Pruebas
document = "Documento de prueba"
print("\n >>>>>> Impresora Básica <<<<<< ")
simple_printer = SimplePrinter()
simple_printer.print(document)

print("\n >>>>>> Impresora Multifuncional <<<<<< ")
multi_function_printer = MultiFunctionPrinter()
multi_function_printer.print(document)
multi_function_printer.scan(document)
