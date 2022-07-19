var fs = require("fs");

fs.readFile("itemdb.js", "utf-8", (err, data) => {
  console.log(data);
});