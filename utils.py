import os


def file_handler_decorator(func):
    def wrapper(file_path):
        try:
            with open(file_path, 'r') as file:
                file_content = file.read()
                result = func(file_content)
                return result
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"Error occurred: {str(e)}")
    return wrapper


def load_file(filename, *subdirs):
    resource_folder = 'resources'
    os.makedirs(resource_folder, exist_ok=True)
    for subdir in subdirs:
        resource_folder = os.path.join(resource_folder, subdir)
    return os.path.join(resource_folder, filename)
