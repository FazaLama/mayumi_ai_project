from backend.profile.profile_manager import ProfileManager


class ProfileService:

    def __init__(self):

        self.manager = ProfileManager()

    # ==========================
    # GET PROFILE
    # ==========================

    def get_profile(self):

        return self.manager.load()

    # ==========================
    # GET NAME
    # ==========================

    def get_name(self):

        return self.manager.load().name

    # ==========================
    # GET COUNTRY
    # ==========================

    def get_country(self):

        return self.manager.load().country

    # ==========================
    # GET FAVORITE DRINK
    # ==========================

    def get_favorite_drink(self):

        return self.manager.load().favorite_drink