
# get https://html.spec.whatwg.org/multipage/entities.json
# Usage: python entities.json > entities.rs

# Could easily extend this to look up entity values

import json
import sys

def main(args):
	jsondata = json.loads(file(args[1]).read())
	entities = [entity[1:-1] for entity in jsondata.keys()]
	entities.sort()
	print """// Autogenerated by mk_entities.py

const ENTITIES: [&'static str; %i] = [""" % len(entities)
	for e in entities:
		print "        \"" + e + "\","
	print """    ];

pub fn is_valid_entity(name: &str) -> bool {
	ENTITIES.binary_search(&name).is_ok()
}
"""

main(sys.argv)