from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.workbench_job_model_provider import WorkbenchJobModelProvider

T = TypeVar("T", bound="WorkbenchJobModel")


@_attrs_define
class WorkbenchJobModel:
    """Model override for a workbench job

    Attributes:
        model (str): The model name for this job
        provider (WorkbenchJobModelProvider): The AI provider for this job
    """

    model: str
    provider: WorkbenchJobModelProvider
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model

        provider = self.provider.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
                "provider": provider,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        model = d.pop("model")

        provider = WorkbenchJobModelProvider(d.pop("provider"))

        workbench_job_model = cls(
            model=model,
            provider=provider,
        )

        workbench_job_model.additional_properties = d
        return workbench_job_model

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
