from marshmallow import Schema, fields


__all__ = ('NodeSchema',)


class NodeSchema(Schema):
    dloc = fields.String()
    arch = fields.String()
    state = fields.String()
    cpu_type = fields.String()
    node_type = fields.String()
    total_cpus = fields.Integer(attribute="resources_available.ncpus")
    assigned_cpus = fields.Integer(attribute="resources_assigned.ncpus")
    total_gpus = fields.Integer(attribute="resources_available.ngpus")
    assigned_gpus = fields.Integer(attribute="resources_assigned.ngpus")
    total_mem = fields.Integer(attribute="resources_available.mem")
    assigned_mem = fields.Integer(attribute="resources_assigned.mem")
    network = fields.String(attribute="resources_assigned.network")
    jobs = fields.List(fields.String())
