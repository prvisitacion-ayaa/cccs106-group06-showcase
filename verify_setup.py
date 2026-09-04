import os
import sys
import subprocess
from pathlib import Path


def check(condition, message):
    if condition:
        print(f"[PASS] {message}")
        return True
    else:
        print(f"[FAIL] {message}")
        return False


def main():
    results = []

    # 1. Python 3.10+
    python_ok = sys.version_info >= (3, 10)
    results.append(
        check(
            python_ok,
            f"Python 3.10+ ({sys.version.split()[0]})"
        )
    )

    # 2. Virtual environment isolation
    venv = os.environ.get("VIRTUAL_ENV")

    if venv:
        venv_ok = Path(sys.prefix).resolve() == Path(venv).resolve()
    else:
        venv_ok = False

    results.append(
        check(
            venv_ok,
            "Virtual environment isolation"
        )
    )

    # 3. Flet SDK 0.86.5+
    try:
        import flet

        flet_version = getattr(flet, "__version__", "0.0.0")

        def version_tuple(version):
            return tuple(
                int(x) for x in version.split(".")[:3]
                if x.isdigit()
            )

        flet_ok = version_tuple(flet_version) >= (0, 86, 5)

    except Exception:
        flet_version = "not installed"
        flet_ok = False

    results.append(
        check(
            flet_ok,
            f"Flet SDK v0.86.5+ ({flet_version})"
        )
    )

    # 4. Git binary detection
    try:
        result = subprocess.run(
            ["git", "--version"],
            capture_output=True,
            text=True,
            check=True
        )
        git_ok = True
        git_version = result.stdout.strip()
    except Exception:
        git_ok = False
        git_version = "not found"

    results.append(
        check(
            git_ok,
            f"Git binary detection ({git_version})"
        )
    )

    # 5. Institutional Git identity
    try:
        username = subprocess.run(
            ["git", "config", "--get", "user.name"],
            capture_output=True,
            text=True
        ).stdout.strip()

        email = subprocess.run(
            ["git", "config", "--get", "user.email"],
            capture_output=True,
            text=True
        ).stdout.strip()

        identity_ok = bool(username and email)

    except Exception:
        username = "mica"
        email = "@cspc"
        identity_ok = False

    results.append(
        check(
            identity_ok,
            "Configured institutional Git user identity"
        )
    )

    # 6. .gitignore hygiene
    gitignore = Path(".gitignore")

    if gitignore.exists():
        content = gitignore.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        ignored_items = [
            ".venv/",
            "__pycache__/",
            "*.pyc",
            ".env"
        ]

        hygiene_ok = any(
            item in content
            for item in ignored_items
        )
    else:
        hygiene_ok = False

    results.append(
        check(
            hygiene_ok,
            ".gitignore hygiene"
        )
    )

    # Summary
    print()
    print("=" * 50)

    if all(results):
        print("PRE-FLIGHT AUDIT: ALL CHECKS PASSED")
        print("=" * 50)
        return 0
    else:
        print("PRE-FLIGHT AUDIT: ONE OR MORE CHECKS FAILED")
        print("=" * 50)
        return 1


if __name__ == "__main__":
    sys.exit(main())
