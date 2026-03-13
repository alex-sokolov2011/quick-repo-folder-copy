# Quick Repo Folder Copy

## Description

Quick Repo Folder Copy lets you quickly copy specific folders from GitHub repositories without cloning the entire repo, creating nested subfolders, or dealing with `.gitmodules`. It's an open-source alternative to the Gitzip extension and requires no access tokens or special permissions.

## Features

- Copy specific folders without cloning the entire repository
- Download the entire repository if no folder is specified
- No access tokens or permissions required
- Works on Linux and Windows (Git Bash)

## Installation

### Linux

1. Clone the repository:

    ```sh
    git clone https://github.com/alex-sokolov2011/quick-repo-folder-copy.git
    cd quick-repo-folder-copy
    ```

2. Run the installation script:

    ```sh
    chmod +x install.sh
    ./install.sh
    ```

    The script makes the Python script executable and creates a symlink at `/usr/local/bin/copy_folder_gitrepo` for global access.

3. Install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

### Windows (Git Bash)

1. Clone the repository in Git Bash:

    ```sh
    git clone https://github.com/alex-sokolov2011/quick-repo-folder-copy.git
    cd quick-repo-folder-copy
    ```

2. Run the installation script:

    ```sh
    bash install.sh
    ```

    The script creates `~/bin/copy_folder_gitrepo` and adds `~/bin` to PATH in `~/.bashrc`.

3. Reload the shell config:

    ```sh
    source ~/.bashrc
    ```

4. Install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

After installation, use the command from any directory:

```sh
copy_folder_gitrepo https://github.com/DataTalksClub/mlops-zoomcamp/tree/main/cohorts/2024/06-best-practices
copy_folder_gitrepo https://github.com/DataTalksClub/mlops-zoomcamp
```

The script downloads a ZIP archive from GitHub and extracts only the requested folder or the entire repository.

## Advantages

- **Time-saving**: Downloads only the required content instead of cloning the entire repository.
- **Space-saving**: No need to store the whole repository locally.
- **Easy to use**: No tokens or permissions required.
- **Privacy**: No third-party extensions monitoring your GitHub or local folders.

## Help

```sh
copy_folder_gitrepo -h
```

or

```sh
copy_folder_gitrepo --help
```

## Motivation

This project was inspired by participation in the MLOps Zoomcamp, where participants needed to copy specific homework folders from course repositories. Many ran into issues with Git submodules and nested folders. This tool simplifies that process.

## Feedback and Support

If you have questions or suggestions, open an issue on this repository.

## License

This project is licensed under the MIT License.
