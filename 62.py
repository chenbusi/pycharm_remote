def get_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")


get_age(-1)
