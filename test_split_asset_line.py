import pytest
from mock import patch
import split_asset_line

def test_sorted_number_split():
    """
    test for sorted_number_split
    """

    with patch('split_asset_line.glob') as mock_glob:
        # <integer>.js
        mock_glob.glob.return_value = ["0.js", "1.js", "2.js"]
        assert split_asset_line.sorted_number_split("/home/app/public_html", "/assets", "js") == [0,1,2]

        # not <integer>.js
        mock_glob.glob.return_value = ["app.js", "admin.js", "style.css"]
        assert split_asset_line.sorted_number_split("/home/app/public_html", "/assets", "js") == []

        # ordering test
        mock_glob.glob.return_value = ["2.js", "0.js", "1.js"]
        assert split_asset_line.sorted_number_split("/home/app/public_html", "/assets", "js") != [2,0,1]

        # ordering test
        mock_glob.glob.return_value = ["2.js", "0.js", "1.js"]
        assert split_asset_line.sorted_number_split("/home/app/public_html", "/assets", "js") == [0,1,2]

        # mix
        mock_glob.glob.return_value = ["2.js", "0.js", "1.js", "app.js", "admin.js", "style.css"]
        assert split_asset_line.sorted_number_split("/home/app/public_html", "/assets", "js") == [0,1,2]



def test_convert_line():
    """
    unit test for convert_line
    """

    # divide line
    line = "<script src=\"/assets/js/admin/admin.js?1\"></script>"
    assetdir = "/assets/js/admin"
    assetfile = "admin"
    ext = "js"
    assetnumbers = [285, 429]
    include_orgname = True
    expected = "<script src=\"/assets/js/admin/285.js?1\"></script><script src=\"/assets/js/admin/429.js?1\"></script><script src=\"/assets/js/admin/admin.js?1\"></script>"
    assert split_asset_line.convert_line(line, assetdir, assetfile, ext, assetnumbers, include_orgname) == expected

    # divide line
    line = "<script src=\"/assets/js/admin/admin.js?1\"></script>"
    assetdir = "/assets/js/admin"
    assetfile = "admin"
    ext = "js"
    assetnumbers = [0,1,2]
    include_orgname = False
    expected = "<script src=\"/assets/js/admin/0.js?1\"></script><script src=\"/assets/js/admin/1.js?1\"></script><script src=\"/assets/js/admin/2.js?1\"></script>"
    assert split_asset_line.convert_line(line, assetdir, assetfile, ext, assetnumbers, include_orgname) == expected

    # not divide line
    line = "<script src=\"/assets/js/admin/app.js?1\"></script>"
    assetdir = "/assets/js/admin"
    assetfile = "admin"
    ext = "js"
    include_orgname = False
    assetnumbers = [0,1,2]
    expected = line
    assert split_asset_line.convert_line(line, assetdir, assetfile, ext, assetnumbers, include_orgname) == expected

    # not divide line
    line = "<script src=\"/assets/js/admin/admin.css?1\"></script>"
    assetdir = "/assets/js/admin"
    assetfile = "admin"
    ext = "js"
    include_orgname = False
    assetnumbers = [0,1,2]
    expected = line
    assert split_asset_line.convert_line(line, assetdir, assetfile, ext, assetnumbers, include_orgname) == expected
