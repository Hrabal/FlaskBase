# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy.orm import RelationshipProperty


def dump_datetime(value):
    if value is None:
        return None
    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d %H:%M:%S")
    raise TypeError


class Dictable:
    def serialize(self, relations=True):
        item_id = getattr(self, "id", getattr(self, "code", None))
        res = {"id": item_id}
        for k, v in self.iter_model():
            if isinstance(v, datetime):
                res.setdefault("data", {})[k] = dump_datetime(v)
            elif isinstance(v, RelationshipProperty):
                if relations:
                    res.setdefault("related", {})[k] = [i.serialize() for i in v]
            else:
                res.setdefault("data", {})[k] = v
        return res

    @property
    def serialize_many2many(self):
        return [item.serialize for item in self.many2many]

    def iter_model(self):
        for col in self.__class__.__table__.columns:
            if col.autoincrement is not True:
                yield col.key, self.__dict__.get(col.key, None)
