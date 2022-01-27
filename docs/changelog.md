<h1 align="center" style="font-weight: bold">
    CHANGELOG
</h1>

## **MangDL v.3.1.0.0**

### **ADDED**

- <a target="_blank" href="https://lhtranslation.net/">Lhtranslation</a> provider
- <a target="_blank" href="https://readmanhua.net/">Read Manhua</a> provider
- <a target="_blank" href="https://readlight.org/">UltraLight</a> provider
- Added `setsu` function in the `mangdl/api/providers/templates/wordpress.py`'s `manga_id_fn` templates and make it a default for the providers to use.

### **CHANGED**

- Changed `mangdl/api/providers/templates/wordpress.py`'s `template` class to make `%B %d, %Y` as default for `date_format`.
- Changed `mangdl/api/providers/templates/wordpress.py`'s `template.manga` function to check if a provider script declares a `date_format`, if which it did will pass the `ms` or master soup to it and use the returned value as the title of the manga.
- Changed `mangdl/api/providers/templates/wordpress.py`'s `template.manga` function to check if a provider script declares a `title_fn`, if which it did will be used as the date format for the all the manga metadata dates.
- Removed `manga_id_fn` function in `mangdl/api/providers/chibimanga.py` and `mangdl/api/providers/setsuscans.py` to use the default `manga_id_fn.setsu` template function.

### **FIXED**