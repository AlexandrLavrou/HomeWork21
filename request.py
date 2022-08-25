from extender import storage_dict


class Request:

    def __init__(self, storage_dict, request_str):
        req_list = request_str.split()
        self._from = req_list[1]
        self._to = req_list[3]
        self._count = int(req_list[5])
        self._item = req_list[6]
        self.storage_dict = storage_dict

    def move(self):
        if self._from and self._to in self.storage_dict.keys():
            self.storage_dict[self._from].remove(self._item, self._count)
            self.storage_dict[self._to].add(self._item, self._count)
