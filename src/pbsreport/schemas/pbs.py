from marshmallow import Schema, EXCLUDE, fields, post_load, pre_load


__all__ = ("NodeSchema", "NodesSchema")


class NodeSchema(Schema):
    hostname = fields.String(data_key='Mom')
    state = fields.String()
    comment = fields.String()
    queue = fields.String()
    resources_available = fields.Nested(Schema.from_dict({
        "dloc": fields.String(),
        "arch": fields.String(),
        "cpu_type": fields.String(),
        "node_type": fields.String(),
        "network": fields.String(),
        "cpus": fields.Integer(data_key='ncpus', load_default=0),
        "gpus": fields.Integer(data_key='ngpus', load_default=0),
        "mem": fields.String(load_default="0kb")
    }), unknown=EXCLUDE)
    resources_assigned = fields.Nested(Schema.from_dict({
        "cpus": fields.Integer(data_key='ncpus', load_default=0),
        "gpus": fields.Integer(data_key='ngpus', load_default=0),
        "mem": fields.String(load_default="0kb")
    }), unknown=EXCLUDE)
    jobs = fields.List(fields.String())

    class Meta:
        unknown = EXCLUDE


class NodesSchema(Schema):
    nodes = fields.Dict(keys=fields.String(), values=fields.Nested(NodeSchema))

    class Meta:
        unknown = EXCLUDE

    @post_load
    def unwrap_envelope(self, data, **kwargs):
        unwrap = []
        for key, value in data["nodes"].items():
            value["node"] = key
            unwrap.append(value)
        return unwrap
