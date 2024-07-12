#!/usr/bin/env python

"""Script for copying a folder from a GitHub repository to the current directory"""

import os
import sys
import zipfile
from io import BytesIO

import requests


def parse_github_url(url):
    """
    Parse the GitHub URL to extract repository owner, name repo, branch, and path within the repo.

    Parameters:
    url (str): The GitHub URL of the folder.

    Returns:
    tuple: A tuple containing the repository owner, name repo, branch, and path within the repo.
    """
    try:
        parts = url.split("/")
        repo_owner = parts[3]
        repo_name = parts[4]
        branch = parts[6] if "tree" in parts else "main"
        path_in_repo = "/".join(parts[7:]) if "tree" in parts else ""
    except IndexError:
        print("Error: Invalid GitHub URL format. Please ensure the URL is correct.")
        sys.exit(1)

    return repo_owner, repo_name, branch, path_in_repo


def download_and_extract(repo_owner, repo_name, branch, path_in_repo, dest_path):
    """
    Download and extract the specified folder from the GitHub repository.

    Parameters:
    repo_owner (str): The owner of the GitHub repository.
    repo_name (str): The name of the GitHub repository.
    branch (str): The branch to download.
    path_in_repo (str): The path of the folder within the repository to download.
    dest_path (str): The destination path to extract the folder to.
    """
    url = f"https://github.com/{repo_owner}/{repo_name}/archive/refs/heads/{branch}.zip"
    response = requests.get(url, timeout=2)
    if response.status_code == 200:
        with zipfile.ZipFile(BytesIO(response.content)) as z:
            if path_in_repo:
                for file_info in z.infolist():
                    if file_info.filename.startswith(f"{repo_name}-{branch}/{path_in_repo}"):
                        file_info.filename = file_info.filename[len(f"{repo_name}-{branch}/{path_in_repo}") :]
                        if file_info.filename:
                            z.extract(file_info, dest_path)
            else:
                z.extractall(dest_path)
    else:
        print(f"Error: Unable to download repository archive. Status code: {response.status_code}")
        sys.exit(1)


def print_help():
    """
    Print the help message for using the script.
    """
    help_message = """
    Usage: copy_folder_gitrepo <github_url>

    This script copies a specified folder from a GitHub repository to the current directory.
    If no folder is specified, the entire repository will be copied.

    Arguments:
    <github_url>  The URL of the folder or repository in the GitHub repository.

    Example:
    copy_folder_gitrepo https://github.com/DataTalksClub/mlops-zoomcamp/tree/main/cohorts/2024/06-best-practices
    copy_folder_gitrepo https://github.com/DataTalksClub/mlops-zoomcamp
    """
    print(help_message)


def main():
    """
    The main function of script. Copies specified folder or entire repository from GitHub repo to the current directory.
    """
    if len(sys.argv) != 2 or sys.argv[1] in ("-h", "--help"):
        print_help()
        return

    github_url = sys.argv[1]
    repo_owner, repo_name, branch, path_in_repo = parse_github_url(github_url)
    dest_path = os.path.basename(path_in_repo) if path_in_repo else f"{repo_name}-{branch}"
    download_and_extract(repo_owner, repo_name, branch, path_in_repo, dest_path)
    print(f"Copied {path_in_repo or 'entire repository'} from {repo_owner}/{repo_name} to {dest_path}")


if __name__ == "__main__":
    main()
