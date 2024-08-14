import sqlite3
import json
import sys
from datetime import datetime

def init_database(json_file, database_file):

    con = sqlite3.connect(database_file)
    cur = con.cursor()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS repo_metadata (id text, language text, name text, full_name text, private text, html_url text, clone_url text, size int, created_at text, updated_at text, archived bool, disabled bool, visited_at timestamp);"
    )
    cur.execute(
        "CREATE TABLE IF NOT EXISTS repo_topic (id text, name text);"
    )

    cur.execute(
        "CREATE VIEW repo_full AS SELECT repo_metadata.id, language, repo_metadata.name, full_name, private, html_url, clone_url, size, created_at, updated_at, archived, disabled, visited_at, repo_topic.name AS topic_name FROM repo_metadata INNER JOIN repo_topic ON repo_metadata.id=repo_topic.id;"
    )

    with open(json_file, "r") as dump:
        data = json.load(dump)

    for item in data:
        cur.execute(
            "INSERT INTO repo_metadata (id, language, name, full_name, private, html_url, clone_url, size, created_at, updated_at, archived, disabled, visited_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
            (item["id"], item["language"], item["name"], item["full_name"], item["private"], item["html_url"], item["clone_url"], item["size"], item["created_at"], item["updated_at"], item["archived"], item["disabled"], datetime.now()),
        )

        topics = item["topics"]

        for topic in topics:
            cur.execute(
                "INSERT INTO repo_topic (id, name) VALUES (?, ?);", (item["id"], topic)
            )

    con.commit()
    con.close()

def main():
    args = sys.argv
    if len(args) < 3:
        print(f"usage: {args[0]} <json> <database>")
        exit()
    
    init_database(json_file=args[1], database_file=args[2])

if __name__ == '__main__':
    main()
