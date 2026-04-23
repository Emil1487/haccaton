# entities/visitor.py

ORIGIN_COLORS = {
    "город": (100, 149, 237),
    "рынок": (244, 211, 94),
    "перевал": (120, 120, 120),
    "космопорт": (168, 218, 220),
    "неизвестно": (230, 57, 70)
}

class Visitor:
    def __init__(self, data: dict):
        self.name = data["name"]
        self.age = data["age"]
        self.origin = data["origin"]
        self.destination = data["destination"]
        self.portrait_path = data["portrait_path"]
        self.dialogue_id = data["dialogue_id"]
        self.energy_cost = data["energy_cost"]
        self.secret = data.get("secret")
        self.documents = data.get("documents", {})
        self.baggage = data.get("baggage", {})
        self.consequences = data.get("consequences", {})

    def get_document_info(self) -> str:
        return "\n".join(f"{k}: {v}" for k, v in self.documents.items())

    def get_baggage_info(self) -> str:
        return "\n".join(f"{k}: {v}" for k, v in self.baggage.items())

    def get_origin_color(self) -> tuple:
        return ORIGIN_COLORS.get(self.origin, (255, 255, 255))
