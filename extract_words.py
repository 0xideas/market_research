for token in doc:
    if token.dep_ == "nsubj":
            for child in token.head.children:
                if child.pos_ in ["ADJ", "VERB"]:
                    print([child, child.pos_])


 for token in doc:
     ...:     if token.dep_ == "nsubj":
     ...:         for child in token.head.children:
     ...:             if child.pos_ == "ADJ":
     ...:                 print("Condition 1")
     ...:                 print([child, child.pos_])
     ...:     
     ...:     if token.dep_ == "dobj":
     ...:         for child in token.head.children:
     ...:             if token.head.pos_ == "VERB" and child.dep_ == "nsubj":
     ...:                 print("Condition 2")
     ...:                 print([token.head, token.head.pos_])         
     ...: 
     ...:     if token.dep_ == "amod" and token.pos_ == "ADJ":
     ...:         print("Condition 3")
     ...:         print([token, token.pos_])
     ...:         
     ...:     if token.dep_ == "conj" and token.pos_ == "ADJ":
     ...:         print("Condition 4")
     ...:         print([token, token.pos_])
     ...:         
     ...:     if token.dep_ == "advmod" and token.pos_ == "ADJ":
     ...:         print([token, token.pos_])


for token in doc:
     ...:     if token.dep_ == "nsubj":
     ...:         for child in token.head.children:
     ...:             if child.pos_ == "ADJ":
     ...:                 print("Condition 1")
     ...:                 print([child, child.pos_])
     ...:     
     ...:     if token.dep_ == "dobj":
     ...:         print("Condition 2")
     ...:         print([token.head, token.head.pos_])
     ...: 
     ...:     if token.dep_ == "amod" and token.pos_ == "ADJ":
     ...:         print("Condition 3")
     ...:         print([token, token.pos_])
     ...:         
     ...:     if token.dep_ == "conj" and token.pos_ == "ADJ":
     ...:         print("Condition 4")
     ...:         print([token, token.pos_])
     ...:         
     ...:     if token.dep_ == "advmod" and token.pos_ == "ADV" and token.head.pos_ =
     ...: = "ADJ":
     ...:         print("Condition 5")
     ...:         print([token, token.pos_])
     ...:     if token.dep_ == "acomp":
     ...:         print("Condition 6")
     ...:         print([token, token.pos_])


def extract_words(doc_object):
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

        if token.dep_ == "advmod" and token.pos_ == "ADV" and token.head.pos_ == "ADJ":
            keywords += [token]

    return(keywords)