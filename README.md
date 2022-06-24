# Curse Of Aros API
**A python wrapper for [Curse Of Aros game leaderboards](https://www.curseofaros.com).**

![PyPI - Downloads](https://img.shields.io/pypi/dw/curseofaros?color=g&label=Downloads&logo=pypi&style=for-the-badge)
![PyPI - Version](https://img.shields.io/pypi/v/curseofaros?style=for-the-badge)
![GitHub Workflow Status (event)](https://img.shields.io/github/workflow/status/Blank-c/Curse-Of-Aros-API/Upload%20Python%20Package?style=for-the-badge)


## Installation
```
pip install curseofaros
```

## Usage
```python
import curseofaros

client = curseofaros.Client()
```


**Player Functions**
```python
await client.melee("name", limit= None)

await client.magic("name", limit= None)

await client.mining("name", limit= None)

await client.smithing("name", limit= None)

await client.woodcutting("name", limit= None)

await client.crafting("name", limit= None)

await client.fishing("name", limit= None)

await client.cooking("name", limit= None)

await client.tailoring("name", limit= None)
```


**Guild Functions**
```python
await client.g_melee("guild prefix", place= 1, limit= None)

await client.g_magic("guild prefix", place= 1, limit= None)

await client.g_mining("guild prefix", place= 1, limit= None)

await client.g_smithing("guild prefix", place= 1, limit= None)

await client.g_woodcutting("guild prefix", place= 1, limit= None)

await client.g_crafting("guild prefix", place= 1, limit= None)

await client.g_fishing("guild prefix", place= 1, limit= None)

await client.g_cooking("guild prefix", place= 1, limit= None)

await client.g_tailoring("guild prefix", place= 1, limit= None)
```

## Information
<details>
<summary><b>Parameters</b></summary><br>
<b>place (Int)</b> - Shows the <i>nth</i> result of the search.<br><b>limit (None or Int)</b> - Limits your search to the given number of pages <i>(first page is 0)</i>.<br>
</details>

<details>
<summary><b>Errors</b></summary><br>
<b>NotFound</b> - Raised when the search fails (when <i>limit</i> is reached or searched term is not found).
</details>
