import os

# root of the project
ROOT = os.path.dirname(os.path.abspath(__file__))
print ROOT

DIRPATHS = dict(
    DATA=os.path.join(ROOT, 'data')
)
