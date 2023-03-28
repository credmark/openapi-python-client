# AModelA Model for testing all the ways custom objects can be used




## Properties
Name | Type | Description
------------ | ------------- | -------------
an_enum_value | AnEnum | For testing Enums in all the ways they can be used 
an_allof_enum_with_overridden_default | AnAllOfEnum | None
a_camel_date_time | Union[datetime.date, datetime.datetime] | None
a_date | datetime.date | None
required_not_nullable | str | None
one_of_models | Union['FreeFormModel', 'ModelWithUnionProperty', Any] | None
model | ModelWithUnionProperty | 
any_value | Union[Unset, Any] | None
an_optional_allof_enum | Union[Unset, AnAllOfEnum] | None
nested_list_of_enums | Union[Unset, List[List[DifferentEnum]]] | None
a_nullable_date | Optional[datetime.date] | None
a_not_required_date | Union[Unset, datetime.date] | None
attr_1_leading_digit | Union[Unset, str] | None
attr_leading_underscore | Union[Unset, str] | None
required_nullable | Optional[str] | None
not_required_nullable | Union[Unset, None, str] | None
not_required_not_nullable | Union[Unset, str] | None
nullable_one_of_models | Union['FreeFormModel', 'ModelWithUnionProperty', None] | None
not_required_one_of_models | Union['FreeFormModel', 'ModelWithUnionProperty', Unset] | None
not_required_nullable_one_of_models | Union['FreeFormModel', 'ModelWithUnionProperty', None, Unset, str] | None
nullable_model | Optional[ModelWithUnionProperty] | 
not_required_model | Union[Unset, ModelWithUnionProperty] | 
not_required_nullable_model | Union[Unset, None, ModelWithUnionProperty] | 

