![](banner.png)

Data catalogs made easy. The Data Cataloginator is written in Python and built using great open source projects like FastAPI, Lunr.js, Pydantic, Jinja2 and Bootstrap. The projects goal is to keep everything simple, lightweight, modular and as easy to extend as possible. All data aspects are anchored in JSON from the data model to the search index.

![Python](https://img.shields.io/badge/python-3.9.21-blue)

### Features

🔎 **Search** - Lunr.js based search index

💽 **Data** - Pydantic/JSON Schema compatible data model

🤖 **API** - FastAPI based REST API with Swagger UI and GraphQL support paired with GraphiQL

📄 **Website** - Common HTML Jinja2 templating for easy customization

## USGS Software Release Information

(SOFTWARE RELEASE IN PROGRESS)

The official USGS software release can be found at https://doi.org/10.5066/P1336TXZ and cited as follows:

Serna, Brandon and Hsu, Leslie, 2025. Data Cataloginator Version 1.0.0, U.S. Geological Survey software release, https://doi.org/10.5066/P1336TXZ.

A provisional, development version is available at https://github.com/usgs/data-cataloginator. 

The main branch will have the most up-to-date version of the code.  

IP-174120

## Contacts
- Brandon Serna (bserna@usgs.gov), Lead developer
- Leslie Hsu (lhsu@usgs.gov), Contributor and Outreach


## Getting started

__Installation notes__

Pygraphviz is a difficult install

```sh
python3 -m pip install \
                --config-settings="--global-option=build_ext" \
                --config-settings="--global-option=-I$(brew --prefix graphviz)/include/" \
                --config-settings="--global-option=-L$(brew --prefix graphviz)/lib/" \
                pygraphviz
```

```bash

make all

cd app
uvicorn main:app --reload

```

## Hosting

A python server is needed for deployment. It's setup with Uvicorn.

## Demo

![](demo/Header.png)

![](demo/home.png)

![](demo/search.png)

![](demo/landing.png)

![](demo/api.png)

![](demo/graphql.png)

## Requirements

The [requirements.txt](/requirements.txt) file lists required python packages for running the data catalog.

## License

Unless otherwise noted, This project is in the public domain in the United
States because it contains materials that originally came from the United
States Geological Survey, an agency of the United States Department of
Interior. For more information, see the official USGS copyright policy at
https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits

Additionally, we waive copyright and related rights in the work
worldwide through the CC0 1.0 Universal public domain dedication.


### CC0 1.0 Universal Summary
-------------------------

This is a human-readable summary of the
[Legal Code (read the full text)][1].


#### No Copyright

The person who associated a work with this deed has dedicated the work to
the public domain by waiving all of his or her rights to the work worldwide
under copyright law, including all related and neighboring rights, to the
extent allowed by law.

You can copy, modify, distribute and perform the work, even for commercial
purposes, all without asking permission.


#### Other Information

In no way are the patent or trademark rights of any person affected by CC0,
nor are the rights that other persons may have in the work or in how the
work is used, such as publicity or privacy rights.

Unless expressly stated otherwise, the person who associated a work with
this deed makes no warranties about the work, and disclaims liability for
all uses of the work, to the fullest extent permitted by applicable law.
When using or citing the work, you should not imply endorsement by the
author or the affirmer.

## Disclaimer

This software is preliminary or provisional and is subject to revision. It is
being provided to meet the need for timely best science. The software has not
received final approval by the U.S. Geological Survey (USGS). No warranty,
expressed or implied, is made by the USGS or the U.S. Government as to the
functionality of the software and related material nor shall the fact of release
constitute any such warranty. The software is provided on the condition that
neither the USGS nor the U.S. Government shall be held liable for any damages
resulting from the authorized or unauthorized use of the software.



[1]: https://creativecommons.org/publicdomain/zero/1.0/legalcode

