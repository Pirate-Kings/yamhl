    with open("license.yaml", "r") as f:
        license = yaml.load(f.read(), yaml.FullLoader)
    if (copyright := []) == []:
        c = license["cholder"]
        for u, (r, y) in ((*u.keys(), *r.items()) for u in c for s in u.values() for r in s):
            copyright.append(
                f"by [Github Account [{u}](https://github.com/{u}) Owner, {y}] as part of project [{r}](https://github.com/{u}/{r})"
            )
        if len(copyright) > 1:
            copyright[-2] += f", and {copyright[-1]}"
            del copyright[-1]
        cholder = f"""Copyright for portions of project [{Vars.project_name}](https://github.com/{Vars.organization}/{Vars.project_name}) are held {', '.join(copyright)}.\n
All other copyright for project [{Vars.project_name}](https://github.com/{Vars.organization}/{Vars.project_name}) are held by [Github Account [{Vars.user}](https://github.com/{Vars.user}) Owner, 2021]."""
    else:
        cholder = f"Copyright (c) 2021 Github Account [{Vars.project_name}](https://github.com/{Vars.user}) Owner"