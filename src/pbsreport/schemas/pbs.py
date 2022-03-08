from marshmallow import Schema, fields, pre_load


__all__ = ('NodeSchema',)


class NodeSchema(Schema):
    state = fields.String()
    comment = fields.String()
    queue = fields.String()
    dloc = fields.String(attribute="resources_available.dloc")
    arch = fields.String(attribute="resources_available.arch")
    cpu_type = fields.String(attribute="resources_available.cpu_type")
    node_type = fields.String(attribute="resources_available.node_type")
    total_cpus = fields.Integer(attribute="resources_available.ncpus")
    assigned_cpus = fields.Integer(attribute="resources_assigned.ncpus")
    total_gpus = fields.Integer(attribute="resources_available.ngpus")
    assigned_gpus = fields.Integer(attribute="resources_assigned.ngpus")
    total_mem = fields.Integer(attribute="resources_available.mem")
    assigned_mem = fields.Integer(attribute="resources_assigned.mem")
    network = fields.String(attribute="resources_assigned.network")
    jobs = fields.List(fields.String())

    @pre_load(pass_many=True)
    def unwrap_envelope(self, data, many, **kwargs):
        key = self.opts.plural_name if many else self.opts.name
        return data[key]
