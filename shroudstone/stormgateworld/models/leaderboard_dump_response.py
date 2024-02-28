# coding: utf-8

"""
    api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from shroudstone.stormgateworld.models.leaderboard_entry_response import LeaderboardEntryResponse
from typing import Optional, Set
from typing_extensions import Self

class LeaderboardDumpResponse(BaseModel):
    """
    LeaderboardDumpResponse
    """ # noqa: E501
    count: Annotated[int, Field(strict=True, ge=0)]
    cached_at: datetime
    entries: List[LeaderboardEntryResponse]
    __properties: ClassVar[List[str]] = ["count", "cached_at", "entries"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of LeaderboardDumpResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in entries (list)
        _items = []
        if self.entries:
            for _item in self.entries:
                if _item:
                    _items.append(_item.to_dict())
            _dict['entries'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LeaderboardDumpResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "count": obj.get("count"),
            "cached_at": obj.get("cached_at"),
            "entries": [LeaderboardEntryResponse.from_dict(_item) for _item in obj["entries"]] if obj.get("entries") is not None else None
        })
        return _obj


