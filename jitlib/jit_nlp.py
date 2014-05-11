import nltk

#--------------------------------------------------------------------------------------------------------#
# FUNCTION DEFINITIONS 

def extract_entity_names(t):
    # extracts the named entities from an input NLTK tree
    # Source: https://gist.github.com/322906/90dea659c04570757cccf0ce1e6d26c9d06f9283
    # t = input NLTK tree
    # returns entity_names (a list)
    entity_names = []
    
    if hasattr(t, 'node') and t.node:
        if t.node == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))
                
    return entity_names

def extract_tags(string):
    # extracts tags from an input string
    # string = input string to extract tags from
    # returns tags (a list)
    tokens = nltk.word_tokenize(string)             # extract tokens from string
    pos_tags = nltk.pos_tag(tokens)                 # perform parts-of-speech tagging
    tree = nltk.ne_chunk(pos_tags, binary=True)     # perform NER and generate NLTK tree
    tags = extract_entity_names(tree)               # extract named entities from the NLTK tree
    return tags

#--------------------------------------------------------------------------------------------------------#