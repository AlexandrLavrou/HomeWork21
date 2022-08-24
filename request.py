#
#
# class Request:
#
#     def __init__(self, storage_list, request_str):
#         req_list = request_str.split()
#         action = req_list[0]
#         self._count = int(req_list[1])
#         self._item = req_list[2]
#         if req_list[4] or req_list[6] in storage_list:
#             if action == "Доставить":
#                 self._from = req_list[4]
#                 self._to = req_list[6]
#             if action == "Забрать":
#                 self._from = req_list[4]
#                 self._to = None
#             if action == "Привезти":
#                 self._to = req_list[4]
#                 self._from = None
#
#     def move(self):
#         if self._to and self._from:
#             if eval(self._to).add(self._item, self._count):
#                 eval(self._from).remove(self._item, self._count)
#         elif self._to:
#             eval(self._to).add(self._item, self._count)
#         elif self._from:
#             eval(self._from).remove(self._item, self._count)


from extender import storage_list


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
        #     print("ups some thing whent wrong")

