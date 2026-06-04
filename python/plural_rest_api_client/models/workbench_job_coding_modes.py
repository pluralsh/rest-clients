from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkbenchJobCodingModes")


@_attrs_define
class WorkbenchJobCodingModes:
    """Coding mode options for a workbench job

    Attributes:
        approval (bool | Unset): Whether coding agent runs require approval before continuing
        babysit (bool | Unset): Whether babysit mode is enabled for coding agent runs
    """

    approval: bool | Unset = UNSET
    babysit: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        approval = self.approval

        babysit = self.babysit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if approval is not UNSET:
            field_dict["approval"] = approval
        if babysit is not UNSET:
            field_dict["babysit"] = babysit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        approval = d.pop("approval", UNSET)

        babysit = d.pop("babysit", UNSET)

        workbench_job_coding_modes = cls(
            approval=approval,
            babysit=babysit,
        )

        workbench_job_coding_modes.additional_properties = d
        return workbench_job_coding_modes

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
