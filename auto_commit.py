import subprocess
import sys
import os
from typing import List


def check_git_repo():
    """
    Checks if the current directory is within a Git repository.

    Exits the script if not in a Git work tree.
    """
    try:
        # Check if `git rev-parse --is-inside-work-tree` returns 0
        subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            check=True,
            capture_output=True,
        )
    except subprocess.CalledProcessError:
        print("Error: The current directory is not a Git repository.", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print(
            "Error: 'git' command not found. Ensure Git is installed and in your PATH.",
            file=sys.stderr,
        )
        sys.exit(1)


def get_staged_files() -> List[str]:
    """
    Retrieves a list of all files currently staged (added to the index).

    Returns:
        List[str]: A list of staged file paths.
    """
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", "--cached"],
            capture_output=True,
            text=True,
            check=True,
        )
        return [f.strip() for f in result.stdout.splitlines() if f.strip()]
    except subprocess.CalledProcessError as e:
        print(
            f"Error: Failed to execute Git command to fetch staged files.\n{e.stderr}",
            file=sys.stderr,
        )
        sys.exit(1)


def generate_message(file_path: str) -> str:
    """
    Generates an intelligent commit message based on the single file's extension and name.

    Uses Conventional Commits style (e.g., feat, fix, docs).

    Args:
        file_path (str): The path to the single staged file.

    Returns:
        str: The generated commit message.
    """
    filename = os.path.basename(file_path)
    extension = os.path.splitext(filename)[1].lower()

    type_map = {
        (".md", ".txt", ".rst"): ("docs", "Update documentation/README"),
        (".py", ".sh", ".go", ".java", ".c", ".cpp", ".js", ".ts"): (
            "feat",
            "Add new algorithms",
        ),
        (".html", ".css", ".scss", ".less"): ("style", "Adjust styles or layout"),
        (".png", ".jpg", ".jpeg", ".svg", ".gif"): (
            "asset",
            "Add or update media resources",
        ),
    }

    prefix = "chore"
    description = "Miscellaneous changes"

    # Match against file type
    for extensions, (p, desc) in type_map.items():
        if extension in extensions:
            prefix, description = p, desc
            break

    # Match against file name content
    if "test" in filename.lower() or "spec" in filename.lower():
        prefix, description = "test", "Add or modify test cases"
    elif filename in [
        "package.json",
        "requirements.txt",
        "pom.xml",
        "Gemfile",
        "Dockerfile",
    ]:
        prefix, description = "build", "Update dependencies or build configuration"

    # Conventional Commit format: type: subject (file_name)
    return f"{prefix}: {description} ({filename})"


def main():
    """
    Main function to orchestrate the staged file check and auto-commit logic.
    """
    check_git_repo()
    staged_files = get_staged_files()

    if not staged_files:
        subprocess.run(["git", "add", "."])

    print("--- Staged Files List ---")
    for f in staged_files:
        print(f)
    print("-------------------------")

    if len(staged_files) == 1:
        # Case 1: Single file, auto-generate and commit
        file_to_commit = staged_files[0]
        commit_message = generate_message(file_to_commit)

        print(f"\nDetected single staged file: {file_to_commit}")
        print(f"Auto-generated Commit Message: '{commit_message}'")

        try:
            
            subprocess.run(["git", "commit", "-m", commit_message], check=True)
            print("\n✅ Auto-commit successful!")
            print(f"Commit Message: {commit_message}")
        except subprocess.CalledProcessError as e:
            print(f"\n❌ Commit failed:\n{e.stderr}", file=sys.stderr)
            sys.exit(1)

    else:
        # Case 2: Multiple files, prompt for manual commit
        print(f"\nDetected {len(staged_files)} staged files.")
        print(
            "The script cannot safely determine an appropriate single commit message."
        )
        print("Please commit manually using 'git commit -m \"Your message\"'.")


if __name__ == "__main__":
    main()
