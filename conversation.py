import vertexai
from vertexai.language_models import TextGenerationModel
from google.cloud import aiplatform

aiplatform.init(
    # your Google Cloud Project ID or number
    # environment default used is not set
    project='my-project',

    # the Vertex AI region you will use
    # defaults to us-central1
    location='us-central1',

    # Google Cloud Storage bucket in same region as location
    # used to stage artifacts
    staging_bucket='gs://my_staging_bucket',

    # custom google.auth.credentials.Credentials
    # environment default creds used if not set
    credentials=my_credentials,

    # customer managed encryption key resource name
    # will be applied to all Vertex AI resources if set
    encryption_spec_key_name=my_encryption_key_name,

    # the name of the experiment to use to track
    # logged metrics and parameters
    experiment='my-experiment',

    # description of the experiment above
    experiment_description='my experiment decsription'
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