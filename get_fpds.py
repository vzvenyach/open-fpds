import requests
import xml.etree.ElementTree as ET


class GetFPDS:
    def __init__(self, start_date="2016/05/09", end_date="2016/05/13", start=0):

        def next(elem):
            return None if elem is None else elem.attrib["href"]

        base_url = "https://www.fpds.gov/dbsight/FEEDS/ATOM?FEEDNAME=PUBLIC&q=LAST_MOD_DATE:"
        date_string = "[" + start_date + ", " + end_date + "]"
        ns = {
            'feed': 'http://www.w3.org/2005/Atom',
            'fpds': 'http://www.fpdsng.com/FPDS'
        }
        data = self.parse(self.get(base_url + date_string + "&start=" + str(start)).text)
        self.next = next(data.find('./feed:link[@rel="next"]', ns))
        self.entries = data.findall('.//feed:entry', ns)

    def get(self, url):
        r = requests.get(url)
        return r

    def parse(self, fpds_str):
        root = ET.fromstring(fpds_str)
        return root
