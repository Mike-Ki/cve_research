# Open-Source Research

This file is meant to introduce the user to the scripts developed for an open-source security research effort. This research was conducted during the [Hacker Contest](https://www.usd.de/tag/hacker-contest/) course.

## Installation

To install the needed dependencies, it is recommended to use a virtual environment. After setting this up, the requirements can be installed through the following command.

```bash
pip install -r requirements.txt
```

## Usage

Fistly, add your access token to the *secrets/github_api_token.txt* file to use the GitHub API.
Now run *scripts/github_scraper.py*, which will generate a JSON dump of all GitHub repositories written in Java.

```bash
python scripts/github_scraper.py > datasets/dump_java_50-100.json
```

For easier processing, generate a database from the newly acquired dump.

```bash
python scripts/json_to_sqlite.py datasets/dump_java_50-100.json datasets/research.sqlite
```

After determining which repositories shall be investigated, use *scripts/clone_repositories.py* to clone the selected repositories. For more information on how to search through the dataset, please refer to [this](#interacting-with-the-dataset) subsection.
```bash
python scripts/clone_repositories.py output/filtered_projects.csv
```

You will find the cloned repositories in *repos/*.

## Interacting with the Dataset

To interact with the dataset, *sqlite3* will be used. You can filter the `repo_metadata` table using the following command.
This statement will return every repository that is not part of the *"android"* topic.

```sql
SELECT * FROM repo_metadata  WHERE id NOT IN (SELECT id FROM repo_full WHERE topic_name LIKE "android");
```

### Examples

If you are looking through the dataset and found an intersting research candidate e.g. through the *README.md* of the project, check out the tech stack through the following command. Note that this does not guarantee a full overview of the used technologies.

```sql
SELECT topic_name FROM repo_full WHERE name LIKE '%project%';
```

You can also search for specific tech using the command below.
```sql
SELECT clone_url FROM repo_full WHERE topic_name LIKE '%docker%';
```
