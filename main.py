import fixieai

BASE_PROMPT = """I am a helpful agent that can answer questions about Recent ServiceNow earnings reports."""
FEW_SHOTS = """
Q: Who is Bill McDermott
A: Bill McDermott is the CEO of ServiceNow Inc.
"""


URLS = [
    "https://explore-fixie.s3.us-west-2.amazonaws.com/servicenow_earnings_transcript_q1_2023.pdf"
]

CORPORA = [fixieai.DocumentCorpus(urls=URLS)]

agent = fixieai.CodeShotAgent(BASE_PROMPT,
                              FEW_SHOTS,
                              CORPORA,
                              conversational=True
                              )


