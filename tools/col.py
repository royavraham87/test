# tools/col.py

def myzip(it1, it2):

    # Create iterators for the input iterables
    iter1 = iter(it1)
    iter2 = iter(it2)

    # Continue generating tuples until the shortest iterable is exhausted
    while True:
        try:
            # Get the next elements from the input iterables
            element1 = next(iter1)
            element2 = next(iter2)

            # Yield a tuple containing elements from both iterables
            yield (element1, element2)

        except StopIteration:
            # If one of the iterables is exhausted, stop the iteration
            break
