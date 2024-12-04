import re

class LinkValidator:
    @staticmethod
    def validate(link: str) -> bool:
        regex = re.compile(
            r'^(https?://)?'  # http:// or https://
            r'([a-zA-Z0-9.-]+)'  # Domain name
            r'(:[0-9]{1,5})?'  # Port (optional)
            r'(/.*)?$'  # Path (optional)
        )
        return re.match(regex, link) is not None
