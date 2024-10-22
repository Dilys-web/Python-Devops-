# Command Line Arguments

Command line arguments are additional pieces of information that you can provide to a program when you run it from the command line. They allow you to customize the program's behavior without modifying its source code. These arguments are typically specified after the program's name, separated by spaces.

## Accessing Command Line Arguments

To read command line arguments in Python, you need to import the `sys` module. The command line arguments can be accessed using the `sys.argv` list.

### Example

```python
import sys

# Access command line arguments
print("Program name:", sys.argv[0])
print("Arguments:", sys.argv[1:])

```
### Running the Application from the Command Line
1. Open your command line interface (Terminal on macOS/Linux or Command Prompt/PowerShell on Windows).
2. Navigate to the directory where your Python script is located using the cd command. For example:
```
cd path/to/your/script

```

3. Run the script with command line arguments by typing python (or python3, depending on your installation) followed by the script name and any arguments you want to pass. For example:

```
python your_script.py arg1 arg2 arg3

```

### Important Notes
sys.argv is a list of strings, where:

- The first element (sys.argv[0]) is always the name of the program itself.
- Subsequent elements (sys.argv[1], sys.argv[2], etc.) are the arguments passed to the program.