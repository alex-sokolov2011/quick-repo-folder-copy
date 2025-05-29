#!/usr/bin/env python3

"""Script for copying a folder from a GitHub repository to the current directory"""

import os
import sys
import json
import shutil
import zipfile
from io import BytesIO

import requests


def get_default_branch(repo_owner, repo_name):
    """
    Fetch the default branch name from the GitHub API.

    Parameters:
    repo_owner (str): The owner of the repository.
    repo_name (str): The name of the repository.

    Returns:
    str: The default branch name (e.g., 'main' or 'master').
    """
    api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"
    response = requests.get(api_url, timeout=5)
    if response.status_code == 200:
        data = response.json()
        return data.get("default_branch", "main")
    else:
        print(f"Error: Unable to fetch repo metadata. Status code: {response.status_code}")
        sys.exit(1)

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
        if "tree" in parts:
            branch = parts[6]
            path_in_repo = "/".join(parts[7:])
        else:
            branch = get_default_branch(repo_owner, repo_name)
            path_in_repo = ""
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
    response = requests.get(url, timeout=5)
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

def rename_extracted_root(repo_name, branch, target_name):
    """
    Rename the extracted root folder (e.g., repo-main) to a desired name.

    Parameters:
    repo_name (str): The name of the repository.
    branch (str): The branch that was downloaded.
    target_name (str): The desired name of the resulting folder.
    """
    extracted_name = f"{repo_name}-{branch}"
    if os.path.exists(target_name):
        print(f"Error: Destination path '{target_name}' already exists.")
        sys.exit(1)
    shutil.move(extracted_name, target_name)


def main():
    """
    The main function of script. Copies specified folder or entire repository from GitHub repo to the current directory.
    """
    if len(sys.argv) != 2 or sys.argv[1] in ("-h", "--help"):
        print_help()
        return

    github_url = sys.argv[1]
    repo_owner, repo_name, branch, path_in_repo = parse_github_url(github_url)
    dest_path = os.path.basename(path_in_repo) if path_in_repo else "."
    download_and_extract(repo_owner, repo_name, branch, path_in_repo, dest_path)
    
    # Optional rename if full repo was downloaded with branch name
    if dest_path == "." :
        rename_extracted_root(repo_name, branch, repo_name)

    print(f"Copied {path_in_repo or 'entire repository'} from {repo_owner}/{repo_name} to {dest_path}")


if __name__ == "__main__":
    main()
