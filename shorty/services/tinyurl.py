from ..base import ShortyBase
from ..errors import ShorteningError


class TinyURL(ShortyBase):
    def short(self, url: str) -> str:
        response = self.get(
            'http://tinyurl.com/api-create.php',
            params={'url': self.sanitize_url(url)}
        )
        if response.ok:
            return response.text.strip()

        raise ShorteningError(response.content)
