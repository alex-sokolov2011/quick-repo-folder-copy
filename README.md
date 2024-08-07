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
    git clone git clone https://github.com/alex-sokolov2011/quick-repo-folder-copy.git
    cd quick-repo-folder-copy
    ```

2. Run the installation script:

    ```sh
    chmod +x install.sh
    ./install.sh
    ```

    The script will make the Python script executable and create a symlink for global access to the script. Ensure you have the required libraries in requirements.txt installed (e.g., using pip install -r requirements.txt, conda conda install --file requirements.txt, or pipenv install -r requirements.txt).

## Usage

After installation, you can use the `copy_folder_gitrepo` command from any directory:

```sh
copy_folder_gitrepo https://github.com/DataTalksClub/mlops-zoomcamp/tree/main/cohorts/2024/06-best-practices
copy_folder_gitrepo https://github.com/DataTalksClub/mlops-zoomcamp
```

The script uses archiving to reduce download time and save space, extracting only the necessary folders or the entire repository.

### Advantages

- **Time-saving**: Downloads only the required folders from the archive, instead of cloning the entire repository.
- **Space-saving**: No need to store the whole repository, beneficial for large projects.
- **Ease of use**: No access permissions or tokens required, easy to install and use.
- **Privacy:** No third-party extensions or applications will monitor the state of your GitHub and local folders.


## Help
To display the help message, use:
```sh
copy_folder_gitrepo -h
```
or
```sh
copy_folder_gitrepo -help
```

## Motivation

This project was inspired by my participation in the MLOps Zoomcamp, where participants needed to copy nested folders from homework repositories into their own repositories. Many participants faced issues due to insufficient experience with Git. This tool simplifies that process, allowing users to copy specific folders from GitHub repositories without dealing with nested subfolders or `.gitmodules`.

## Feedback and Support

If you have any questions or suggestions, feel free to open an issue on this repository.

## License

This project is licensed under the MIT License.