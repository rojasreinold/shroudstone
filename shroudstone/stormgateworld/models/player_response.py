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
from pydantic import BaseModel, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from shroudstone.stormgateworld.models.leaderboard_entry_response import LeaderboardEntryResponse
from typing import Optional, Set
from typing_extensions import Self

class PlayerResponse(BaseModel):
    """
    PlayerResponse
    """ # noqa: E501
    id: StrictStr
    anonymous: StrictBool
    nickname: Optional[StrictStr] = None
    nickname_discriminator: Optional[StrictStr] = None
    avatar_url: Optional[StrictStr] = None
    leaderboard_entries: List[LeaderboardEntryResponse]
    last_match_ended_at: Optional[datetime] = None
    last_match_started_at: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["id", "anonymous", "nickname", "nickname_discriminator", "avatar_url", "leaderboard_entries", "last_match_ended_at", "last_match_started_at"]

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
        """Create an instance of PlayerResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in leaderboard_entries (list)
        _items = []
        if self.leaderboard_entries:
            for _item in self.leaderboard_entries:
                if _item:
                    _items.append(_item.to_dict())
            _dict['leaderboard_entries'] = _items
        # set to None if nickname (nullable) is None
        # and model_fields_set contains the field
        if self.nickname is None and "nickname" in self.model_fields_set:
            _dict['nickname'] = None

        # set to None if nickname_discriminator (nullable) is None
        # and model_fields_set contains the field
        if self.nickname_discriminator is None and "nickname_discriminator" in self.model_fields_set:
            _dict['nickname_discriminator'] = None

        # set to None if avatar_url (nullable) is None
        # and model_fields_set contains the field
        if self.avatar_url is None and "avatar_url" in self.model_fields_set:
            _dict['avatar_url'] = None

        # set to None if last_match_ended_at (nullable) is None
        # and model_fields_set contains the field
        if self.last_match_ended_at is None and "last_match_ended_at" in self.model_fields_set:
            _dict['last_match_ended_at'] = None

        # set to None if last_match_started_at (nullable) is None
        # and model_fields_set contains the field
        if self.last_match_started_at is None and "last_match_started_at" in self.model_fields_set:
            _dict['last_match_started_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PlayerResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "anonymous": obj.get("anonymous"),
            "nickname": obj.get("nickname"),
            "nickname_discriminator": obj.get("nickname_discriminator"),
            "avatar_url": obj.get("avatar_url"),
            "leaderboard_entries": [LeaderboardEntryResponse.from_dict(_item) for _item in obj["leaderboard_entries"]] if obj.get("leaderboard_entries") is not None else None,
            "last_match_ended_at": obj.get("last_match_ended_at"),
            "last_match_started_at": obj.get("last_match_started_at")
        })
        return _obj


