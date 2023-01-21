class UrlExpiredError(Exception):
    @property
    def code(self):
        return 400

    @property
    def message(self):
        return "URL expired"


class UrlNotFoundError(Exception):
    @property
    def code(self):
        return 404

    @property
    def message(self):
        return "NOT FOUND"


class InvalidUrlError(Exception):
    @property
    def code(self):
        return 422

    @property
    def message(self):
        return "Invalid url"


class InvalidDaysError(Exception):
    @property
    def code(self):
        return 400

    @property
    def message(self):
        return "Insert value between 1 and 365"
