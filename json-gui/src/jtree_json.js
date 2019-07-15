var craeteJtreeJson = function(name, schema) {
    var node = null;
    if (schema.type == "object") {
        console.log(schema);
        var children_nodes = [];
        for (var key in schema.properties) {
            var kid_schema = schema.properties[key];
            children_nodes.push(craeteJtreeJson(key, kid_schema));
        }
        node = {
            "text" : schema.title ? schema.title : schema.id,
            "children" : children_nodes,
            "extral_schema" : schema,
        };
    } else {
        node = {
            "text" : schema.title ? schema.title : name,
            "extral_schema" : schema
        };
    }
    return node;
};
