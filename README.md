This is the source code for my freelancing landing page.

Local Setup:
* python -m pip install -r requirements.txt

Generate blog:
* create your context in content/ as a .md file
* then run `pelican -r -l` to preview your changes
* and if it's all good, publish it -> `pelican content -s publishconf.py`
* then commit your changes; `git commit`

