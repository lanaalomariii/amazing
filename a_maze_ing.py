import sys
from config import read_configuration_file, validate_configurations


def main() -> None:

    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py config.txt")
        sys.exit(1)

    config_file = sys.argv[1]

    try:
        config = read_configuration_file(config_file)
        params = validate_configurations(config)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)

    print(f"Width:   {params['width']}")
    print(f"Height:  {params['height']}")
    print(f"Entry:   {params['entry']}")
    print(f"Exit:    {params['exit']}")
    print(f"Perfect: {params['perfect']}")


if __name__ == "__main__":
    main()
