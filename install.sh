#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

case "$(uname -s)" in
    MINGW*|MSYS*|CYGWIN*)
        printf '#!/bin/bash\npython "%s/copy_folder_gitrepo.py" "$@"\n' "$SCRIPT_DIR" \
            > /usr/local/bin/copy_folder_gitrepo
        chmod +x /usr/local/bin/copy_folder_gitrepo
        echo "Installed for Git Bash (Windows)."
        ;;
    *)
        chmod +x "$SCRIPT_DIR/copy_folder_gitrepo.py"
        sudo ln -sf "$SCRIPT_DIR/copy_folder_gitrepo.py" /usr/local/bin/copy_folder_gitrepo
        echo "Installed for Linux."
        ;;
esac

echo "Installation complete. You can now use 'copy_folder_gitrepo <github_url>' from any directory."
echo "Install dependencies: pip install -r requirements.txt"

