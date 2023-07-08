import vertexai
from vertexai.language_models import TextGenerationModel
from google.cloud import aiplatform

aiplatform.init(
    # your Google Cloud Project ID or number
    # environment default used is not set
    project='ghc-012',

    # the Vertex AI region you will use
    # defaults to us-central1
    location='us-central1',

    # Google Cloud Storage bucket in same region as location
    # used to stage artifacts
    staging_bucket='gs://my_staging_bucket',

    # custom google.auth.credentials.Credentials
    # environment default creds used if not set
    credentials="fa1d7ddd22c269f6795dd7a1e6a5235963c7b4a4",

    # customer managed encryption key resource name
    # will be applied to all Vertex AI resources if set
    encryption_spec_key_name="-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCxlYh+lRnCa7my\nLphg8bppxnxVbkW8YCDUBJEM43Ik0lmjFT9SsXPKtSFx7czQRqjJ43kWGoj//Gdv\nQBCxiZ/hBkCwnhBMS50YLe4pLj5cW5ruyp/BYj08qESmsTTzV80wOEA+Gu76dtOH\nRLcemNIjG5Gw6sPMorCxUz/Pk2pvpdC9Q8IgSjJidJAzQwyvKGxpOk2qB4Txp4dB\n10jxFLQZpNwXnlh8GOP5iKra7j55m4+F5POmldlJsI/wRh7SUz14eztxeCn63svq\nBUFw7iWMYjPX+kkppAKqyWVhcfbrVdCH0TcpeKGQLL+kFVZZ305As0Ty+itG0IhL\nnaT7y91jAgMBAAECggEABpywOTJZBAWvI4TGSgRwx0PLg6zNmOl6tMTkwmDs8j+z\ndGCJUTgSknodtYMVV1iXgUjgdyO5dSU96VpZJMXLN6gxcWy5OPYEco7clBjzhncn\nX3vDk1eSkHcdc0LG23FUo6vR1zN5MXHfh2UAwnljMvPHABowUdFpmHimjWvfkH+W\np9ilYsjbWC3+xgFM9gF69URBUsAA+9NLk/xjAlurJYNA9YxtzIWJQ93A2CtH+VWV\n6J8khelW4yr6rH/xOhN4GMNhr36/6DMnEYf2Q6bA1sCLCVq3bmHCprLWuCtL0Qu7\nPKU+RiaZuWnbKi8RqEinqlnlUFhiJg9LBrQCq3aepQKBgQDaC5g9AFO5pav8pWNe\nkl1LQM7fdOcjKWGp1/IE79/0auMyq8tsdcrmxPS6jwl6N/ps3KLZ/tkoWP8ZF04j\n4n3rPzOYPIMv3zznLxMaKPrMc9mT73Wzo/6EuyjR2wN4uzdpcTE9MO6u7zDXvDlZ\nTb1hmzpbupOWL6HdwTu2Y3PVpQKBgQDQfu5yP4hxCkbpVhafPEXcjiSxk8Y0O+Pw\n0+BwtL4KqEwlqAl5YTWwixMw4JL5PeGhTUNy6USxue0faBKIq2Sy3+7adJMfdiWQ\nPYEZNgtAUZ4Z4L7VBI0PzSpDTW2sMMK7vzOGSGOiKSZefFqHErWKEIKLpkYu3GLH\nxq9aIajIZwKBgF3AzIW2JUnWrVuldVONlWWtCQZVyqh4u5B+1IZA6ce7SdNYwM/y\n2fpdx2iL5iRR+3BhcfhPtum9UnpkZenSEhhbhYC4zCOCVjqFKC6AXk4Ypf4Q4UgL\nhH1nyAZrqFN6FDpXPDe2WXqISDUKrpHydjKIvw//6kOSWYPy+QzUOFMtAoGAWNhu\nFaM7Kihd9VqpAyv0/TpZKo61HFcVF+/BqWVrwjDbWgSUHPQuo89v2xknqCwVdN3u\nyw3aJv36rLJ1i2W14H+KUe7xLqvy79c1px+fhcYB4DckOrPYxI4B33IkNQcGRGkC\ntMsuIdD1N7g3/20ajP3iE05Eg/2H3metG3RSbysCgYAL7qVaCiPGXOAL/bps1SbF\nwnEZI1Yt32m3Qa+aTZGg7VgtmDM7PvLBInO+u6kS5QsaD3HEoTjcaxirNDTDx/fU\nyidtiITfPFEis0XHvFrFkxAZJz2ukoSomvFkFs0opjF8yv+8D5wSSyhBWTVhLnG8\nxIDFalBK1VZ7fNRe2nD+lg==\n-----END PRIVATE KEY-----\n",

    # the name of the experiment to use to track
    # logged metrics and parameters
    experiment='test1',

    # description of the experiment above
    experiment_description='chatbot test',
)

vertexai.init(project="forward-robot-392208", location="us-central1")
parameters = {
    "temperature": 1,
    "max_output_tokens": 256,
    "top_p": 0.8,
    "top_k": 40
}
model = TextGenerationModel.from_pretrained("text-bison@001")
response = model.predict(
    """You are an english teacher. You need to help the customer to get better. Feel free to correct them but also explain and give them where they were wrong, answer their questions to help them.

input: Hi.
output: Hi how are you ?

input: Heay.
output: I think you meant to say \"hey\".

input: Hello I´m trying to get better in English. Coorrect if im wrong.
Watever but how are you ?
output:
""",
    **parameters
)
print(f"Response from Model: {response.text}")