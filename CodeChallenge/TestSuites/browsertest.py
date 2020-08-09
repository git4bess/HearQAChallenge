#call the browser

from pathlib import Path

import pytest


@pytest.mark.skip
class TestBrowser:

    def test_browser(self):

        #this is weird
        # base_path = Path(__file__).parent
        # file_path = base_path.parent.resolve()
        # print("file path is :"+file_path.as_posix())

        base_path = Path.cwd()
        parent = base_path.parent
        print("parent folder is "+parent.as_posix())
        #base_path = pathlib.Path('.').parent
        #file_path = base_path.absolute()

        #print("file path is :"+file_path.as_posix())