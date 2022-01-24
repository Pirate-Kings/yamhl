from os import path
from pathlib import Path
from typing import Any, Dict, List

import httpx

from .settings import stg
from .utils import ddir, srv_tpl

class Constants:
    pass

YAHML = stg(None, "yamhl.yml")
MD_VARS_YML = ddir(YAHML, "md_vars")
RMVC = ddir(MD_VARS_YML, "commons")

RULES = ddir(YAHML, "rules")

def dd(od: Dict[str, List[str]], *dicts: List[Dict[str, List[str]]]) -> Dict[str, List[str]]:
    for d in dicts:
        for a, v in d.items():
            od[a] = [*(od.get(a, []) or []), *v]
    return od

def rules_fn(rules: Dict[Any, Any], key: str) -> Dict[str, List[str]]:
    _rules = ddir(rules, key)
    return dd({"": ddir(_rules, "del", [])}, ddir(_rules, "repl"))

def op_fn(ip, s: str):
    op = None
    if (_op:= ip.stem) not in ddir(YAHML, f"{s}_op_exc", []):
        op = path.join(YAHML[f'{s}_op'], *ip.parts[1:-1], f"{ddir(YAHML, f'files_conv/{_op}/{s}_op', _op)}.{s}")
    return op

def repl(s: str, repl_dict: Dict[str, List[str]]) -> str:
    op = s
    for k, v in repl_dict.items():
        for i in v:
            op = op.replace(i, k)
    return op

for i in ["md", "html"]:
    setattr(Constants, f"{i}_rules", rules_fn(RULES, i))

def main(rmv: Dict[Any, Any]={}):
    rmv_r = ddir(rmv, "rules")
    rmv_mv = ddir(rmv, "md_vars")
    for i in ["md", "html"]:
        setattr(Constants, f"{i}_repl", dd(rules_fn(RULES, i), rules_fn(rmv_r, i)))
    MVC = dict(RMVC, **ddir(rmv_mv, "commons"))
    for rip in list(Path(f'./{YAHML["input"]}').rglob("*.md")):
        md_out, html_out = [op_fn(rip, i) for i in ["md", "html"]]

        with open(rip, "r") as ip:
            md = repl(ip.read(), Constants.md_repl)
            for k, v in dict(MVC, **ddir(MD_VARS_YML, f"files/{rip.stem}"), **ddir(rmv_mv, f"files/{rip.stem}")).items():
                md = md.replace(f"${{{k}}}", v)

            if md_out:
                with open(md_out, "w") as md_out:
                    md_out.write(md)

            if html_out:
                with open(html_out, "w") as html_out:
                    headers = {"accept": "application/vnd.github.v3+json"}
                    data = {"text": md}
                    md = str(
                        httpx.post("https://api.github.com/markdown", headers=headers, json=data).content,
                        encoding="utf-8"
                    )

                    html_out.write(srv_tpl("html.mako", content=repl(md, Constants.html_repl)))