import fixieai

BASE_PROMPT = """I am a helpful agent that can answer questions about Recent NiteRider Bicycle Lights."""
FEW_SHOTS = """
Q: How do I remove the light from the mount?  
A: press the release tab down and slide the head light forward. 
"""


URLS = [
    "https://cdn.shopify.com/s/files/1/0315/2222/6235/files/NR_LuminaMaxSeries_UserGuide_eFile_bb775e81-bbc0-420c-a86d-b2a49e27f08f.pdf?v=1670971476",
    "https://www.niterider.com/pages/user-guides",
    "https://www.niterider.com/products/6797-lumina-max-2500",
    "https://www.niterider.com/pages/faqs"
]

# https://www.niterider.com/pages/faqs -- no pdf, just web page
# https://www.niterider.com/products/6797-lumina-max-2500 -- no pdf, just web product page
# https://cdn.shopify.com/s/files/1/0315/2222/6235/files/NR_LuminaMaxSeries_UserGuide_eFile.pdf?v=1653683765 -- PDF
# https://www.manualslib.com/manual/2218296/Niterider-Lumina-Max-2500.html#manual -- html manual, not good
# https://www.hupleong.co/shop-niterider/niterider-lumina-max-2500-with-nitelink -- product page, not good
# https://road.cc/content/review/niterider-lumina-max-2500-300133 -- product reviews, not great for indexing
# https://www.youtube.com/watch?v=e6aBaOkgCbE -- Video
# https://www.youtube.com/watch?v=jSFkUBhbzK0 -- Video


CORPORA = [fixieai.DocumentCorpus(urls=URLS)]

agent = fixieai.CodeShotAgent(BASE_PROMPT,
                              FEW_SHOTS,
                              CORPORA,
                              conversational=True
                              )


