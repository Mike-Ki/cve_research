import sys
from git import Repo
import time


def clone_repos_from_file(repos_file):
    with open(repos_file) as f:
        try:
            for l in f:
                repo_url = l.strip()
                repo_name = repo_url.split("//")
                local_path = f'repos/{repo_name[1].strip(".git")}'
                try:
                    Repo.clone_from(repo_url, local_path)
                except:
                    print(
                        f"[ERROR] [{int(time.time())}] failed to clone {repo_url}",
                        file=sys.stderr,
                    )

                print(
                    f"[INFO] [{int(time.time())}] successfully cloned {repo_url} to {local_path}"
                )
                time.sleep(1)
        except KeyboardInterrupt:
            exit()


def main():
    args = sys.argv
    if len(args) < 2:
        print(f"usage: {args[0]} <repository_list>")
        exit()
    
    clone_repos_from_file(args[1])


if __name__ == "__main__":
    main()
