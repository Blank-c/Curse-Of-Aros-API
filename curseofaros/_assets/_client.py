from aiohttp import ClientSession
from sys import maxsize, _getframe
from curseofaros._assets.errors import *

class Client:
    
    def __level(self, xp):
        level_table = [0, 46, 99, 159, 229, 309, 401, 507, 628, 768, 928, 1112, 1324, 1567, 1847, 2168, 2537, 2961, 3448, 4008, 4651, 5389, 6237, 7212, 8332, 9618, 11095, 12792, 14742, 16982, 19555, 22510, 25905, 29805, 34285, 39431, 45342, 52132, 59932, 68892, 79184, 91006, 104586, 120186, 138106, 158690, 182335, 209496, 240696, 276536, 317705, 364996, 419319, 481720, 553400, 635738, 730320, 838966, 963768, 1107128, 1271805, 1460969, 1678262, 1927866, 2214586, 2543940, 2922269, 3356855, 3856063, 4429503, 5088212, 5844870, 6714042, 7712459, 8859339, 10176758, 11690075, 13428420, 15425254, 17719014, 20353852, 23380486, 26857176, 30850844, 35438364, 40708040, 46761308, 53714688, 61702024, 70877064, 81416417, 93522954, 107429714, 123404386, 141754466, 162833172, 187046247, 214859767, 246809111, 283509271, 325666684, 374092835, 429719875, 493618564, 567018884, 651333710, 748186012, 859440093, 987237472, 1134038112, 1302667765, 1496372370, 1718880532, 1974475291, 2268076571, 2605335878, 2992745089, 3437761413, 3948950932, 4536153492, 5210672106, maxsize]
        for i in range(len(level_table)):
            if (i == len(level_table) - 1) or (xp >= level_table[i] and xp < level_table[i + 1]):
                return i + 1
    
    async def __request(self, url):
        async with ClientSession() as session:
            async with session.get(url) as res:
                return await res.json()

    async def __stat(self, statname, name, startswith: bool= False , tries= 0, limit= None):
        if tries < 0:
            tries = 0
        if not startswith:
            tries= 0
        try:
            if limit is not None:
                limit = None if int(limit) < 0 else limit
        except ValueError:
            raise TypeError("Limit value must be an Integer or NoneType")
        page = 0
        rank = 1
        while True:
            if limit is not None:
                if page == limit + 1:
                    break
            r = await self.__request("https://curseofaros.com/highscores-" + statname  + ".json?p=" + str(page))
            if len(r) == 0:
                break
            for i in r:
                if not startswith:
                    found = i.get("name").lower() == name.lower().strip()
                if startswith:
                    found = i.get("name").lower().startswith(name.lower())
                if not found:
                    rank += 1
                else:
                    if tries == 0:
                        return {**i , **{"rank" : rank, "page" : page, "level" : self.__level(i.get("xp"))}}
                    else:
                        tries -= 1
            page += 1
        raise NotFound("Result not found!")

    async def melee(self, name: str, limit: int= None):
        try:
            if limit is not None and int(limit) < 1:
                limit = 1
        except ValueError:
            raise TypeError("Limit value must be an Integer or NoneType")
        return await self.__stat(_getframe().f_code.co_name, name, limit= limit)

    async def magic(self, name: str, limit: int= None):
        try:
            if limit is not None and int(limit) < 1:
                limit = 1
        except ValueError:
            raise TypeError("Limit value must be an Integer or NoneType")
        return await self.__stat(_getframe().f_code.co_name, name, limit= limit)
    
    async def mining(self, name: str, limit: int= None):
        try:
            if limit is not None and int(limit) < 1:
                limit = 1
        except ValueError:
            raise TypeError("Limit value must be an Integer or NoneType")
        return await self.__stat(_getframe().f_code.co_name, name, limit= limit)

    async def smithing(self, name: str, limit: int= None):
        try:
            if limit is not None and int(limit) < 1:
                limit = 1
        except ValueError:
            raise TypeError("Limit value must be an Integer or NoneType")
        return await self.__stat(_getframe().f_code.co_name, name, limit= limit)
        
    async def woodcutting(self, name: str, limit: int= None):
        try:
            if limit is not None and int(limit) < 1:
                limit = 1
        except ValueError:
            raise TypeError("Limit value must be an Integer or NoneType")
        return await self.__stat(_getframe().f_code.co_name, name, limit= limit)
        
    async def crafting(self, name: str, limit: int= None):
        try:
            if limit is not None and int(limit) < 1:
                limit = 1
        except ValueError:
            raise TypeError("Limit value must be an Integer or NoneType")
        return await self.__stat(_getframe().f_code.co_name, name, limit= limit)
        
    async def fishing(self, name: str, limit: int= None):
        try:
            if limit is not None and int(limit) < 1:
                limit = 1
        except ValueError:
            raise TypeError("Limit value must be an Integer or NoneType")
        return await self.__stat(_getframe().f_code.co_name, name, limit= limit)
        
    async def cooking(self, name: str, limit: int= None):
        try:
            if limit is not None and int(limit) < 1:
                limit = 1
        except ValueError:
            raise TypeError("Limit value must be an Integer or NoneType")
        return await self.__stat(_getframe().f_code.co_name, name, limit= limit)
        
    async def tailoring(self, name: str, limit: int= None):
        try:
            if limit is not None and int(limit) < 1:
                limit = 1
        except ValueError:
            raise TypeError("Limit value must be an Integer or NoneType")
        return await self.__stat(_getframe().f_code.co_name, name, limit= limit)
    
    async def g_melee(self, gname: str, place: int= 1, limit: int= None):
        gname = gname.strip().split()[0] + " "
        if place.__class__.__name__ != "int":
            raise TypeError("Place value must be an Integer")
        if limit is not None:
            if limit.__class__.__name__ != "int":
                raise TypeError("Limit value must be an Integer or NoneType")
        return await self.__stat(_getframe().f_code.co_name.replace("g_", ""), gname, limit= limit, startswith= True, tries= place - 1)
        
    async def g_magic(self, gname: str, place: int= 1, limit: int= None):
        gname = gname.strip().split()[0] + " "
        if place.__class__.__name__ != "int":
            raise TypeError("Place value must be an Integer")
        if limit is not None:
            if limit.__class__.__name__ != "int":
                raise TypeError("Limit value must be an Integer or NoneType")
        return await self.__stat(_getframe().f_code.co_name.replace("g_", ""), gname, limit= limit, startswith= True, tries= place - 1)
        
    async def g_mining(self, gname: str, place: int= 1, limit: int= None):
        gname = gname.strip().split()[0] + " "
        if place.__class__.__name__ != "int":
            raise TypeError("Place value must be an Integer")
        if limit is not None:
            if limit.__class__.__name__ != "int":
                raise TypeError("Limit value must be an Integer or NoneType")
        return await self.__stat(_getframe().f_code.co_name.replace("g_", ""), gname, limit= limit, startswith= True, tries= place - 1)
        
    async def g_smithing(self, gname: str, place: int= 1, limit: int= None):
        gname = gname.strip().split()[0] + " "
        if place.__class__.__name__ != "int":
            raise TypeError("Place value must be an Integer")
        if limit is not None:
            if limit.__class__.__name__ != "int":
                raise TypeError("Limit value must be an Integer or NoneType")
        return await self.__stat(_getframe().f_code.co_name.replace("g_", ""), gname, limit= limit, startswith= True, tries= place - 1)
        
    async def g_woodcutting(self, gname: str, place: int= 1, limit: int= None):
        gname = gname.strip().split()[0] + " "
        if place.__class__.__name__ != "int":
            raise TypeError("Place value must be an Integer")
        if limit is not None:
            if limit.__class__.__name__ != "int":
                raise TypeError("Limit value must be an Integer or NoneType")
        return await self.__stat(_getframe().f_code.co_name.replace("g_", ""), gname, limit= limit, startswith= True, tries= place - 1)
        
    async def g_crafting(self, gname: str, place: int= 1, limit: int= None):
        gname = gname.strip().split()[0] + " "
        if place.__class__.__name__ != "int":
            raise TypeError("Place value must be an Integer")
        if limit is not None:
            if limit.__class__.__name__ != "int":
                raise TypeError("Limit value must be an Integer or NoneType")
        return await self.__stat(_getframe().f_code.co_name.replace("g_", ""), gname, limit= limit, startswith= True, tries= place - 1)
        
    async def g_fishing(self, gname: str, place: int= 1, limit: int= None):
        gname = gname.strip().split()[0] + " "
        if place.__class__.__name__ != "int":
            raise TypeError("Place value must be an Integer")
        if limit is not None:
            if limit.__class__.__name__ != "int":
                raise TypeError("Limit value must be an Integer or NoneType")
        return await self.__stat(_getframe().f_code.co_name.replace("g_", ""), gname, limit= limit, startswith= True, tries= place - 1)
        
    async def g_cooking(self, gname: str, place: int= 1, limit: int= None):
        gname = gname.strip().split()[0] + " "
        if place.__class__.__name__ != "int":
            raise TypeError("Place value must be an Integer")
        if limit is not None:
            if limit.__class__.__name__ != "int":
                raise TypeError("Limit value must be an Integer or NoneType")
        return await self.__stat(_getframe().f_code.co_name.replace("g_", ""), gname, limit= limit, startswith= True, tries= place - 1)
        
    async def g_tailoring(self, gname: str, place: int= 1, limit: int= None):
        gname = gname.strip().split()[0] + " "
        if place.__class__.__name__ != "int":
            raise TypeError("Place value must be an Integer")
        if limit is not None:
            if limit.__class__.__name__ != "int":
                raise TypeError("Limit value must be an Integer or NoneType")
        return await self.__stat(_getframe().f_code.co_name.replace("g_", ""), gname, limit= limit, startswith= True, tries= place - 1)