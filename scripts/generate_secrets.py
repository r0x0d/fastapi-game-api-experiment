import os
import random
import string

from cryptography.fernet import Fernet
from rich.console import Console

PATH_TO_ENV_FILE: str = ".env"
console = Console()


def parse_env_file() -> list[str]:
    """Parse the .env file and replace the secrets."""
    env_list = []
    with open(PATH_TO_ENV_FILE) as handler:
        lines = [line.strip() for line in handler.readlines()]
        for line in lines:
            # This is used for both the Fernet key and the jwt key
            if line in (
                "CARNAGE_SESSION_SECRET_KEY=",
                "CARNAGE_CHAT_SECRET_KEY=",
            ):
                env_var_with_value = line.split("=")
                if not env_var_with_value[1]:
                    console.log(
                        f"Generating new secret for {env_var_with_value[0]}",
                    )
                    key = Fernet.generate_key()
                    line = f"{env_var_with_value[0]}={key.decode()}"

            if line == "JWT_SECRET_KEY=":
                env_var_with_value = line.split("=")
                if not env_var_with_value[1]:
                    console.log(
                        f"Generating new secret for {env_var_with_value[0]}",
                    )
                    random_key = "".join(
                        random.choice(string.ascii_letters) for _ in range(32)
                    )
                    line = f"{env_var_with_value[0]}={str(random_key)}"

            env_list.append(line)

    return env_list


def write_env_file(env_list: list[str]) -> None:
    """Write the environments back to the file.

    :param env_list: List of environment variables to be written.
    """
    with open(PATH_TO_ENV_FILE, mode="w") as handler:
        for line in env_list:
            line += "\n"
            handler.write(line)


def main() -> int:
    """Main entrypoint for generating secrets script."""
    if os.path.exists(PATH_TO_ENV_FILE):
        env_list = parse_env_file()
        write_env_file(env_list)
        return 0

    console.log(f"'{PATH_TO_ENV_FILE}' not found.")
    return 1


if __name__ == "__main__":
    main()
