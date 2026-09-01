from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="HelmSpec")


@_attrs_define
class HelmSpec:
    """Helm chart configuration for a service

    Attributes:
        chart (str | Unset): Helm chart name (e.g., "nginx")
        python_file (str | Unset): A python file to use for helm applies
        python_folder (str | Unset): A folder of python files to include in the final script used
        python_script (str | Unset): A python script to use for helm applies
        release (str | Unset): Helm release name for the deployment
        repository_id (str | Unset): ID of the Helm repository for this chart
        url (str | Unset): URL of the Helm chart repository
        values (str | Unset): Inline helm values for the helm chart
        values_files (list[str] | Unset): List of referenced values.yaml files
        version (str | Unset): Helm chart version
    """

    chart: str | Unset = UNSET
    python_file: str | Unset = UNSET
    python_folder: str | Unset = UNSET
    python_script: str | Unset = UNSET
    release: str | Unset = UNSET
    repository_id: str | Unset = UNSET
    url: str | Unset = UNSET
    values: str | Unset = UNSET
    values_files: list[str] | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chart = self.chart

        python_file = self.python_file

        python_folder = self.python_folder

        python_script = self.python_script

        release = self.release

        repository_id = self.repository_id

        url = self.url

        values = self.values

        values_files: list[str] | Unset = UNSET
        if not isinstance(self.values_files, Unset):
            values_files = self.values_files

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chart is not UNSET:
            field_dict["chart"] = chart
        if python_file is not UNSET:
            field_dict["python_file"] = python_file
        if python_folder is not UNSET:
            field_dict["python_folder"] = python_folder
        if python_script is not UNSET:
            field_dict["python_script"] = python_script
        if release is not UNSET:
            field_dict["release"] = release
        if repository_id is not UNSET:
            field_dict["repository_id"] = repository_id
        if url is not UNSET:
            field_dict["url"] = url
        if values is not UNSET:
            field_dict["values"] = values
        if values_files is not UNSET:
            field_dict["values_files"] = values_files
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        chart = d.pop("chart", UNSET)

        python_file = d.pop("python_file", UNSET)

        python_folder = d.pop("python_folder", UNSET)

        python_script = d.pop("python_script", UNSET)

        release = d.pop("release", UNSET)

        repository_id = d.pop("repository_id", UNSET)

        url = d.pop("url", UNSET)

        values = d.pop("values", UNSET)

        values_files = cast(list[str], d.pop("values_files", UNSET))

        version = d.pop("version", UNSET)

        helm_spec = cls(
            chart=chart,
            python_file=python_file,
            python_folder=python_folder,
            python_script=python_script,
            release=release,
            repository_id=repository_id,
            url=url,
            values=values,
            values_files=values_files,
            version=version,
        )

        helm_spec.additional_properties = d
        return helm_spec

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
