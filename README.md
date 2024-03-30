
# Advanced Calculator Application

This Advanced Calculator is a versatile command-line application designed for performing arithmetic operations, managing calculation history, and extending functionalities through a dynamic plugin system. Built with scalability and flexibility in mind, it integrates professional logging practices and advanced data handling using Pandas, making it an ideal tool for both casual and professional use.

## Core Functionalities

### Command-Line Interface (REPL)
- **Arithmetic Operations**: Perform addition, subtraction, multiplication, and division with ease.
- **Calculation History Management**: Access and manage your calculation history directly from the command line.
- **Plugin System**: Extend the calculator's capabilities with additional commands or features through plugins.

### Plugin System
- **Dynamic Integration**: Seamlessly integrates new features without needing to alter the core application code.
- **Discoverability**: A dedicated "Menu" command within the REPL interface lists all available commands, including those from dynamically loaded plugins.

### Calculation History Management with Pandas
- Leverages the power of Pandas for sophisticated management of calculation history, including the ability to load, save, clear, and delete history records.

### Professional Logging Practices
- Implements a detailed logging system to record application operations, data manipulations, errors, and informational messages, differentiated by severity levels for efficient monitoring.

### Advanced Data Handling with Pandas
- Utilizes Pandas for efficient and robust data operations, especially for managing calculation history in CSV format.

## Design Patterns for Scalable Architecture

### Facade Pattern
- Abstracts complex Pandas data manipulations behind a simple interface, making the application more accessible and easier to use.

### Command Pattern
- Structures arithmetic and history management commands within the REPL, enabling a modular and extensible command system.

### Factory Method, Singleton, and Strategy Patterns
- These patterns are employed to enhance the application's code structure, flexibility, scalability, and to ensure efficient management of resources and configurations.

## Getting Started

### Prerequisites
- Python 3.8 or newer
- Pandas library

### Installation
1. Clone this repository to your local machine:
   ```sh
   git clone https://github.com/k-0016/midterm_calc
   ```
2. Change to the project directory:
   ```sh
   cd midterm_calc
   ```
3. Install the necessary Python packages:
   ```sh
   pip install -r requirements.txt
   ```

### How to Use
To launch the calculator application, execute:
```sh
python -m app
```
Follow the on-screen prompts to perform arithmetic operations, manage your calculation history, or explore extended functionalities offered by plugins.

## Architectural Overview

The application is designed with best practices in software architecture, employing various design patterns to ensure code modularity, extensibility, and maintainability. Key architectural decisions include the use of the Facade Pattern to simplify interactions with Pandas, the Command Pattern for a clean command structure, and additional patterns like Factory Method and Singleton for overall architectural integrity.

## Contributing

We welcome contributions to the Advanced Calculator project. Please feel free to fork the repository, make your changes, and submit a pull request for review.
