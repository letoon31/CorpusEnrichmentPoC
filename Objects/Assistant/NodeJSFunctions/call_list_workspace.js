var watson = require('watson-developer-cloud');

username = process.argv[2].replace(/_/g, " ")
password = process.argv[3].replace(/_/g, " ")

var assistant = new watson.AssistantV1({
  username: username,
  password: password,
  version: '2018-09-20'
});

assistant.listWorkspaces(function(err, response) {
  if (err) {
    console.error(err);
  } else {
    console.log(JSON.stringify(response, null, 2));
  }
});