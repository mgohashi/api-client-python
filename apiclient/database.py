from asyncio import sleep
from logging import getLogger


class InMemoryStorage:
    DELAY=.1
    __db__ = {}
    logger = getLogger(__name__)

    def __init__(self):
        pass

    @classmethod
    async def __save_obj__(cls, db_name, obj, update_criteria):
        await sleep(cls.DELAY)
        if update_criteria:
            try:
                found = next(iter(await cls.__find_obj__(db_name, update_criteria)))
                if found:
                    cls.logger.debug("Updating item...")
                    found.__merge__(obj)
                    cls.logger.debug("Item updated!")

                    await cls.__print_db__()

                    return found
            except StopIteration:
                cls.logger.debug("Item not found in DB!")

        cls.__db__[db_name].append(obj)

        await cls.__print_db__()

        return obj

    @classmethod
    async def __find_obj__(cls, db_name, criteria):
        await sleep(cls.DELAY)
        return (item for item in cls.__db__[db_name]
                if criteria(item))

    @classmethod
    async def __remove_obj__(cls, db_name, criteria):
        await sleep(cls.DELAY)
        to_remove = [item for item in cls.__db__[db_name] if criteria(item)]

        if not to_remove:
            return None

        for item in to_remove:
            cls.__db__[db_name].remove(item)

        await cls.__print_db__()

        return to_remove

    @classmethod
    async def __remove_all__(cls, db_name):
        await sleep(cls.DELAY)
        cls.__db__[db_name].clear()
        await cls.__print_db__()

    @classmethod
    async def __print_db__(cls):
        cls.logger.debug("")
        cls.logger.debug("##### Data Base Updated #####")
        cls.logger.debug(f"{cls.__db__}")
        cls.logger.debug("#############################")
        cls.logger.debug("")


