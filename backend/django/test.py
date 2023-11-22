import re


def ireplace(old, repl, text):
    return re.sub(
        b"(?P<matched_string>" + re.escape(old) + b")",
        repl,  # lambda m: repl,
        text,
        flags=re.IGNORECASE,
    )


class HttpResponse:
    def __init__(self, content=b"", *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Content is a bytestring. See the `content` property methods.
        self.content = content

    @property
    def content(self):
        return b"".join(self._container)

    @content.setter
    def content(self, value):
        content = bytes(value)
        self._container = [content]


def monkeypatch():
    original_content = HttpResponse.content

    @property  # type: ignore
    def content(self):
        x = original_content.fget(self)
        x = ireplace(b"</head>", b'<META name="x" content="y" />\g<matched_string>', x)
        return x

    @content.setter
    def content(self, value):
        return original_content.fset(self, value)

    HttpResponse.content = content


def main():
    monkeypatch()

    bla = HttpResponse(b"hello")
    bla.content = b"""
    <html>
        <HeAd>
            <title>bla</title>
        </hEaD>
        <body><p>bla</p></body>
    </html>
    """
    print(bla.content)


if __name__ == "__main__":
    main()
