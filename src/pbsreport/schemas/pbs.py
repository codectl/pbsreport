from functools import partial

from marshmallow import Schema, EXCLUDE, fields, post_load

from pbsreport import utils

__all__ = ("NodeSchema", "NodesSchema")


class ResourceSchema(Schema):
    cpus = fields.Integer(data_key="ncpus", load_default=0)
    gpus = fields.Integer(data_key="ngpus", load_default=0)
    mem = fields.String(load_default="0kb")

    class Meta:
        unknown = EXCLUDE


class NodeSchema(Schema):
    fqdn = fields.String(data_key="Mom", load_default="-")
    state = fields.String(load_default="-")
    comment = fields.String(load_default="-")
    queue = fields.String(load_default="-")
    dloc = fields.Function(
        data_key="resources_available", deserialize=lambda x: x.get("dloc", "-")
    )
    arch = fields.Function(
        data_key="resources_available", deserialize=lambda x: x.get("arch", "-")
    )
    cpu_type = fields.Function(
        data_key="resources_available", deserialize=lambda x: x.get("cpu_type", "-")
    )
    node_type = fields.Function(
        data_key="resources_available", deserialize=lambda x: x.get("node_type", "-")
    )
    network = fields.Function(
        data_key="resources_available", deserialize=lambda x: x.get("network", "-")
    )
    resources_available = fields.Nested(ResourceSchema)
    resources_assigned = fields.Nested(ResourceSchema)
    jobs = fields.List(fields.String(), load_default=[])

    class Meta:
        unknown = EXCLUDE

    @post_load
    def unwrap_envelope(self, data, **_):
        mem_available = data["resources_available"]["mem"]
        mem_assigned = data["resources_assigned"]["mem"]
        data["resources_available"]["mem"] = utils.convert_raw_bytes(mem_available)
        data["resources_assigned"]["mem"] = utils.convert_raw_bytes(mem_available)
        return data


class NodesSchema(Schema):
    nodes = fields.Dict(keys=fields.String(), values=fields.Nested(NodeSchema))

    class Meta:
        unknown = EXCLUDE

    @post_load
    def unwrap_envelope(self, data, **_):
        return [{"name": key, **value} for key, value in data["nodes"].items()]
