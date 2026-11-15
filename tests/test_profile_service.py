from backend.services.profile_service import ProfileService

profile = ProfileService()

print(profile.get_name())

print(profile.get_country())

print(profile.get_favorite_drink())