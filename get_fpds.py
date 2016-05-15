import requests
import xml.etree.ElementTree as ET
from urllib.parse import parse_qs


class GetFPDS:
    def __init__(self, start_date="2016/05/09", end_date="2016/05/13", agency=None, start=0):

        def next(elem):
            return None if elem is None else parse_qs(elem.attrib["href"])["start"][0]

        base_url = "https://www.fpds.gov/dbsight/FEEDS/ATOM?FEEDNAME=PUBLIC&templateName=1.4.4&q=LAST_MOD_DATE:"
        date_string = "[" + start_date + ", " + end_date + "]"

        url = base_url + date_string
        if agency:
            url = url + " DEPARTMENT_NAME:" + agency
        url += "&start=" + str(start)
        ns = {
            'feed': 'http://www.w3.org/2005/Atom',
            'fpds': 'http://www.fpdsng.com/FPDS'
        }
        data = self.parse(self.get(url).text)
        self.next = next(data.find('./feed:link[@rel="next"]', ns))
        self.last = parse_qs(data.find('./feed:link[@rel="last"]', ns).attrib["href"])["start"][0]
        self.entries = data.findall('.//feed:entry', ns)

    def get(self, url):
        r = requests.get(url)
        return r

    def parse(self, fpds_str):
        root = ET.fromstring(fpds_str)
        return root
