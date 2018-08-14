def extract_words(text, spacy_object, stop_words):
    keywords = []
    doc_object = spacy_object(text)
    for token in doc_object:
        if token.pos_ == "ADJ":
            if token.dep_ in ["amod", "conj"]:
                keywords += [token]

        if token.dep_ == "nsubj":
            for child in token.head.children:
                if child.pos_ == "ADJ":
                    keywords += [child]

        if token.dep_ in ["dobj", "acomp"]:
            keywords += [token]
            
        if token.dep_ == "conj" and token.head.pos_ == "VERB":
            keywords += [token]

        if token.dep_ == "advmod" and token.pos_ == "ADV" and token.head.pos_ == "ADJ":
            keywords += [token]
        
        if len([c for c in token.children]) > 3 and token.text not in stop_words:
            keywords += [token]
            
    if len(keywords) == 0:
        keywords = list(doc_object)

    if len(doc_object) == 0 :
        keywords = list(spacy_object("and"))
        
    return(list(set(keywords)))