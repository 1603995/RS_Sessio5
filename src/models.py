import json


class Task:
    ESTAT_PENDENT = "pendent"

    def __init__(self, id, titol=None, assignatura=None, estat=None, **kwargs):
        self.id = int(id)
        self.titol = titol if titol is not None else kwargs.get("title", "")
        self.assignatura = (
            assignatura if assignatura is not None else kwargs.get("subject", "")
        )
        self.estat = (
            estat if estat is not None else kwargs.get("status", self.ESTAT_PENDENT)
        )

    @property
    def title(self):
        return self.titol

    @property
    def subject(self):
        return self.assignatura

    @property
    def status(self):
        return self.estat

    def to_dict(self):
        return {
            "id": self.id,
            "títol": self.titol,
            "assignatura": self.assignatura,
            "estat": self.estat,
        }

    @classmethod
    def from_dict(cls, dades):
        return cls(
            id=dades["id"],
            titol=dades.get("títol", dades.get("title", "")),
            assignatura=dades.get("assignatura", dades.get("subject", "")),
            estat=dades.get("estat", dades.get("status", cls.ESTAT_PENDENT)),
        )

    def to_json(self):
        return json.dumps(self.to_dict(), ensure_ascii=False)

    @classmethod
    def from_json(cls, cadena):
        if isinstance(cadena, dict):
            return cls.from_dict(cadena)
        return cls.from_dict(json.loads(cadena))

    def __str__(self):
        return f"[{self.id}] {self.titol} ({self.assignatura}) - estat: {self.estat}"

    def __repr__(self):
        return (
            f"Task(id={self.id!r}, titol={self.titol!r}, "
            f"assignatura={self.assignatura!r}, estat={self.estat!r})"
        )


Tasca = Task
