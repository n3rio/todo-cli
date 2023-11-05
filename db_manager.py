from tinydb import TinyDB, Query


class DBManager:
    def __init__(self, name: str, content: str, project: str = None, entry_type: str = None) -> None:
        self.project = project
        self.entry_type = entry_type
        self.db = self._get_db()

    def _get_db(self):
        """
        If no project, look in general
        """
        return "NOT IMPLEMENTED YET"

    def get_entry(self):
        """ 
        Return specific entry or list the entries
        that match the seaerch criteria
        Search criteria:
            - name (partial/complete)
            - content (partial/complete)
            - date (this one is a maybe)
        """
        return "NOT IMPLEMENTED YET"

    def add_entry(self):
        """ 
        Add entry, 
            - if no project, put in general
            - if no entry_type, set as scratch
        """
        return "NOT IMPLEMENTED YET"

    def list_entries(self):
        """ 
        - If project not None, list entry in project
        - If entry_type not None, look only that entry_type
        - If both above are None, list everything
        """
        return "NOT IMPLEMENTED YET"

    def update_entry(self):
        """
        Look for entry by name or UUID and replace with content
        """
        return "NOT IMPLEMENTED YET"
