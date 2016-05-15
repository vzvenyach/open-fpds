from get_fpds import GetFPDS
import xml.etree.ElementTree as ET
import xmltodict
import json

def run(start_date, end_date):
    with open('results/' + start_date.replace('/','-') + '.json', 'w') as fp:
        g = GetFPDS(start_date=start_date, end_date=end_date, start=0)
        ns = {
            'http://www.w3.org/2005/Atom': None,
            'http://www.fpdsng.com/FPDS': None
        }
        results = []

        while g.next is not None:
            for entry in g.entries:
                d = ET.tostring(entry, encoding="unicode")
                results.append(xmltodict.parse(d, process_namespaces=True, namespaces=ns))
            g = GetFPDS(start_date=start_date, end_date=end_date, start=g.next)

        # Last time
        for entry in g.entries:
            d = ET.tostring(entry, encoding="unicode")
            results.append(xmltodict.parse(d, process_namespaces=True, namespaces=ns))

        fp.write(json.dumps(results, indent=2))

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Run FPDS getter')
    parser.add_argument('start_date', help='the start date in the format "YYYY/MM/DD"')
    #parser.add_argument('end_date', help='the end date in the format "YYYY/MM/DD"')
    args = parser.parse_args()
    run(args.start_date, args.start_date)
