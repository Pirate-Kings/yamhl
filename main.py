import base64
from datetime import date

from yamhl import yamhl

icons = ["issues", "forks", "stars", "contributors", "license", "code"]

langs = ["python", "html", "yaml"]

def b64(name: str):
    with open(f"./site/assets/images/icons/{name}", "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

RULES_MDV = {
    "rules": {
        "md": {
            "del": {},
            "repl": {
                **{f'<pre><code id="hljs {i}">': [f"```{i}\n",] for i in langs},
                '</code></pre>': ["```"],
            },
        },
        "html": {
            "del": {},
            "repl": {},
        }
    },
    "md_vars": {
        "commons": {
            "year": str(date.today().year),
            **{f"{i}_b64": b64(f"{i}.png") for i in icons}
        },
        "files": {},
    }
}

def main():
    yamhl.main(RULES_MDV)

if __name__ == "__main__":
    main()