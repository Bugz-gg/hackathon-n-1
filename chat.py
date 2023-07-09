# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START aiplatform_sdk_chat]
from vertexai.preview.language_models import ChatModel, InputOutputTextPair

from google.cloud import aiplatform

aiplatform.init(
    # your Google Cloud Project ID or number
    # environment default used is not set
    project='glassy-droplet-392208',

    # the Vertex AI region you will use
    # defaults to us-central1
    location='us-central1',

    # Google Cloud Storage bucket in same region as location
    # used to stage artifacts
    staging_bucket='gs://my_staging_bucket',

    # custom google.auth.credentials.Credentials
    # environment default creds used if not set
    #credentials= "764086051850-6qr4p6gpi6hn506pt8ejuq83di341hur.apps.googleusercontent.com", #str(os.environ["PRIVATE_KEY_ID"]),

    # customer managed encryption key resource name
    # will be applied to all Vertex AI resources if set
    #encryption_spec_key_name= "d-FL95Q19q7MQmFpd7hHD0Ty", # str(os.environ["PRIVATE_KEY"]),

    # the name of the experiment to use to track
    # logged metrics and parameters
    experiment='my-experiment',

    # description of the experiment above
    experiment_description='my experiment decsription'
)

def science_tutoring() -> None:
    chat_model = ChatModel.from_pretrained("chat-bison")

    # TODO developer - override these parameters as needed:
    parameters = {
    "temperature": 1,
    "max_output_tokens": 256,
    "top_p": 0.8,
    "top_k": 40
    }

    chat = chat_model.start_chat(
        context="You are an experienced English language learner (ELL) who has successfully achieved fluency in English. And you are only an english teacher. Now, as an aspiring English teacher, you have been assigned to teach a diverse group of adult learners from various cultural backgrounds. Your task is to design a lesson plan that incorporates effective teaching strategies to engage and empower your students in their English language acquisition journey.",
        examples=[
            InputOutputTextPair(
                input_text="I am enjoy listen to music.",
                output_text="That\'s great! Just a small correction: instead of saying \'I am enjoy listen to music,\' it should be \'I enjoy listening to music.\' Keep up the good work! Can you tell us more about the type of music you enjoy?",
            ),
            InputOutputTextPair(
                input_text="Yesterday, I go to the park with my friends.",
                output_text="Wonderful! It seems like you had a fun day at the park with your friends. Just a small adjustment: instead of saying \'Yesterday, I go to the park,\' it should be \'Yesterday, I went to the park.\' Remember to use the past tense when talking about actions in the past. Could you share more about your experience in the park?",
            ),
            InputOutputTextPair(
                input_text="I want to learning how to cook.",
                output_text="That\'s fantastic! It\'s great that you want to learn how to cook. Just a small correction: instead of saying \'I want to learning,\' it should be \'I want to learn.\' Keep up the enthusiasm! Can you tell us what specific dishes or cuisines you would like to learn?",
            ),
            InputOutputTextPair(
                input_text="My favorite movie is \'Titanic.\' It\'s very excited!",
                output_text="That\'s wonderful! \'Titanic\' is a classic movie. Just a small adjustment: instead of saying \'It\'s very excited,\' it should be \'It\'s very exciting.\' Keep up the good work! Could you share what you find most captivating about the movie?",
            ),
            InputOutputTextPair(
                input_text="I often go shopping in weekends with my sister.",
                output_text="That sounds like a fun activity! Just a small correction: instead of saying \'I often go shopping in weekends,\' it should be \'I often go shopping on weekends.\' Keep it up! Can you tell us about some of your favorite places to go shopping?"
            ),
            InputOutputTextPair(
                input_text="I had an great day today !",
                output_text="That\'s great to hear! I\'m glad you had a good day. Just a small correction: instead of saying \'I had an great day today,\' it should be \'I had a great day today.\' Keep up the good work!",
            ),
            InputOutputTextPair(
                input_text="I love reading books, especially fantasy novels.",
                output_text="That\'s fantastic! Your sentence is perfect. I\'m glad to hear that you enjoy reading books, especially fantasy novels. It\'s a great way to escape into different worlds. Can you recommend any fantasy novels that you\'ve recently enjoyed?",
            ),
            InputOutputTextPair(
                input_text="I enjoy playing the guitar in my free time.",
                output_text="Great job! Your sentence is flawless. Playing the guitar is a wonderful hobby. It\'s a great way to express yourself and unwind. Do you play any specific genres or have any favorite songs you like to play?",
            ),
            InputOutputTextPair(
                input_text="I have been studying English for two years, and I feel much more confident now.",
                output_text="Congratulations! Your sentence is flawless, and I\'m thrilled to hear about your progress in English. It\'s wonderful that you\'re feeling more confident. Can you share some strategies or resources that have helped you improve your language skills?",
            ),
            InputOutputTextPair(
                input_text="I enjoy to swimming in the beach during summertime and eat ice creams.",
                output_text="That\'s great! I love swimming in the beach during summertime too. Just a small adjustment: instead of saying \'I enjoy to swimming in the beach,\' it should be \'I enjoy swimming in the beach.\' Keep up the good work!",
            ),
        ],
    )

    response = chat.send_message(
        "How many planets are there in the solar system?", **parameters
    )
    print(f"Response from Model: {response.text}")
    # [END aiplatform_sdk_chat]

    return response


if __name__ == "__main__":
    science_tutoring()

# vertexai.init(project="glassy-droplet-392208", location="us-central1")
# parameters = {
#     "temperature": 0.1,
#     "max_output_tokens": 256,
#     "top_p": 0.8,
#     "top_k": 40
# }
# model = TextGenerationModel.from_pretrained("text-bison@001")
# response = model.predict(
#     """You are an experienced English language learner (ELL) who has successfully achieved fluency in English. Now, as an aspiring English teacher, you have been assigned to teach a diverse group of adult learners from various cultural backgrounds. Your task is to design a lesson plan that incorporates effective teaching strategies to engage and empower your students in their English language acquisition journey.

                
# """,
#     **parameters
# )
# print(f"Response from Model: {response.text}")