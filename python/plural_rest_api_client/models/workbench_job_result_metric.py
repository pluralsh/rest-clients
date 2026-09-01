from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workbench_job_result_metric_labels import (
        WorkbenchJobResultMetricLabels,
    )


T = TypeVar("T", bound="WorkbenchJobResultMetric")


@_attrs_define
class WorkbenchJobResultMetric:
    """A metric persisted on the job result

    Attributes:
        labels (WorkbenchJobResultMetricLabels | Unset): Labels for the metric
        name (str | Unset): Name of the metric
        timestamp (str | Unset): ISO 8601 timestamp of the metric
        value (float | Unset): Value of the metric
    """

    labels: WorkbenchJobResultMetricLabels | Unset = UNSET
    name: str | Unset = UNSET
    timestamp: str | Unset = UNSET
    value: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        name = self.name

        timestamp = self.timestamp

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if labels is not UNSET:
            field_dict["labels"] = labels
        if name is not UNSET:
            field_dict["name"] = name
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.workbench_job_result_metric_labels import (
            WorkbenchJobResultMetricLabels,
        )

        d = dict(src_dict)
        _labels = d.pop("labels", UNSET)
        labels: WorkbenchJobResultMetricLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = WorkbenchJobResultMetricLabels.from_dict(_labels)

        name = d.pop("name", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        value = d.pop("value", UNSET)

        workbench_job_result_metric = cls(
            labels=labels,
            name=name,
            timestamp=timestamp,
            value=value,
        )

        workbench_job_result_metric.additional_properties = d
        return workbench_job_result_metric

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
