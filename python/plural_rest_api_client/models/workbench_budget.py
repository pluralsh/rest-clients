from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.workbench_budget_unit import WorkbenchBudgetUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkbenchBudget")


@_attrs_define
class WorkbenchBudget:
    """Token bucket budget configuration and current state for a workbench

    Attributes:
        enabled (bool | Unset): Whether budget tracking is enabled
        last (float | Unset): Remaining budget capacity
        last_updated (datetime.datetime | Unset): When the budget was last updated
        maximum (float | Unset): Maximum budget capacity
        min_free (float | Unset): Minimum budget capacity to keep free
        unit (WorkbenchBudgetUnit | Unset): The budget unit
    """

    enabled: bool | Unset = UNSET
    last: float | Unset = UNSET
    last_updated: datetime.datetime | Unset = UNSET
    maximum: float | Unset = UNSET
    min_free: float | Unset = UNSET
    unit: WorkbenchBudgetUnit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        last = self.last

        last_updated: str | Unset = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        maximum = self.maximum

        min_free = self.min_free

        unit: str | Unset = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if last is not UNSET:
            field_dict["last"] = last
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated
        if maximum is not UNSET:
            field_dict["maximum"] = maximum
        if min_free is not UNSET:
            field_dict["min_free"] = min_free
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        last = d.pop("last", UNSET)

        _last_updated = d.pop("last_updated", UNSET)
        last_updated: datetime.datetime | Unset
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = datetime.datetime.fromisoformat(_last_updated)

        maximum = d.pop("maximum", UNSET)

        min_free = d.pop("min_free", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: WorkbenchBudgetUnit | Unset
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = WorkbenchBudgetUnit(_unit)

        workbench_budget = cls(
            enabled=enabled,
            last=last,
            last_updated=last_updated,
            maximum=maximum,
            min_free=min_free,
            unit=unit,
        )

        workbench_budget.additional_properties = d
        return workbench_budget

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
