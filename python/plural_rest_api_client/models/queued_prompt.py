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


T = TypeVar("T", bound="QueuedPrompt")


@_attrs_define
class QueuedPrompt:
    """A deferred prompt queued for a workbench job.  The prompt will wait for the job to settle and for its dequeuable
    time to elapse before being sent to the job.

        Attributes:
            consumed_at (datetime.datetime | Unset): When the prompt was consumed
            dequeable_at (datetime.datetime | Unset): When the prompt becomes eligible to dequeue
            id (str | Unset): Unique identifier for the queued prompt
            inserted_at (datetime.datetime | Unset):
            modes (WorkbenchJobModes | Unset): Mode-specific options for a workbench job
            prompt (str | Unset): The prompt text
            updated_at (datetime.datetime | Unset):
            user_id (str | Unset): ID of the user this prompt runs as
            workbench_job_id (str | Unset): ID of the workbench job this prompt targets
    """

    consumed_at: datetime.datetime | Unset = UNSET
    dequeable_at: datetime.datetime | Unset = UNSET
    id: str | Unset = UNSET
    inserted_at: datetime.datetime | Unset = UNSET
    modes: WorkbenchJobModes | Unset = UNSET
    prompt: str | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    user_id: str | Unset = UNSET
    workbench_job_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        consumed_at: str | Unset = UNSET
        if not isinstance(self.consumed_at, Unset):
            consumed_at = self.consumed_at.isoformat()

        dequeable_at: str | Unset = UNSET
        if not isinstance(self.dequeable_at, Unset):
            dequeable_at = self.dequeable_at.isoformat()

        id = self.id

        inserted_at: str | Unset = UNSET
        if not isinstance(self.inserted_at, Unset):
            inserted_at = self.inserted_at.isoformat()

        modes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.modes, Unset):
            modes = self.modes.to_dict()

        prompt = self.prompt

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        user_id = self.user_id

        workbench_job_id = self.workbench_job_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if consumed_at is not UNSET:
            field_dict["consumed_at"] = consumed_at
        if dequeable_at is not UNSET:
            field_dict["dequeable_at"] = dequeable_at
        if id is not UNSET:
            field_dict["id"] = id
        if inserted_at is not UNSET:
            field_dict["inserted_at"] = inserted_at
        if modes is not UNSET:
            field_dict["modes"] = modes
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if workbench_job_id is not UNSET:
            field_dict["workbench_job_id"] = workbench_job_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.workbench_job_modes import WorkbenchJobModes

        d = dict(src_dict)
        _consumed_at = d.pop("consumed_at", UNSET)
        consumed_at: datetime.datetime | Unset
        if isinstance(_consumed_at, Unset):
            consumed_at = UNSET
        else:
            consumed_at = datetime.datetime.fromisoformat(_consumed_at)

        _dequeable_at = d.pop("dequeable_at", UNSET)
        dequeable_at: datetime.datetime | Unset
        if isinstance(_dequeable_at, Unset):
            dequeable_at = UNSET
        else:
            dequeable_at = datetime.datetime.fromisoformat(_dequeable_at)

        id = d.pop("id", UNSET)

        _inserted_at = d.pop("inserted_at", UNSET)
        inserted_at: datetime.datetime | Unset
        if isinstance(_inserted_at, Unset):
            inserted_at = UNSET
        else:
            inserted_at = datetime.datetime.fromisoformat(_inserted_at)

        _modes = d.pop("modes", UNSET)
        modes: WorkbenchJobModes | Unset
        if isinstance(_modes, Unset):
            modes = UNSET
        else:
            modes = WorkbenchJobModes.from_dict(_modes)

        prompt = d.pop("prompt", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        user_id = d.pop("user_id", UNSET)

        workbench_job_id = d.pop("workbench_job_id", UNSET)

        queued_prompt = cls(
            consumed_at=consumed_at,
            dequeable_at=dequeable_at,
            id=id,
            inserted_at=inserted_at,
            modes=modes,
            prompt=prompt,
            updated_at=updated_at,
            user_id=user_id,
            workbench_job_id=workbench_job_id,
        )

        queued_prompt.additional_properties = d
        return queued_prompt

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
