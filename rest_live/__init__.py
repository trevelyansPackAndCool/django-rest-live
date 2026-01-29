DEFAULT_GROUP_BY_FIELD = "pk"


def get_group_name(model_label) -> str:
    return f"RESOURCE-{model_label}"


CREATED = "CREATED"
UPDATED = "UPDATED"
DELETED = "DELETED"
