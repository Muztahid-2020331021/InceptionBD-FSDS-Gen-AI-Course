# 🐍 Conda Virtual Environment Command Cheatsheet

Managing virtual environments is essential for Python development to ensure your projects have isolated dependencies. This cheatsheet covers the commands for creating, activating, listing, and removing Conda environments.

## 1. Environments Saved in the Default Conda Location

These commands are used when you want Conda to manage your environment files in its standard installation directory (typically inside the `anaconda3/envs` folder).

| Action | Command Syntax | Description |
| :--- | :--- | :--- |
| **Create Environment** | `conda create -n <env_name> python=X.Y -y` | Creates a new environment with a specific name and Python version. |
| **Activate Environment** | `conda activate <env_name>` | Switches your current shell session into the specified environment. |
| **List Environments** | `conda env list` | Shows a list of all existing environments and their file paths. |
| **Remove Environment** | `conda remove --name <env_name> --all` | Completely deletes the specified environment and all its packages. |

### Example Commands (Using `helmet` as the Environment Name)


- **To create the 'helmet' environment using Python 3.9:**

    `conda create -n helmet python=3.9 -y`

- **To activate the 'helmet' environment:**

    `conda activate helmet`

- **To see the list of all environments in your Conda installation:**

    `conda env list`

- **To remove the 'helmet' environment:**

    `conda remove --name helmet --all`


# 2. Environments Saved in a Custom Location (Project Folder)

This method uses the `--prefix` flag to create the environment directly within a specific folder, often your current project directory (`.\helmet`). This makes the environment portable with your project folder.

| Action | Command Syntax | Description |
| :--- | :--- | :--- |
| **Create Environment** | `conda create --prefix <path/to/folder> python=X.Y -y` | Creates the environment structure directly in the specified folder path. |
| **Activate Environment** | `conda activate <path/to/folder>` | Activates the environment by pointing to its exact path, not its name. |

### Example Commands (Using a Relative Path `.\helmet`)


- **To create the environment in a subfolder named 'helmet' within your current directory:**

    `conda create --prefix .\helmet python=3.9 -y`

- **To activate the environment using its path:**
    
    `conda activate .\helmet`


# 3. Other necessary commands

- **To install all libraries in the requirements.txt:**

    `pip install -r requirements.txt`

- **To check which libraries are installed in the environment:**

    `pip list`