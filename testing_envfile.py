import os
from dotenv import load_dotenv
import sys


# load_dotenv()
# print(os.getenv("PROJECT_ACCESS_TOKEN"))
# # issue found -> accessing a env variable that is not defined
#
# print(os.getenv("PROJECT_ID"))
# print(os.getenv("GITLAB_API_KEY"))

everything = sys.argv
argument0 = sys.argv[0]
argument2 = sys.argv[1]
out_of_bounds = sys.argv[2]

print(everything)
print(argument0)
print(argument2)
print(out_of_bounds)