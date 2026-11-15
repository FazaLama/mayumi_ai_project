class IntentClassifier:

    def classify(self, text: str):

        text = text.lower()

        # Open Notepad
        if any(keyword in text for keyword in [
            "notepad",
            "catatan",
            "menulis",
            "note"
        ]):
            return "open_notepad"

        # Calculator
        if any(keyword in text for keyword in [
            "calculator",
            "kalkulator",
            "hitung"
        ]):
            return "open_calculator"

        # Time
        if any(keyword in text for keyword in [
            "jam",
            "waktu",
            "pukul"
        ]):
            return "get_time"

        # Date
        if any(keyword in text for keyword in [
            "tanggal",
            "hari ini"
        ]):
            return "get_date"

        return None