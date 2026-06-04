from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workbench_job_result_metadata import WorkbenchJobResultMetadata
    from ..models.workbench_job_result_todo import WorkbenchJobResultTodo


T = TypeVar("T", bound="WorkbenchJobResult")


@_attrs_define
class WorkbenchJobResult:
    """The result of a workbench job run (working theory, conclusion, todos, metadata)

    Attributes:
        conclusion (str | Unset): The conclusion for this result
        criticism (str | Unset): Markdown-formatted critique of the work done so far, highlighting gaps,
            inconsistencies, and weaknesses in the current investigation
        id (str | Unset): Unique identifier for the result
        inserted_at (datetime.datetime | Unset):
        metadata (WorkbenchJobResultMetadata | Unset): Metadata associated with a workbench job result
        todos (list[WorkbenchJobResultTodo] | Unset): Todos for this result
        updated_at (datetime.datetime | Unset):
        workbench_job_id (str | Unset): ID of the job this result belongs to
        working_theory (str | Unset): The working theory for this result
    """

    conclusion: str | Unset = UNSET
    criticism: str | Unset = UNSET
    id: str | Unset = UNSET
    inserted_at: datetime.datetime | Unset = UNSET
    metadata: WorkbenchJobResultMetadata | Unset = UNSET
    todos: list[WorkbenchJobResultTodo] | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    workbench_job_id: str | Unset = UNSET
    working_theory: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conclusion = self.conclusion

        criticism = self.criticism

        id = self.id

        inserted_at: str | Unset = UNSET
        if not isinstance(self.inserted_at, Unset):
            inserted_at = self.inserted_at.isoformat()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        todos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.todos, Unset):
            todos = []
            for todos_item_data in self.todos:
                todos_item = todos_item_data.to_dict()
                todos.append(todos_item)

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        workbench_job_id = self.workbench_job_id

        working_theory = self.working_theory

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conclusion is not UNSET:
            field_dict["conclusion"] = conclusion
        if criticism is not UNSET:
            field_dict["criticism"] = criticism
        if id is not UNSET:
            field_dict["id"] = id
        if inserted_at is not UNSET:
            field_dict["inserted_at"] = inserted_at
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if todos is not UNSET:
            field_dict["todos"] = todos
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if workbench_job_id is not UNSET:
            field_dict["workbench_job_id"] = workbench_job_id
        if working_theory is not UNSET:
            field_dict["working_theory"] = working_theory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workbench_job_result_metadata import WorkbenchJobResultMetadata
        from ..models.workbench_job_result_todo import WorkbenchJobResultTodo

        d = dict(src_dict)
        conclusion = d.pop("conclusion", UNSET)

        criticism = d.pop("criticism", UNSET)

        id = d.pop("id", UNSET)

        _inserted_at = d.pop("inserted_at", UNSET)
        inserted_at: datetime.datetime | Unset
        if isinstance(_inserted_at, Unset):
            inserted_at = UNSET
        else:
            inserted_at = datetime.datetime.fromisoformat(_inserted_at)

        _metadata = d.pop("metadata", UNSET)
        metadata: WorkbenchJobResultMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = WorkbenchJobResultMetadata.from_dict(_metadata)

        _todos = d.pop("todos", UNSET)
        todos: list[WorkbenchJobResultTodo] | Unset = UNSET
        if _todos is not UNSET:
            todos = []
            for todos_item_data in _todos:
                todos_item = WorkbenchJobResultTodo.from_dict(todos_item_data)

                todos.append(todos_item)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        workbench_job_id = d.pop("workbench_job_id", UNSET)

        working_theory = d.pop("working_theory", UNSET)

        workbench_job_result = cls(
            conclusion=conclusion,
            criticism=criticism,
            id=id,
            inserted_at=inserted_at,
            metadata=metadata,
            todos=todos,
            updated_at=updated_at,
            workbench_job_id=workbench_job_id,
            working_theory=working_theory,
        )

        workbench_job_result.additional_properties = d
        return workbench_job_result

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
