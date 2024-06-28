# Quick Repo Folder Copy

## Description

Quick Repo Folder Copy is a one-day project that allows you to quickly copy specific folders from GitHub repositories without creating nested subfolders and `.gitmodules`. It’s an open-source alternative to the Gitzip extension, requiring no access permissions or tokens.

## Features:
- Copy specific folders without cloning the entire repository
- No need for access permissions or tokens
- Easy installation and usage
- Developed in one day for quick tasks

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/quick-repo-folder-copy.git
    cd quick-repo-folder-copy
    ```

2. Run the installation script:

    ```sh
    chmod +x install.sh
    ./install.sh
    ```

    The script will check for Python3, create a virtual environment, install dependencies, and create a symlink for global access to the script.

## Usage

After installation, you can use the `copy_folder_gitrepo` command from any directory:

```sh
copy_folder_gitrepo https://github.com/DataTalksClub/mlops-zoomcamp/tree/main/cohorts/2024/06-best-practices
```

## Help
To display the help message, use:
```sh
copy_folder_gitrepo -h
```
or
```sh
copy_folder_gitrepo -help
```



