from functools import reduce


class HistoryEntry:

    def __init__(self, entry_id, entry_op_name, entry_op_value):
        self.id = entry_id
        self.op_name = entry_op_name
        self.op_value = entry_op_value


class History:

    def __init__(self, calc_ops):
        self._entries = []
        self._calc_ops = calc_ops

    def append(self, entry_op_name, entry_op_value):

        next_entry_id = max([entry.id for entry in self._entries] or [0]) + 1

        new_history_entry = HistoryEntry(
            next_entry_id, entry_op_name, entry_op_value)
        self._entries.append(new_history_entry)

    def remove(self, entry_id):
        for entry in self._entries:
            if entry.id == entry_id:
                self._entries.remove(entry)
                break

    def clear(self):
        self._entries.clear()

    def _calc_operation(self, result, entry):

        for calc_op in self._calc_ops:
            if entry.op_name == calc_op.command:
                return calc_op.fn(result, entry.op_value)

        return result

    @property
    def __dict__(self):
        return [entry.__dict__ for entry in self._entries]

    @property
    def result(self):
        return reduce(self._calc_operation, self._entries, 0)

    def __len__(self):
        return len(self._entries)

    def __iter__(self):
        return iter(self._entries)

    def __next__(self):
        return next(self._entries)
