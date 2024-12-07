"""reports module"""


class Reports:
    """reports class"""

    def __init__(self, initial_data: list[int]):
        """constructor"""
        self.data = initial_data

        self.size = len(initial_data)
        self.ascending = False
        self.descending = False
        self.safe = self.is_safe()

    def is_safe(self) -> bool:
        """method to get indexes of bad levels"""
        ascending_bad_indexes = self.get_ascending_bad_indexes()
        descending_bad_indexes = self.get_descending_bad_indexes()
        step_bad_indexes = self.get_step_bad_indexes()
        if ascending_bad_indexes:
            if step_bad_indexes:
                if ascending_bad_indexes[0] == step_bad_indexes[0]:
                    return True
                else:
                    return False
            else:
                return True

        if descending_bad_indexes:
            if step_bad_indexes:
                if descending_bad_indexes[0] == step_bad_indexes[0]:
                    return True
                else:
                    return False
            else:
                return True

    def get_step_bad_indexes(self):
        bad_levels = []
        for level_index, level in enumerate(self.data):
            if level_index == self.size - 1:
                if len(bad_levels) <= 1:
                    return bad_levels
                else:
                    return None
            elif abs(level - self.data[level_index + 1]) > 3:
                bad_levels.append(level_index)

    def get_ascending_bad_indexes(self):
        bad_levels = []
        for level_index, level in enumerate(self.data):
            if level_index == self.size - 1:
                if len(bad_levels) <= 1:
                    return bad_levels
                else:
                    return None
            elif level > self.data[level_index + 1]:
                bad_levels.append(level_index)
            elif level == self.data[level_index + 1]:
                bad_levels.append(level_index)

    def get_descending_bad_indexes(self):
        bad_levels = []
        for level_index, level in enumerate(self.data):
            if level_index == self.size - 1:
                if len(bad_levels) <= 1:
                    return bad_levels
                else:
                    return None
            elif level < self.data[level_index + 1]:
                bad_levels.append(level_index)
            elif level == self.data[level_index + 1]:
                bad_levels.append(level_index)
