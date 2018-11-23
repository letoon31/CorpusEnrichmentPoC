var watson = require('watson-developer-cloud');

username = process.argv[2].replace(/_/g, " ")
password = process.argv[3].replace(/_/g, " ")
workspace_id = process.argv[4].replace(/_/g, " ")
entity = process.argv[5].replace(/_/g, " ")

var assistant = new watson.AssistantV1({
  username: username,
  password: password,
  version: '2018-09-20'
});

var params = {
  workspace_id: workspace_id,
  entity: entity
};

assistant.createEntity(params, function(err, response) {
  if (err) {
    console.error(err);
  } else {
    console.log(JSON.stringify(response,null, 2));
  } 
});