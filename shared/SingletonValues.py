class Important:
    SERVER_FOR = "tab"
    SERVER_ROLE = "auth"


class SingletonValues:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SingletonValues, cls).__new__(cls)
        return cls._instance


    class Routes:
        pass


    class Values:
        BOT_ID = 1387687742875635733
        BOT_NAME = "Endless_Arcade"
        BOT_PREFIX = "."
        GUILD_ID = 1311538039465574440
        OWNERS = [744675594200940545, # bhindi
                  766314561623949413, # 710devil
                  755432975507652729, # angel
                  ]
