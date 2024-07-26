## Applying the Interface Segregation Principle (ISP)

<!-- Illustration image. -->
![Showing the practice working](https://github.com/user-attachments/assets/6ddc62dc-29b8-4915-80b5-9843441ee79a)

### Applying the Interface Segregation Principle (ISP) in the Programming 2 class at the Technological Institute of the Americas (ITLA).

### Project Purpose

This project is a practical exercise in applying the Interface Segregation Principle (ISP) from SOLID principles. The goal is to design a flexible and maintainable code structure to manage different types of printers: basic printers that only print and multifunction printers that can print and scan.

### Objectives

+ Accommodate different printer capabilities without forcing basic printers to implement unnecessary methods.
+ Develop specific interfaces for printing and scanning functionalities.
+ Implement these interfaces in SimplePrinter and MultiFunctionPrinter classes to ensure each class has only the responsibilities it needs.
+ Run client code to verify that instances of SimplePrinter and MultiFunctionPrinter work independently according to their capabilities.

### Interface Segregation Principle (ISP)

The ISP promotes the creation of small, specific interfaces instead of large, general ones. This prevents classes from depending on methods they do not use, resulting in cleaner, more flexible, and maintainable software design.
