from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AFormData")


@attr.s(auto_attribs=True)
class AFormData:
    """
    Attributes:
        an_required_field (str):
        an_optional_field (Union[Unset, str]):
        a_simple_dict (Union[Unset, Dict[str, Any]]):
    """

    an_required_field: str
    an_optional_field: Union[Unset, str] = UNSET
    a_simple_dict: Union[Unset, Dict[str, Any]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        an_required_field = self.an_required_field
        an_optional_field = self.an_optional_field
        a_simple_dict = self.a_simple_dict

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "an_required_field": an_required_field,
            }
        )
        if an_optional_field is not UNSET:
            field_dict["an_optional_field"] = an_optional_field
        if a_simple_dict is not UNSET:
            field_dict["a_simple_dict"] = a_simple_dict

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        an_required_field = d.pop("an_required_field")

        an_optional_field = d.pop("an_optional_field", UNSET)

        a_simple_dict = d.pop("a_simple_dict", UNSET)

        a_form_data = cls(
            an_required_field=an_required_field,
            an_optional_field=an_optional_field,
            a_simple_dict=a_simple_dict,
        )

        a_form_data.additional_properties = d
        return a_form_data

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
