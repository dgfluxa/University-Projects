
function build_id(name, string2){
    const id = Buffer.from(name + ':' + string2).toString("base64").slice(0, 22);
    console.log(id);
    return id;
}

module.exports = build_id;