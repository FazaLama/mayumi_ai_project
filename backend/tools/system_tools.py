from datetime import datetime


class SystemTools:

    @staticmethod
    def get_time():

        now = datetime.now()

        return now.strftime("%H:%M:%S")

    @staticmethod
    def get_date():

        now = datetime.now()

        return now.strftime("%d-%m-%Y")