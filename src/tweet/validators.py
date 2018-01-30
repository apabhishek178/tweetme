from django.core.exceptions import ValidationError

#make all your validations here

def validate_content(value):
    content = value
    if content == 'abc':
        raise ValidationError("Content cannot be abc")
    return value
