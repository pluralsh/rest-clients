from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workbench_job_result_metric import WorkbenchJobResultMetric


T = TypeVar("T", bound="WorkbenchJobResultMetadata")


@_attrs_define
class WorkbenchJobResultMetadata:
    """Metadata associated with a workbench job result

    Attributes:
        metrics (list[WorkbenchJobResultMetric] | Unset): Metrics for this result
    """

    metrics: list[WorkbenchJobResultMetric] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metrics: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = []
            for metrics_item_data in self.metrics:
                metrics_item = metrics_item_data.to_dict()
                metrics.append(metrics_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metrics is not UNSET:
            field_dict["metrics"] = metrics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workbench_job_result_metric import WorkbenchJobResultMetric

        d = dict(src_dict)
        _metrics = d.pop("metrics", UNSET)
        metrics: list[WorkbenchJobResultMetric] | Unset = UNSET
        if _metrics is not UNSET:
            metrics = []
            for metrics_item_data in _metrics:
                metrics_item = WorkbenchJobResultMetric.from_dict(metrics_item_data)

                metrics.append(metrics_item)

        workbench_job_result_metadata = cls(
            metrics=metrics,
        )

        workbench_job_result_metadata.additional_properties = d
        return workbench_job_result_metadata

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
