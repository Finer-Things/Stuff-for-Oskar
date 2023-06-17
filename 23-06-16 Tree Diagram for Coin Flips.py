flips = ["Heads", "Tails"]
counter = 0

def make_tree(counter, limit):
    for flip in flips:
        print("\t"*(counter), flip)
        counter += 1
        if counter < limit:
            make_tree(counter, limit)

make_tree(0, 5)
    
