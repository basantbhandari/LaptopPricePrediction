# LPPS

Setup Python virtual Environment
--------
- Install venv :
```bash
 sudo apt-get install -y python3-venv
```
- Inside Project script folder
```bash
python3 -m venv venv
```
- activate virtual environment
```bash
source venv/bin/activate
```
Now, virtual environment 'venv' should be activated.
-------
Now install requirements for project (just first time)
```python
pip3 install -r requirements.txt
```
- And to deactivate venv:
```bash
deactivate
```
Note:
--------
Check for sites to be eligible for scrapping or not.
Make a seperate folder for each website to store scripts to scrape that site.

