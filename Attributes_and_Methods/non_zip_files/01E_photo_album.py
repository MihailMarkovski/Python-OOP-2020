class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(photos_count // 4)

    def add_photo(self, label: str):
        for page_num, page in enumerate(self.photos):
            if len(page) < 4:
                page.append(label)
                return f"{label} photo added successfully on page {page_num + 1}" \
                       f" slot {page.index(label) + 1}"
        return "No more free spots"

    def display(self):
        result = ''
        dashes = f"{'-' * 11}\n"
        for page in self.photos:
            result += dashes
            for i in range(len(page)):
                if i == len(page) - 1:
                    result += '[]'
                else:
                    result += '[] '
            result += '\n'
        result += dashes
        return result
