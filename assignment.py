import os


def read_file(file_path: str) -> str:
    """
    Reads the contents of a file and returns it as a string.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
    raise NotImplementedError()


def write_file(file_path: str, content: str) -> None:
    """
    Writes the given content to a file.
    """
    f = open(file_path,'a')
    f.write(content)
    f.close()
    return None
    raise NotImplementedError()


def list_files_in_directory(directory_path: str) -> list:
    """
    Returns a list of files in the specified directory.
    """
    return [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    raise NotImplementedError()


def generate_numbers(n: int) -> iter:
    """
    Generates a sequence of numbers from 0 to n-1 using an iterator.
    """
    return iter(range(n))
    raise NotImplementedError()


def use_function_from_module(module_name: str, function_name: str, *args) -> any:
    """
    Demonstrates how to import a function from another script (module) and execute it.
    The module name and function name are passed as strings, along with any arguments for the function.
    """
    import importlib
    module = importlib.import_module(module_name)
    func = getattr(module, function_name)
    return func(*args)
    raise NotImplementedError()
