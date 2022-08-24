
class Request:

    def __init__(self, _list, request_str):
        req_list = request_str.split()
        self._from = req_list[1]
        self._to = req_list[3]
        self._count = int(req_list[5])
        self._item = req_list[6]
        self._list = _list

    def move(self):
        # if self._to and self._from in self._list:
        exec(self._to).add(self._item, self._count)
        exec(self._from).remove(self._item, self._count)
        # else:
        #     print("ups some thing went wrong")

