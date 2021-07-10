# Split asset line in a source file.

## Description:
    In a development stage, build javascript with development mode.
	html line is like:
	'<script src="/assets/js/admin/admin.js?2020062501"></script>'

    In a production stage, js file is splitted.
	html line is like:
	'<script src="/assets/js/admin/285.js?2020062501"></script>'
	'<script src="/assets/js/admin/429.js?2020062501"></script>'
	'<script src="/assets/js/admin/admin.js?2020062501"></script>'

	filenames are (digits) and original file name.

	This program converts a html source file (or html.erb in rails, etc) from development mode to production mode.

### Updated

	The example above is using splitChunks in Webpack 5:

	The first version is corresponding only to AggressiveSplittingPlugin in Webpack 4.
	In this case, html line is like:
	'<script src="/assets/js/admin/0.js?2020062501"></script>'
	'<script src="/assets/js/admin/1.js?2020062501"></script>'
	'<script src="/assets/js/admin/2.js?2020062501"></script>'
	'<script src="/assets/js/admin/3.js?2020062501"></script>'



## Assumption
    Javascript file is already splitted, and splitted files exists in same directory of non-splitted file.

## Usage:
### Usage:
    python3 split_asset_line.py <script file path> <html root path> <url for splitted assets files> <non-splitted file name> <file extension> <includes? origal filename : default True>

### Example:
    python3 split_asset_line.py ./examples/script.html /home/app/public_html /assets/js/admin admin js False

## Test:
    pytest


## Licence:

[MIT]

## Author

[Katsuyoshi Yabe](https://github.com/kay1759)
