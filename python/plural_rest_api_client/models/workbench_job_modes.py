from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workbench_job_coding_modes import WorkbenchJobCodingModes


T = TypeVar("T", bound="WorkbenchJobModes")


@_attrs_define
class WorkbenchJobModes:
    """Mode-specific options for a workbench job

    Attributes:
        coding (WorkbenchJobCodingModes | Unset): Coding mode options for a workbench job
        plan (bool | Unset): Whether planning mode is enabled for this job
    """

    coding: WorkbenchJobCodingModes | Unset = UNSET
    plan: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        coding: dict[str, Any] | Unset = UNSET
        if not isinstance(self.coding, Unset):
            coding = self.coding.to_dict()

        plan = self.plan

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if coding is not UNSET:
            field_dict["coding"] = coding
        if plan is not UNSET:
            field_dict["plan"] = plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workbench_job_coding_modes import WorkbenchJobCodingModes

        d = dict(src_dict)
        _coding = d.pop("coding", UNSET)
        coding: WorkbenchJobCodingModes | Unset
        if isinstance(_coding, Unset):
            coding = UNSET
        else:
            coding = WorkbenchJobCodingModes.from_dict(_coding)

        plan = d.pop("plan", UNSET)

        workbench_job_modes = cls(
            coding=coding,
            plan=plan,
        )

        workbench_job_modes.additional_properties = d
        return workbench_job_modes

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
