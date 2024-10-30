import os
import py_compile
from colorama import init, Fore, Style

# Initialize Colorama
init(autoreset=True)

def convert_to_bytecode(file):
    """Convert supported file to bytecode if applicable."""
    bytecode_file = file + 'c'
    try:
        if file.endswith('.py'):
            py_compile.compile(file, cfile=bytecode_file)
            return f"{Fore.GREEN}Compiled {file} to bytecode: {bytecode_file}"
        else:
            return f"{Fore.YELLOW}{file} is not a Python file and will not be compiled."
    except SyntaxError as e:
        return f"{Fore.RED}SyntaxError while processing {file}: {e}"
    except Exception as e:
        return f"{Fore.RED}Error while processing {file}: {e}"

def is_supported_file_format(file):
    """Check if the file has a supported format."""
    supported_formats = ['.py', '.scr', '.txt', '.html', '.js', '.json', '.csv', '.xml']
    return any(file.endswith(ext) for ext in supported_formats)

def file_type_description(file):
    """Return a description of the file type."""
    descriptions = {
        '.py': "Python Script",
        '.scr': "Script File",
        '.txt': "Text File",
        '.html': "HTML File",
        '.js': "JavaScript File",
        '.json': "JSON File",
        '.csv': "Comma-Separated Values File",
        '.xml': "XML File"
    }
    ext = os.path.splitext(file)[1]
    return descriptions.get(ext, "Unknown File Type")

def center_text(text, width=80):
    """Center the given text within a specified width."""
    return text.center(width)

def main():
    # Tool name and feature list emphasizing simplicity
    tool_name = "ByteCompiler"
    feature_list = [
        "✔ Simple tool for converting file formats to bytecode",
        "✔ Supports .py, .scr, .txt, .html, .js, .json, .csv, and .xml files"
    ]
    
    print(center_text(Fore.CYAN + tool_name, 23))
    print(center_text('-' * len(tool_name), 18))
    print(center_text("Features:", 10))
    for feature in feature_list:
        print(center_text(feature, 12))
    print()

    # Input: list of files to convert
    files_input = input(center_text("Enter file names separated by commas: \n(supported formats: .py, .scr, .txt, .html, .js, .json, .csv, .xml): ", 80))
    files = [file.strip() for file in files_input.split(',')]
    
    results = []

    for file in files:
        if os.path.isfile(file):
            if is_supported_file_format(file):
                description = file_type_description(file)
                print(f"\n{Fore.YELLOW}Processing {file} ({description})...")
                result = convert_to_bytecode(file)
                results.append(result)
            else:
                results.append(f"{Fore.RED}Unsupported file format: {file}")
        else:
            results.append(f"{Fore.RED}File not found: {file}")

    print("\nSummary of Results:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
