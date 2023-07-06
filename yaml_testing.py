# checking out PyYAML features
# To check installed version of PyYAML:
# pip show PyYAML

import yaml

# Loading a YAML document
a = yaml.safe_load("""
        - One
        - Two
        - Three
        """)
print (a)



# 1. Define custome yaml dump format for our class Dice
# 2. Define a custom loader for our class Dice
class Dice(tuple):
    def __new__(cls, a, b):
        return tuple.__new__(cls, [a, b])
    def __repr__(self):
        return "Dice(%s,%s)" % self


# 1.1) define a representer that converts Dice object to a scalar
def dice_representer(dumper, data):
        return dumper.represent_scalar(u'!dice', u'%sd%s' % data)
# 1.2) register the representer function
yaml.add_representer(Dice, dice_representer)
print (yaml.dump({'gold': Dice(10,6)}))

# 2.1) define a constructor for our custome tag "!dice"
def dice_constructor(loader, node):
     value = loader.construct_scalar(node)
     a, b = map(int, value.split('d'))
     return Dice(a, b)

# 2.2) register consturctor for tag "!dice"
yaml.add_constructor(u'!dice', dice_constructor)

# 2.3) Now load the Dice object
print( yaml.full_load("""
    initial hit points: !dice 8d4
    """))



# Custom constructor for our own class RTP and tag "!rtp"
class RTP:
    def __init__(self, data):
        self.payload = data['payload']
    def __repr__(self):
        return f"RTP(payload:{self.payload})"

def rtp_constructor(loader, node):
    mydict = loader.construct_mapping(node)
    return RTP(mydict)

yaml.add_constructor(u'!rtp', rtp_constructor)
     
a = yaml.full_load("""
        data: !rtp
            payload: abcde
        """)
print (a)
