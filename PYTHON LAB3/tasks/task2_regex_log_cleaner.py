import re
from tasks.decorators import log_time
import random

def generate_fake_logs():
    emails = [f"user{n}@example.com" for n in range(5)]
    invalids = ["notanemail", "123@", "@nope.com", "foo.bar", "test@@test.com"]
    lines = emails + invalids
    random.shuffle(lines)
    with open('access.log', 'w') as f:
        for line in lines:
            f.write(line + '\n')

@log_time
def regex_log_cleaner():
    generate_fake_logs()
    with open('access.log', 'r') as f:
        content = f.read()
    emails = set(re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", content))
    with open('valid_emails.txt', 'w') as f:
        for email in emails:
            f.write(email + '\n')
    print(f"Found {len(emails)} unique valid emails.")
