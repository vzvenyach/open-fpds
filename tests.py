import pytest
import vcr
import get_fpds


@vcr.use_cassette('fixtures/data/get_fpds.yml', record_mode='once',)
def test_fpds_first():
    r = get_fpds.GetFPDS()
    assert r.next == '10'
    assert len(r.entries) == 10


@vcr.use_cassette('fixtures/data/get_fpds_last.yml', record_mode='once',)
def test_fpds_last():
    r = get_fpds.GetFPDS(start='118760')
    assert r.next is None
