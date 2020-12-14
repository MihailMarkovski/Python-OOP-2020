# from Attributes_and_Methods.document_management_03E.project.category import Category
# from Attributes_and_Methods.document_management_03E.project.topic import Topic
# from Attributes_and_Methods.document_management_03E.project.document import Document


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        searched = [c for c in self.categories if c.id == category_id]
        if searched:
            category = searched[0]
            category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        searched = [t for t in self.topics if t.id == topic_id]
        if searched:
            topic = searched[0]
            topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        searched = [d for d in self.documents if d.id == document_id]
        if searched:
            document = searched[0]
            document.edit(new_file_name)

    def delete_category(self, category_id):
        searched = [c for c in self.categories if c.id == category_id]
        if searched:
            category = searched[0]
            self.categories.remove(category)

    def delete_topic(self, topic_id):
        searched = [t for t in self.topics if t.id == topic_id]
        if searched:
            topic = searched[0]
            self.topics.remove(topic)

    def delete_document(self, document_id):
        searched = [d for d in self.documents if d.id == document_id]
        if searched:
            document = searched[0]
            self.documents.remove(document)

    def get_document(self, document_id):
        searched = [d for d in self.documents if d.id == document_id]
        if searched:
            document = searched[0]
            return document

    def __repr__(self):
        result = ''
        for d in self.documents:
            result += f'{d}\n'
        return result


# c1 = Category(1, "work")
# t1 = Topic(1, "daily tasks", "C:\\work_documents")
# d1 = Document(1, 1, 1, "finilize project")
#
# d1.add_tag("urgent")
# d1.add_tag("work")
#
# storage = Storage()
# storage.add_category(c1)
# storage.add_topic(t1)
# storage.add_document(d1)
#
# print(c1)
# print(t1)
# print(storage.get_document(1))
# print(storage)
