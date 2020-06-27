# Split asset line in a source file.

## Description:
    In a development stage, build javascript with development mode.
	html line is like:
	'<script src="/assets/js/admin/admin.js?2020062501"></script>'

    In a production stage, js file is splitted.
	html line is like:
	'<script src="/assets/js/admin/0.js?2020062501"></script>'
	'<script src="/assets/js/admin/1.js?2020062501"></script>'
	'<script src="/assets/js/admin/2.js?2020062501"></script>'
	'<script src="/assets/js/admin/3.js?2020062501"></script>'

	This program converts a html source file (or html.erb in rails, etc) from development mode to production mode.

## Assumption
    Javascript file is already splitted, and splitted files exists in same directory of non-splitted file.

## Usage:
### Usage:
    python3 split_asset_line.py <script file path> <html root path> <url for splitted assets files> <non-splitted file name> <file extension>

### Example:
    python3 split_asset_line.py ./examples/script.html /home/app/public_html /assets/js/admin admin js

## Test:
    python3 -m unittest


## Licence:

[MIT]

## Author

[Katsuyoshi Yabe](https://github.com/kay1759)
