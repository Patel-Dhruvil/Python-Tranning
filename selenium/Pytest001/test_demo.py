from Pytest001.BaseClass import BaseClass

class TestDemo(BaseClass):
    def test_firstTestDemo(self):
        print("This is first demo")
        assert 1 == 1
        log = self.get_logger()
        log.info("assert success")

    def test_secTestDemo(self):
        log = self.get_logger()
        log.info("assert fail ")
        log.warning("here is warning")

    def test_dataload1(self,dataload):
        print(dataload)
        self.get_logger()
