from typing import Any, Dict

from mako.lookup import TemplateLookup

from .settings import stg


LOOKUPS_DICT = {"templates": ["templates", "yamhl.yml"], "pdoc": ["pdoc/templates", "yamhl.yml"]}

class Lookups:
    pass

for k, v in LOOKUPS_DICT.items():
    setattr(Lookups, k, TemplateLookup(directories=stg(*v) or []))

def ddir(d: Dict[Any, Any], dir: str, de: Any={}) -> Any:
    """
    Retrieve dictionary value using recursive indexing with a string.
    ex.:
        `ddir({"data": {"attr": {"ch": 1}}}, "data/attr/ch")`
        will return `1`


    Args:
        dict (dict): Dictionary to retrieve the value from.
        dir (str): Directory of the value to be retrieved.

    Returns:
        op (Any): Retrieved value.
    """
    op = d
    for a in dir.split("/"):
        op = op.get(a)
        if not op:
            break
    return op or de

def srv_tpl(tn: str, ln: str="templates", **kwargs: Dict[str, Any]):
    return getattr(Lookups, ln).get_template(tn).render(**kwargs)