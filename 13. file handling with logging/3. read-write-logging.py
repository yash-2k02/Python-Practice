import logging

logging.basicConfig(
    filename='files/file_handler.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
    filemode='a'
)


def read_from_file(filepath):
    try:
        with open(filepath, "r") as file:
            content = file.readlines()
            logging.info(f"Successfully read from {filepath}")
            return [line.strip() for line in content]
    except FileNotFoundError:
        logging.error(f"File not found {filepath}")
        return []
    except Exception as e:
        logging.critical(f"Unexpected error while reading {filepath}: {e}")
        return []


def write_to_file(filepath, data):
    try:
        with open(filepath, "a") as file:
            file.write(data+"\n")
            logging.info(f"Successfully wrote to {filepath}")
    except Exception as e:
        logging.error(f"Failed to write to {filepath} : {e}")



if __name__ == "__main__":
    filepath = 'files/sample.txt'

    write_to_file(filepath, "First log entry.")
    write_to_file(filepath, "Second log entry.")

    lines = read_from_file(filepath)
    for line in lines:
        print(line)

