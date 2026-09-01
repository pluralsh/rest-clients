from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workbench_job_modes import WorkbenchJobModes


T = TypeVar("T", bound="QueuedPromptInput")


@_attrs_define
class QueuedPromptInput:
    """Input for creating a deferred workbench prompt

    Attributes:
        dequeable_at (datetime.datetime): When the prompt becomes eligible to dequeue
        prompt (str): The prompt to send when dequeued
        modes (WorkbenchJobModes | Unset): Mode-specific options for a workbench job
    """

    dequeable_at: datetime.datetime
    prompt: str
    modes: WorkbenchJobModes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dequeable_at = self.dequeable_at.isoformat()

        prompt = self.prompt

        modes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.modes, Unset):
            modes = self.modes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dequeable_at": dequeable_at,
                "prompt": prompt,
            }
        )
        if modes is not UNSET:
            field_dict["modes"] = modes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.workbench_job_modes import WorkbenchJobModes

        d = dict(src_dict)
        dequeable_at = datetime.datetime.fromisoformat(d.pop("dequeable_at"))

        prompt = d.pop("prompt")

        _modes = d.pop("modes", UNSET)
        modes: WorkbenchJobModes | Unset
        if isinstance(_modes, Unset):
            modes = UNSET
        else:
            modes = WorkbenchJobModes.from_dict(_modes)

        queued_prompt_input = cls(
            dequeable_at=dequeable_at,
            prompt=prompt,
            modes=modes,
        )

        queued_prompt_input.additional_properties = d
        return queued_prompt_input

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
