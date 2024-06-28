#!/bin/bash

# Make the script executable
chmod +x copy_folder_gitrepo.py

# Create a symlink to make the script globally accessible
sudo ln -s $(pwd)/copy_folder_gitrepo.py /usr/local/bin/copy_folder_gitrepo

echo "Installation complete. You can now use 'copy_folder_gitrepo <github_folder_url>' from any directory."
echo "Please ensure you have the required libraries installed by running:"
echo "pip install -r requirements.txt"

