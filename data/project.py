from model.project import Project
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for _ in range(random.randrange(3, maxlen))])

testdata = [
    Project(
        name=random_string("Test dev project-", 5),
        status="development",
        view_state="private",
        description="This is test project"
    ),
    Project(
        name=random_string("Test pre project-", 5),
        status="stable",
        view_state="public",
        description=""
    )
]