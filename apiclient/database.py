from logging import getLogger


class InMemoryStorage:
    __db__ = {}
    logger = getLogger(__name__)

    def __init__(self):
        pass

    @classmethod
    def __save_obj__(cls, db_name, obj, update_criteria):
        if update_criteria:
            try:
                found = next(iter(cls.__find_obj__(db_name, update_criteria)))
                if found:
                    cls.logger.debug("Updating item...")
                    found.__merge__(obj)
                    cls.logger.debug("Item updated!")

                    cls.__print_db__()

                    return found
            except StopIteration:
                cls.logger.debug("Item not found in DB!")

        cls.__db__[db_name].append(obj)

        cls.__print_db__()

        return obj

    @classmethod
    def __find_obj__(cls, db_name, criteria):
        return (item for item in cls.__db__[db_name]
                if criteria(item))

    @classmethod
    def __remove_obj__(cls, db_name, criteria):
        to_remove = [item for item in cls.__db__[db_name] if criteria(item)]

        if not to_remove:
            return None

        for item in to_remove:
            cls.__db__[db_name].remove(item)

        cls.__print_db__()

        return to_remove

    @classmethod
    def __print_db__(cls):
        print()
        print("##### Data Base Updated #####")
        print(f"{cls.__db__}")
        print()


