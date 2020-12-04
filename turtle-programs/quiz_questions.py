def two_fractions(bot, top):
    # Returns a tuple of two tuples, where the first integer of each is the numerator and the second is the denominator
    import random
    return (random.randint(bot, top), random.randint(bot, top)), (random.randint(bot, top), random.randint(bot, top))

def dimensions_rect(bot, top):
    import random
    return (random.randint(bot, top), random.randint(bot, top))

def dimensions_triangle(bot, top):
    import random
    return (random.randint(bot, top), random.randint(bot, top), random.randint(bot, top))