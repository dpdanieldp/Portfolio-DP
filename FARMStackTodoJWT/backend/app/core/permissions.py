SCOPES = {
    "todo:get_my": "Required to get current user's todos- default for all users",
    "todo:create": "Required to create todos- default for all users",
    "todo:update": "Required to update todos- default for all users",
    "todo:delete": "Required to delete todos- special permission- may be granted by admin",
    "admin": "Admin permission, required to perform all admin actions",
}

DEFAULT_SCOPES = [
    "todo:get_my",
    "todo:create",
    "todo:update",
]
