from bs4 import BeautifulSoup
import requests
import unicodedata

# Python 2.7 please!

def proposals():
    doc = BeautifulSoup(requests.get("http://opensourcebridge.org/events/2012/proposals").text)
    return doc.find_all('tr', 'proposal_row')

def clean(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii','ignore')
    return text.replace('\n', '')

def speaker(proposal_row):
    return clean(proposal_row.find_next_sibling('tr').find('a').text)

def title(proposal_row):
    return clean(proposal_row.find('a', 'title').text)

def track(proposal_row):
    return clean(proposal_row.find('td', 'track', 'a').text)


def naive_graph():
    """
    A first attempt.
    """
    print "graph{"
    for proposal in proposals():
        print '"%s" -- "%s" -- "%s";' % ( speaker(proposal), title(proposal), track(proposal) )
    print "}"


def talk_graph():
    """
    De-emphasize titles while keeping an entity to represent the proposed talk itself.
    """
    talk_number = 0
    print "graph{"
    print """
        Chemistry[shape=rectangle, style=filled, fillcolor=red, fontcolor=white, color=red];
        Hacks[shape=rectangle, style=filled, fillcolor=purple, fontcolor=white, color=purple];
        Culture[shape=rectangle, style=filled, fillcolor=deepskyblue2, fontcolor=white, color=deepskyblue2];
        Cooking[shape=rectangle, style=filled, fillcolor=goldenrod1, fontcolor=white, color=goldenrod1];
        Business[shape=rectangle, style=filled, fillcolor=darkgreen, fontcolor=white, color=darkgreen];
    """

    for proposal in proposals():
        print 'talk_%d[shape=point, label=""];' % talk_number
        print '"%s" -- talk_%d -- "%s";' % ( speaker(proposal), talk_number, track(proposal) )
        talk_number += 1
    print "}"



def total_graph():
    """
    De-emphasize all the things!
    """
    talk_number = 0

    print "graph{"
    print """
        Chemistry[shape=rectangle, style=filled, fillcolor=red, fontcolor=white, color=red];
        Hacks[shape=rectangle, style=filled, fillcolor=purple, fontcolor=white, color=purple];
        Culture[shape=rectangle, style=filled, fillcolor=deepskyblue2, fontcolor=white, color=deepskyblue2];
        Cooking[shape=rectangle, style=filled, fillcolor=goldenrod1, fontcolor=white, color=goldenrod1];
        Business[shape=rectangle, style=filled, fillcolor=darkgreen, fontcolor=white, color=darkgreen];
    """

    talks = proposals()
    speakers = {name:number for (number, name) in enumerate( set([speaker(talk) for talk in talks]) ) }

    for (name, number) in speakers.items():
        print 'speaker_%d[shape=diamond, label=""];' % number

    for talk in talks:
        print 'talk_%d[shape=point, label=""];' % talk_number
        print 'speaker_%d -- talk_%d -- "%s";' % ( speakers[speaker(talk)], talk_number, track(talk) )
        talk_number += 1
    print "}"



if __name__ == "__main__":
    total_graph()