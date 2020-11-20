#!/Users/jeff/.pyenv/shims/python

# NOTE: Could not complete this exercise on my own. Just didn't have enough
#       knowledge and experience with classes at the time,  Had to get some
#       help from other people's solution to complete it.

class ImmutableParent():
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            super().__setattr__(key, value)

    def __setattr__(self, key, value):
        raise ImmutableMeansImmutableError(f'Can\'t set {key}')

class ImmutableMe(ImmutableParent):
    pass

class ImmutableMeansImmutableError(Exception):
    pass
