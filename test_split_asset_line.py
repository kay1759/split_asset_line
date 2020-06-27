import unittest
from unittest.mock import Mock, patch, MagicMock
import split_asset_line

class TestStringMethods(unittest.TestCase):

    @patch("split_asset_line.glob")
    def test_sorted_number_split(self, mock_glob):
        """
        test for sorted_number_split
        """
        # <integer>.js
        mock_glob.glob.return_value = ["0.js", "1.js", "2.js"]
        self.assertEqual([0,1,2], split_asset_line.sorted_number_split("/home/app/public_html", "/assets", "js"))

        # not <integer>.js
        mock_glob.glob.return_value = ["app.js", "admin.js", "style.css"]
        self.assertEqual([], split_asset_line.sorted_number_split("/home/app/public_html", "/assets", "js"))
        # ordering test
        mock_glob.glob.return_value = ["2.js", "0.js", "1.js"]
        self.assertNotEqual([2,0,1], split_asset_line.sorted_number_split("/home/app/public_html", "/assets", "js"))

        # ordering test
        mock_glob.glob.return_value = ["2.js", "0.js", "1.js"]
        self.assertEqual([0,1,2], split_asset_line.sorted_number_split("/home/app/public_html", "/assets", "js"))

        # mix
        mock_glob.glob.return_value = ["2.js", "0.js", "1.js", "app.js", "admin.js", "style.css"]
        self.assertEqual([0,1,2], split_asset_line.sorted_number_split("/home/app/public_html", "/assets", "js"))


    def test_convert_line(self):
        """
        unit test for convert_line
        """

        # divide line
        line = "<script src=\"/assets/js/admin/admin.js?1\"></script>"
        assetdir = "/assets/js/admin"
        assetfile = "admin"
        ext = "js"
        assetnumbers = [0,1,2]
        expected = "<script src=\"/assets/js/admin/0.js?1\"></script><script src=\"/assets/js/admin/1.js?1\"></script><script src=\"/assets/js/admin/2.js?1\"></script>"
        self.assertEqual(expected, split_asset_line.convert_line(line, assetdir, assetfile, ext, assetnumbers))

        # not divide line
        line = "<script src=\"/assets/js/admin/app.js?1\"></script>"
        assetdir = "/assets/js/admin"
        assetfile = "admin"
        ext = "js"
        assetnumbers = [0,1,2]
        expected = line
        self.assertEqual(expected, split_asset_line.convert_line(line, assetdir, assetfile, ext, assetnumbers))

        # not divide line
        line = "<script src=\"/assets/js/admin/admin.css?1\"></script>"
        assetdir = "/assets/js/admin"
        assetfile = "admin"
        ext = "js"
        assetnumbers = [0,1,2]
        expected = line
        self.assertEqual(expected, split_asset_line.convert_line(line, assetdir, assetfile, ext, assetnumbers))
