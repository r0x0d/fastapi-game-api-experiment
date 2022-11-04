from carnage.api.schemas.spell.spell import (
    CreateSpellSchema,
    ListSpellSchema,
    UpdateSpellSchema,
)
from carnage.api.schemas.spell.spell_duration_type import (
    CreateSpellDurationTypeSchema,
    ListSpellDurationTypeSchema,
    UpdateSpellDurationTypeSchema,
)
from carnage.api.schemas.spell.spell_range_type import (
    CreateSpellRangeTypeSchema,
    ListSpellRangeTypeSchema,
    UpdateSpellRangeTypeSchema,
)
from carnage.api.schemas.spell.spell_school import (
    CreateSpellSchoolSchema,
    ListSpellSchoolSchema,
    UpdateSpellSchoolSchema,
)

__all__ = (
    "CreateSpellSchema",
    "ListSpellSchema",
    "UpdateSpellSchema",
    "CreateSpellSchoolSchema",
    "ListSpellSchoolSchema",
    "UpdateSpellSchoolSchema",
    "CreateSpellRangeTypeSchema",
    "ListSpellRangeTypeSchema",
    "UpdateSpellRangeTypeSchema",
    "CreateSpellDurationTypeSchema",
    "ListSpellDurationTypeSchema",
    "UpdateSpellDurationTypeSchema",
)
