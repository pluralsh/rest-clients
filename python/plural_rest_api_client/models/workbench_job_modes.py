from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workbench_job_coding_modes import WorkbenchJobCodingModes
    from ..models.workbench_job_model import WorkbenchJobModel


T = TypeVar("T", bound="WorkbenchJobModes")


@_attrs_define
class WorkbenchJobModes:
    """Mode-specific options for a workbench job

    Attributes:
        coding (WorkbenchJobCodingModes | Unset): Coding mode options for a workbench job
        model (WorkbenchJobModel | Unset): Model override for a workbench job
        plan (bool | Unset): Whether planning mode is enabled for this job
        verification (bool | Unset): Whether verification mode is enabled for this job
    """

    coding: WorkbenchJobCodingModes | Unset = UNSET
    model: WorkbenchJobModel | Unset = UNSET
    plan: bool | Unset = UNSET
    verification: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        coding: dict[str, Any] | Unset = UNSET
        if not isinstance(self.coding, Unset):
            coding = self.coding.to_dict()

        model: dict[str, Any] | Unset = UNSET
        if not isinstance(self.model, Unset):
            model = self.model.to_dict()

        plan = self.plan

        verification = self.verification

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if coding is not UNSET:
            field_dict["coding"] = coding
        if model is not UNSET:
            field_dict["model"] = model
        if plan is not UNSET:
            field_dict["plan"] = plan
        if verification is not UNSET:
            field_dict["verification"] = verification

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.workbench_job_coding_modes import (
            WorkbenchJobCodingModes,
        )
        from ..models.workbench_job_model import WorkbenchJobModel

        d = dict(src_dict)
        _coding = d.pop("coding", UNSET)
        coding: WorkbenchJobCodingModes | Unset
        if isinstance(_coding, Unset):
            coding = UNSET
        else:
            coding = WorkbenchJobCodingModes.from_dict(_coding)

        _model = d.pop("model", UNSET)
        model: WorkbenchJobModel | Unset
        if isinstance(_model, Unset):
            model = UNSET
        else:
            model = WorkbenchJobModel.from_dict(_model)

        plan = d.pop("plan", UNSET)

        verification = d.pop("verification", UNSET)

        workbench_job_modes = cls(
            coding=coding,
            model=model,
            plan=plan,
            verification=verification,
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
