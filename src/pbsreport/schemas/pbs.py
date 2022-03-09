from marshmallow import Schema, EXCLUDE, fields, post_load, pre_load


__all__ = ("NodeSchema", "NodesSchema")

class ResourceSchema(Schema):
    dloc = fields.String(load_default=None)
    arch = fields.String(load_default=None)
    cpu_type = fields.String(load_default=None)
    node_type = fields.String(load_default=None)
    network = fields.String(load_default=None)
    cpus = fields.Integer(data_key="ncpus", load_default=0)
    gpus = fields.Integer(data_key="ngpus", load_default=0)
    mem = fields.String(load_default="0kb")

    class Meta:
        unknown = EXCLUDE

class NodeSchema(Schema):
    fqdn = fields.String(data_key="Mom", load_default=None)
    state = fields.String(load_default=None)
    comment = fields.String(load_default=None)
    queue = fields.String(load_default=None)
    resources_available = fields.Nested(ResourceSchema)
    resources_assigned = fields.Nested(ResourceSchema, only=["cpus", "gpus", "mem"])
    jobs = fields.List(fields.String(), load_default=[])

    class Meta:
        unknown = EXCLUDE


class NodesSchema(Schema):
    nodes = fields.Dict(keys=fields.String(), values=fields.Nested(NodeSchema))

    class Meta:
        unknown = EXCLUDE

    @post_load
    def unwrap_envelope(self, data, **_):
        return [{"name": key, **value} for key, value in data["nodes"].items()]
