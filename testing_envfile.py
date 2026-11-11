import os
from dotenv import load_dotenv


load_dotenv()
print(os.getenv("PROJECT_ACCESS_TOKEN"))
# issue found -> accessing a env variable that is not defined

print(os.getenv("PROJECT_ID"))
print(os.getenv("GITLAB_API_KEY"))