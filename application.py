import os
import openai


#openai.organization = "org-jOS3rcSS5l2406Nw1OF6NZXw"
openai.api_key =  "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"

response = openai.Completion.create(
    engine="davinci", 
    prompt= "This is a test",
    max_token = 31)
response = "worked fine keep working"
print(response)