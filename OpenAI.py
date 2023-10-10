import os
import openai
from Apikey import key

openai.api_key = key

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write an a email for birthday wishing\n\nSubject: Birthday Wishes\n\nDear [Recipient], \n\nI hope your special day brings you lots of joy, love, and happiness. Wishing you a very happy birthday! \n\nThis is a reminder of how much joy and light you bring into all the lives you touch. Let this special day bring you all the wonderful things that life has to offer. \n\nHave a great day! \n\nWarmly, \n[Your Name]",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)


# {
#   "id": "chatcmpl-87k4m029A1V9wOM9qTycNVOLtxF2w",
#   "object": "chat.completion",
#   "created": 1696856104,
#   "model": "gpt-3.5-turbo-0613",
#   "choices": [
#     {
#       "index": 0,
#       "message": {
#         "role": "assistant",
#         "content": "your special day! I hope this email finds you surrounded by love, joy, and happiness as you celebrate another year of your life. \n\nOn this memorable occasion, I wanted to take a moment to express my heartfelt birthday wishes for you. You are one of the most amazing individuals I have had the pleasure of knowing, and I feel truly blessed to share this journey of life with you.\n\nYou bring an incredible light to every room you enter, illuminating the lives of those around you with your infectious laughter, kindness, and genuine care. Your presence alone can turn any ordinary gathering into a memorable and joyous occasion.\n\nI admire your resilience, your unwavering determination, and your never-ending pursuit of personal and professional growth. Your ambition is inspiring, and I have no doubt that you will continue to achieve remarkable things in the years to come.\n\nToday, I hope you take the time to indulge in the things that bring you happiness. May this day be filled with countless sweet moments, laughter, and unforgettable memories. Surround yourself with loved ones who appreciate and cherish you, just as I do.\n\nAs you blow out the candles on your birthday cake, I wish for all your dreams to come true. May your life be dotted with success, good health, and abundant opportunities."
#       },
#       "finish_reason": "length"
#     }
#   ],
#   "usage": {
#     "prompt_tokens": 42,
#     "completion_tokens": 256,
#     "total_tokens": 298
#   }
# }
#
#
# {
#   "warning": "This model version is deprecated. Migrate before January 4, 2024 to avoid disruption of service. Learn more https://platform.openai.com/docs/deprecations",
#   "id": "cmpl-87kRN4NdI5bL8tWwJoDgRWr1PrRZo",
#   "object": "text_completion",
#   "created": 1696857505,
#   "model": "text-davinci-003",
#   "choices": [
#     {
#       "text": "",
#       "index": 0,
#       "logprobs": null,
#       "finish_reason": "stop"
#     }
#   ],
#   "usage": {
#     "prompt_tokens": 107,
#     "total_tokens": 107
#   }
# }