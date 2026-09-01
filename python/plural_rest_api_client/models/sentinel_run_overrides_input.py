from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sentinel_run_overrides_input_tags import SentinelRunOverridesInputTags


T = TypeVar("T", bound="SentinelRunOverridesInput")


@_attrs_define
class SentinelRunOverridesInput:
    """Optional overrides applied when triggering a sentinel run

    Attributes:
        tags (SentinelRunOverridesInputTags | Unset): Tags to merge into integration test checks for this run
    """

    tags: SentinelRunOverridesInputTags | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.sentinel_run_overrides_input_tags import (
            SentinelRunOverridesInputTags,
        )

        d = dict(src_dict)
        _tags = d.pop("tags", UNSET)
        tags: SentinelRunOverridesInputTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = SentinelRunOverridesInputTags.from_dict(_tags)

        sentinel_run_overrides_input = cls(
            tags=tags,
        )

        sentinel_run_overrides_input.additional_properties = d
        return sentinel_run_overrides_input

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
