import pytest
import vcr
import get_fpds


@vcr.use_cassette('fixtures/data/get_fpds.yml', record_mode='once',)
def test_fpds_first():
    r = get_fpds.GetFPDS()
    assert r.next == "https://www.fpds.gov/ezsearch/FEEDS/ATOM?s=FPDS&FEEDNAME=PUBLIC&VERSION=1.4&q=LAST_MOD_DATE%3A%5B2016%2F05%2F09%2C+2016%2F05%2F13%5D&start=10"
    assert len(r.entries) == 10

@vcr.use_cassette('fixtures/data/get_fpds_last.yml', record_mode='once',)
def test_fpds_last():
    r = get_fpds.GetFPDS(start=118760)
    assert r.next == None
