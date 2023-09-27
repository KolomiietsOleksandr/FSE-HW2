from datetime import datetime
from user_list_generator import CustomUserListGenerator
from data_fetcher import CustomDataFetcher

if __name__ == "__main__":
    custom_base_url = "https://sef.podkolzin.consulting/api/users/lastSeen"
    desired_custom_count = 217

    custom_data_fetcher = CustomDataFetcher()
    custom_data = custom_data_fetcher.get_custom_data_from_url(custom_base_url, desired_custom_count)

    custom_user_list_generator = CustomUserListGenerator()
    custom_users = custom_user_list_generator.get_custom_users(custom_data)
    current_time = datetime.utcnow()

    for custom_user in custom_users:
        print(f"{custom_user.username} {(custom_user.last_seen)}")
