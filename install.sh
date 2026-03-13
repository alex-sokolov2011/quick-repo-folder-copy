#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

case "$(uname -s)" in
    MINGW*|MSYS*|CYGWIN*)
        mkdir -p "$HOME/bin"
        printf '#!/bin/bash\npython "%s/copy_folder_gitrepo.py" "$@"\n' "$SCRIPT_DIR" \
            > "$HOME/bin/copy_folder_gitrepo"
        chmod +x "$HOME/bin/copy_folder_gitrepo"
        if ! grep -q 'HOME/bin' "$HOME/.bashrc" 2>/dev/null; then
            echo 'export PATH="$HOME/bin:$PATH"' >> "$HOME/.bashrc"
            echo "Added ~/bin to PATH in ~/.bashrc. Run: source ~/.bashrc"
        fi
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

