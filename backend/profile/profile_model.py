from dataclasses import dataclass, field


@dataclass
class UserProfile:

    name: str = ""
    nickname: str = ""

    country: str = ""
    city: str = ""

    job: str = ""
    school: str = ""

    birthday: str = ""

    favorite_food: str = ""
    favorite_drink: str = ""
    favorite_game: str = ""
    favorite_music: str = ""

    hobbies: list = field(default_factory=list)

    personality_traits: list = field(default_factory=list)

    goals: list = field(default_factory=list)