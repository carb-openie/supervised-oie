from oie_readers.oieReader import OieReader
from oie_readers.extraction import Extraction

class RnnOIEReader(OieReader):
    
    def __init__(self):
        self.name = 'RnnOIE'
    
    def read(self, fn):
        d = {}
        with open(fn) as fin:
            for line in fin:
                data = line.strip().split('\t')
                #confidence = data[0]
                #if not all(data[1]):
                #    continue
                text = data[0]
                rel = data[1]
                args = [s[s.index('::') + 2:] for s in data[2:]]
                #args = data[4].strip().split(');')
                ar1 = True
                arg1 = ''
                args = []
                for s in data[2:]:
                    if s[:s.index('::')]=='V':
                         ar1 = False
                         continue
                    if ar1:
                         arg1 = arg1 + ' ' + s[s.index('::') + 2:]
                    else:
                         args.append(s[s.index('::') + 2:])
                    
#                print arg1, rel, args
                curExtraction = Extraction(pred = rel, sent = text, confidence = float(0.1))
                curExtraction.addArg(arg1)
                for arg in args:
                    curExtraction.addArg(arg)
                d[text] = d.get(text, []) + [curExtraction]
        self.oie = d
