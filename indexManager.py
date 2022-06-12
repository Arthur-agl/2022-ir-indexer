
from typing import List, Tuple


class IndexManager:
    index = {}
    doc_id = 1

    def add_entries(self, elements: List[Tuple[str, int]]):
        for element in elements:
            self.add_entry(element)

        self.doc_id += 1

    def add_entry(self, element: Tuple[str, int]):
        if element[0] not in self.index:
            self.index[element[0]] = []

        self.index[element[0]].append((self.doc_id, element[1]))

    def get_index(self):
        return self.index
