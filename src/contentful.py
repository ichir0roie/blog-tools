# https://github.com/contentful/contentful.py

import contentful
from src import constants

client = contentful.Client(
    constants.CONTENTFUL_SPACE_ID,  # This is the space ID. A space is like a project folder in Contentful terms
    constants.CONTENTFUL_ACCESS_TOKEN  # This is the access token for this space. Normally you get both ID and the token in the Contentful web app
)
